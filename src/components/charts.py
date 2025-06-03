"""
Chart components for the Barcelona Vehicle Dashboard.
"""
from dash import dcc, html
from config.settings import COLORS, CHART_CONFIG, CHART_HEIGHT


def create_chart_container(chart_id, style_overrides=None):
    """
    Create a standardized chart container.
    
    Args:
        chart_id (str): ID for the chart component
        style_overrides (dict): Optional style overrides
        
    Returns:
        html.Div: Chart container component
    """
    base_style = {
        'backgroundColor': COLORS['panel'],
        'padding': '16px',
        'borderRadius': '8px',
        'boxShadow': '0 1px 2px rgba(0,0,0,0.06)',
        'flex': '1'
    }
    
    if style_overrides:
        base_style.update(style_overrides)
    
    return html.Div([
        dcc.Graph(
            id=chart_id,
            config=CHART_CONFIG,
            style={'height': f'{CHART_HEIGHT}px'}
        )
    ], style=base_style)


def create_main_charts_section():
    """
    Create the main charts section with distribution and trends.
    
    Returns:
        html.Div: Charts section component
    """
    return html.Div([
        # Top chart: Distribution
        create_chart_container(
            'distribution-chart',
            {'marginBottom': '16px'}
        ),

        # Bottom row: Two side-by-side charts
        html.Div([
            create_chart_container(
                'trends-chart',
                {
                    'width': '60%',
                    'display': 'flex',
                    'flexDirection': 'column'
                }
            ),
            create_chart_container(
                'top-neighborhoods-chart',
                {
                    'width': '38%',
                    'display': 'flex',
                    'flexDirection': 'column'
                }
            )
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between',
            'gap': '2%',
            'flex': '1'
        })
    ], style={
        'flex': '1', 
        'marginLeft': '2%', 
        'display': 'flex', 
        'flexDirection': 'column'
    })