"""
KPI components for the Barcelona Vehicle Dashboard.
"""
from dash import html
from config.settings import COLORS


def create_kpi_overview_card():
    """
    Create the KPI overview card component.
    
    Returns:
        html.Div: KPI overview card component
    """
    return html.Div([
        html.H3("Overview", style={
            'font-size': '14px', 
            'font-weight': '600', 
            'margin-bottom': '16px', 
            'color': COLORS['text']
        }),

        html.Div([
            # Total vehicles KPI
            html.Div([
                html.Div(
                    id='total-vehicles', 
                    className='kpi-value', 
                    style={
                        'font-size': '28px', 
                        'font-weight': '500', 
                        'color': COLORS['text'], 
                        'margin-bottom': '4px'
                    }
                ),
                html.Div("Total Vehicles", style={
                    'font-size': '12px', 
                    'color': COLORS['subtext']
                })
            ], style={'marginBottom': '16px'}),

            # Electric percentage KPI
            html.Div([
                html.Div(
                    id='electric-percent', 
                    className='kpi-value', 
                    style={
                        'font-size': '24px', 
                        'font-weight': '500', 
                        'color': COLORS['Electric'], 
                        'margin-bottom': '4px'
                    }
                ),
                html.Div("Electric", style={
                    'font-size': '12px', 
                    'color': COLORS['subtext']
                })
            ], style={'marginBottom': '16px'}),

            # Hybrid percentage KPI
            html.Div([
                html.Div(
                    id='hybrid-percent', 
                    className='kpi-value', 
                    style={
                        'font-size': '24px', 
                        'font-weight': '500', 
                        'color': COLORS['Hybrid'], 
                        'margin-bottom': '4px'
                    }
                ),
                html.Div("Hybrid", style={
                    'font-size': '12px', 
                    'color': COLORS['subtext']
                })
            ], style={'marginBottom': '16px'}),

            # Sustainable vehicles progress bar
            html.Div([
                html.Div("Sustainable Vehicles", style={
                    'font-size': '12px', 
                    'color': COLORS['subtext'], 
                    'marginBottom': '8px'
                }),
                html.Div(id='progress-container', style={
                    'height': '8px',
                    'backgroundColor': COLORS['Others'],
                    'borderRadius': '4px',
                    'overflow': 'hidden'
                }),
                html.Div(id='sustainable-percent', style={
                    'fontSize': '12px', 
                    'color': COLORS['subtext'], 
                    'marginTop': '4px', 
                    'textAlign': 'right'
                })
            ], style={'marginBottom': '16px'}),

            # Year-over-year change
            html.Div([
                html.Div("YoY Change", style={
                    'font-size': '12px', 
                    'color': COLORS['subtext'], 
                    'marginBottom': '8px'
                }),
                html.Div([
                    html.Div(id='yoy-value', style={
                        'fontSize': '16px', 
                        'fontWeight': '500'
                    })
                ], style={'display': 'flex', 'alignItems': 'center'}),
            ])
        ])
    ], style={
        'padding': '16px', 
        'background-color': COLORS['panel'], 
        'borderRadius': '8px', 
        'boxShadow': '0 1px 2px rgba(0,0,0,0.06)', 
        'flex': '1'
    })