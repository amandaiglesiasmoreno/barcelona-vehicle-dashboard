"""
Main application factory for the Barcelona Vehicle Dashboard.
"""
import dash
from config.settings import APP_TITLE
from src.layouts.main_layout import create_main_layout
from src.callbacks.main_callbacks import register_callbacks
from src.data.loader import load_data


def create_app():
    """Create and configure the Dash application."""
    # Initialize the Dash app
    app = dash.Dash(
        __name__, 
        title=APP_TITLE,
        assets_folder='../assets',
        suppress_callback_exceptions=True
    )
    
    # Load data
    df = load_data()
    
    # Create layout
    app.layout = create_main_layout()
    
    # Register callbacks
    register_callbacks(app, df)
    
    # Custom HTML template
    app.index_string = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Inter', system-ui, sans-serif;
                background-color: #F9FAFB;
                margin: 0;
                padding: 0;
                color: #172B4D;
            }
            
            .Select-control {
                border: 1px solid #DFE1E6 !important;
                border-radius: 4px !important;
                box-shadow: none !important;
                font-size: 13px;
                transition: all 0.2s ease;
            }
            
            .Select-control:hover {
                border-color: #B3BAC5 !important;
            }
            
            .Select-menu-outer {
                border: 1px solid #DFE1E6 !important;
                box-shadow: 0 4px 8px rgba(0,0,0,0.05) !important;
                border-radius: 4px !important;
            }
            
            .js-plotly-plot .plotly {
                font-family: 'Inter', system-ui, sans-serif !important;
            }
            
            *:focus {
                outline: none !important;
            }
            
            .chart-card {
                transition: all 0.3s ease;
            }
            
            .chart-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
    </html>
    '''
    
    return app