"""
Main callbacks for the Barcelona Vehicle Dashboard.
"""
from dash import Input, Output, callback_context, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from config.settings import COLORS
from src.data.loader import get_neighborhoods
from src.utils.helpers import (
    filter_dataframe, 
    calculate_sustainable_percentage,
    calculate_yoy_change,
    format_number,
    create_base_chart_layout
)
from src.utils.constants import DEFAULTS


def register_callbacks(app, df):
    """
    Register all callbacks for the dashboard.
    
    Args:
        app: Dash application instance
        df (pd.DataFrame): Vehicle dataframe
    """
    
    @app.callback(
        [Output('neighborhood-dropdown', 'options'),
         Output('total-vehicles', 'children'),
         Output('electric-percent', 'children'),
         Output('hybrid-percent', 'children'),
         Output('distribution-chart', 'figure'),
         Output('trends-chart', 'figure'),
         Output('top-neighborhoods-chart', 'figure'),
         Output('progress-container', 'children'),
         Output('sustainable-percent', 'children'),
         Output('yoy-value', 'children'),
         Output('yoy-value', 'style')],
        [Input('year-dropdown', 'value'),
         Input('propulsion-dropdown', 'value'),
         Input('district-dropdown', 'value'),
         Input('neighborhood-dropdown', 'value')],
        prevent_initial_call=False
    )
    def update_dashboard(year, propulsion_types, district, neighborhood):
        """Main callback to update all dashboard components."""
        
        # 1. Update neighborhood options
        neighborhood_options = []
        if district:
            neighborhoods = get_neighborhoods(df, district)
            neighborhood_options = [{'label': n, 'value': n} for n in neighborhoods]
        
        # 2. Calculate KPIs
        filtered_df = filter_dataframe(df, year, district, neighborhood)
        total = filtered_df['number'].sum()
        
        # Electric percentage
        electric_data = filtered_df[filtered_df['type_of_propulsion'] == 'Electric']
        electric_percent = (electric_data['number'].sum() / total * 100) if total > 0 else 0
        
        # Hybrid percentage
        hybrid_data = filtered_df[filtered_df['type_of_propulsion'] == 'Hybrid']
        hybrid_percent = (hybrid_data['number'].sum() / total * 100) if total > 0 else 0
        
        # Sustainable percentage
        sustainable_percent = electric_percent + hybrid_percent
        
        # Progress bar for sustainable vehicles
        progress_bar = html.Div(style={
            'width': f'{sustainable_percent}%',
            'height': '100%',
            'backgroundColor': COLORS['Electric'],
            'borderRadius': '4px',
            'transition': 'width 0.5s ease'
        })
        
        # Year-over-year change
        yoy_change, yoy_color = calculate_yoy_change(df, year, district, neighborhood)
        yoy_style = {'fontSize': '16px', 'fontWeight': '500', 'color': yoy_color}
        
        if year > min(df['year'].unique()):
            if yoy_change > 0:
                yoy_value = f"↑ +{yoy_change:.1f}%"
            elif yoy_change < 0:
                yoy_value = f"↓ {yoy_change:.1f}%"
            else:
                yoy_value = "±0.0%"
        else:
            yoy_value = "N/A"
        
        # 3. Create charts
        distribution_fig = create_distribution_chart(df, year, district, neighborhood, propulsion_types)
        trends_fig = create_trends_chart(df, district, neighborhood)
        top_neighborhoods_fig = create_top_neighborhoods_chart(df, year)
        
        return (
            neighborhood_options,
            format_number(total),
            f"{electric_percent:.1f}%",
            f"{hybrid_percent:.1f}%",
            distribution_fig,
            trends_fig,
            top_neighborhoods_fig,
            progress_bar,
            f"{sustainable_percent:.1f}% Sustainable",
            yoy_value,
            yoy_style
        )


