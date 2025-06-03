"""
Main layout for the Barcelona Vehicle Dashboard.
"""
from dash import html
from config.settings import COLORS, APP_TITLE
from src.components.filters import create_filters_card
from src.components.kpis import create_kpi_overview_card
from src.components.charts import create_main_charts_section
from src.data.loader import load_data


def create_header():
    """
    Create the header component.
    
    Returns:
        html.Div: Header component
    """
    return html.Div([
        html.H1(APP_TITLE, style={
            'font-weight': '500', 
            'font-size': '24px', 
            'color': COLORS['text'], 
            'margin': '0'
        })
    ], style={
        'padding': '20px 0', 
        'margin-bottom': '20px', 
        'border-bottom': f'1px solid {COLORS["border"]}'
    })


def create_sidebar(df):
    """
    Create the sidebar with filters and KPIs.
    
    Args:
        df (pd.DataFrame): Vehicle data
        
    Returns:
        html.Div: Sidebar component
    """
    return html.Div([
        create_filters_card(df),
        create_kpi_overview_card()
    ], style={
        'width': '24%', 
        'display': 'flex', 
        'flexDirection': 'column'
    })


def create_main_content():
    """
    Create the main content area.
    
    Returns:
        html.Div: Main content component
    """
    return html.Div([
        create_header(),
        html.Div([
            create_sidebar(load_data()),
            create_main_charts_section()
        ], style={
            'display': 'flex',
            'alignItems': 'stretch',
            'margin-bottom': '20px',
            'height': 'auto'
        })
    ], style={
        'width': '100%',
        'maxWidth': '1400px',
        'margin': '0 auto',
        'font-family': 'Inter, system-ui, sans-serif',
        'padding': '20px',
        'backgroundColor': COLORS['background']
    })


def create_main_layout():
    """
    Create the complete main layout.
    
    Returns:
        html.Div: Complete layout component
    """
    return create_main_content()