"""Configuration settings for the Barcelona Vehicle Dashboard."""

# Color scheme - monochromatic with accent colors
COLORS = {
    'background': '#FFFFFF',
    'panel': '#F5F7FA',
    'text': '#172B4D',
    'subtext': '#7A869A',
    'border': '#E6E8EB',
    'Gasoline': '#FF9D4D',
    'Diesel': '#5E6C84',
    'Electric': '#36B5F6',
    'Hybrid': '#57D9A3',
    'Others': '#EBECF0',
    'Unknown': '#7B50A5',
    'accent': '#0065FF'
}

# Application settings
APP_TITLE = "Barcelona Vehicle Propulsion"
CSV_PATH = 'data/vehicles_by_area_and_type.csv'

# Chart configuration
CHART_CONFIG = {'displayModeBar': False}
CHART_HEIGHT = 325

# Layout dimensions
SIDEBAR_WIDTH = '24%'
MAIN_CONTENT_MARGIN = '2%'