def create_distribution_chart(df, year, district, neighborhood, propulsion_types):
    """Create the distribution chart."""
    filtered_df = filter_dataframe(df, year)
    
    if district:
        if neighborhood:
            # Show propulsion types for selected neighborhood
            filtered_df = filter_dataframe(filtered_df, district=district, neighborhood=neighborhood)
            group_by = 'type_of_propulsion'
            chart_title = f"Propulsion Types in {neighborhood} ({year})"
        else:
            # Show neighborhoods in selected district
            filtered_df = filter_dataframe(filtered_df, district=district)
            group_by = 'neighborhood'
            chart_title = f"Neighborhoods in {district} ({year})"
    else:
        # Show districts
        group_by = 'district'
        chart_title = f"Vehicle Distribution by District ({year})"
    
    if propulsion_types:
        filtered_df = filtered_df[filtered_df['type_of_propulsion'].isin(propulsion_types)]
    
    if group_by == 'type_of_propulsion':
        # Simple bar chart for propulsion types
        result_df = filtered_df.groupby('type_of_propulsion')['number'].sum().reset_index()
        fig = px.bar(
            result_df, 
            x='type_of_propulsion', 
            y='number',
            color='type_of_propulsion',
            color_discrete_map=COLORS
        )
    else:
        # Stacked bar chart for districts/neighborhoods
        pivot_df = filtered_df.pivot_table(
            index=group_by, 
            columns='type_of_propulsion', 
            values='number', 
            aggfunc='sum'
        ).reset_index().fillna(0)
        
        # Sort by total vehicles
        pivot_df['Total'] = pivot_df.sum(axis=1, numeric_only=True)
        pivot_df = pivot_df.sort_values('Total', ascending=False).drop('Total', axis=1)
        
        fig = go.Figure()
        for propulsion in ['Unknown', 'Others', 'Electric', 'Hybrid', 'Diesel', 'Gasoline']:
            if propulsion in pivot_df.columns:
                fig.add_trace(go.Bar(
                    name=propulsion,
                    x=pivot_df[group_by],
                    y=pivot_df[propulsion],
                    marker_color=COLORS[propulsion]
                ))
        
        fig.update_layout(barmode='stack')
    
    # Apply base layout
    layout = create_base_chart_layout(chart_title)
    layout.update({
        'legend_title_text':'',
        'xaxis_title': None,
        'yaxis_title': None,
        'legend': dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        'xaxis': dict(showgrid=False, tickangle=30),
        'yaxis': dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    })
    
    fig.update_layout(layout)
    return fig


def create_trends_chart(df, district, neighborhood):
    """Create the trends chart."""
    filtered_df = filter_dataframe(df, district=district, neighborhood=neighborhood)
    
    # Group by year and propulsion type
    trends_df = filtered_df.groupby(['year', 'type_of_propulsion'])['number'].sum().reset_index()
    
    # Calculate percentages
    total_by_year = trends_df.groupby('year')['number'].sum().reset_index()
    trends_df = trends_df.merge(total_by_year, on='year', suffixes=('', '_total'))
    trends_df['percentage'] = (trends_df['number'] / trends_df['number_total'] * 100).round(1)
    
    fig = px.line(
        trends_df, 
        x='year', 
        y='percentage', 
        color='type_of_propulsion',
        color_discrete_map=COLORS
    )
    
    fig.update_traces(line=dict(width=2.5, shape='spline'))
    
    location_name = neighborhood if neighborhood else district if district else "Barcelona"
    chart_title = f"Propulsion Trends in {location_name}"
    
    layout = create_base_chart_layout(chart_title)
    layout.update({
        'xaxis_title': None,
        'yaxis_title': "Percentage (%)",
        'xaxis': dict(showgrid=False, tickformat='d'),
        'yaxis': dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        'showlegend': False,
        'margin': dict(l=30, r=20, t=40, b=20)
    })
    
    fig.update_layout(layout)
    return fig


def create_top_neighborhoods_chart(df, year):
    """Create the top neighborhoods chart."""
    year_df = filter_dataframe(df, year)
    
    # Calculate electric vehicle percentage by neighborhood
    ev_by_neighborhood = year_df[year_df['type_of_propulsion'] == 'Electric'].groupby('neighborhood')['number'].sum().reset_index()
    total_by_neighborhood = year_df.groupby('neighborhood')['number'].sum().reset_index()
    
    result_df = ev_by_neighborhood.merge(
        total_by_neighborhood, 
        on='neighborhood', 
        suffixes=('_electric', '_total')
    )
    result_df['percentage'] = (result_df['number_electric'] / result_df['number_total'] * 100).round(1)
    
    # Get top 5 neighborhoods
    top_5 = result_df.sort_values('percentage', ascending=False).head(5)
    
    fig = px.bar(
        top_5, 
        x='percentage', 
        y='neighborhood',
        orientation='h',
        text='percentage',
        color_discrete_sequence=[COLORS['Electric']]
    )
    
    fig.update_traces(
        texttemplate='%{text:.1f}%', 
        textposition='inside'
    )
    
    layout = create_base_chart_layout(f"Top 5 Neighborhoods by Electric Adoption ({year})")
    layout.update({
        'xaxis_title': "Electric Vehicles (%)",
        'yaxis_title': None,
        'yaxis': dict(autorange="reversed", showgrid=False),
        'xaxis': dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    })
    
    fig.update_layout(layout)
    return fig