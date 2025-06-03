"""
Filter components for the Barcelona Vehicle Dashboard.
"""
from dash import dcc, html
from config.settings import COLORS
from src.data.loader import get_years, get_districts, get_propulsion_types


def create_filters_card(df):
    """
    Create the filters card component.
    
    Args:
        df (pd.DataFrame): Vehicle data
        
    Returns:
        html.Div: Filters card component
    """
    years = get_years(df)
    districts = get_districts(df)
    propulsion_types = get_propulsion_types(df)
    
    return html.Div([
        html.H3("Filters", style={
            'font-size': '14px', 
            'font-weight': '600', 
            'margin-bottom': '16px', 
            'color': COLORS['text']
        }),

        # Year filter
        html.Div([
            html.Label("Year", style={
                'font-size': '12px', 
                'font-weight': '500', 
                'margin-bottom': '4px', 
                'color': COLORS['subtext']
            }),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in years],
                value=max(years),
                clearable=False,
                style={'border': 'none'}
            ),
        ], style={'margin-bottom': '16px'}),

        # Propulsion type filter
        html.Div([
            html.Label("Propulsion Type", style={
                'font-size': '12px', 
                'font-weight': '500', 
                'margin-bottom': '4px', 
                'color': COLORS['subtext']
            }),
            dcc.Dropdown(
                id='propulsion-dropdown',
                options=[{'label': t, 'value': t} for t in propulsion_types],
                value=None,
                multi=True,
                style={'border': 'none'}
            ),
        ], style={'margin-bottom': '16px'}),

        # District filter
        html.Div([
            html.Label("District", style={
                'font-size': '12px', 
                'font-weight': '500', 
                'margin-bottom': '4px', 
                'color': COLORS['subtext']
            }),
            dcc.Dropdown(
                id='district-dropdown',
                options=[{'label': d, 'value': d} for d in districts],
                style={'border': 'none'}
            ),
        ], style={'margin-bottom': '16px'}),

        # Neighborhood filter
        html.Div([
            html.Label("Neighborhood", style={
                'font-size': '12px', 
                'font-weight': '500', 
                'margin-bottom': '4px', 
                'color': COLORS['subtext']
            }),
            dcc.Dropdown(
                id='neighborhood-dropdown',
                options=[],
                value='Sant Pere, Santa Caterina i la Ribera',
                style={'border': 'none'}
            ),
        ]),
    ], style={
        'padding': '16px', 
        'background-color': COLORS['panel'], 
        'borderRadius': '8px', 
        'boxShadow': '0 1px 2px rgba(0,0,0,0.06)', 
        'marginBottom': '16px'
    })