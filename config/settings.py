"""
Configuration settings for the Barcelona Vehicle Dashboard.
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data configuration
DATA_DIR = BASE_DIR / "data"
CSV_FILE = DATA_DIR / "vehicles_by_area_and_type.csv"

# App configuration
APP_TITLE = "Barcelona Vehicle Propulsion"
DEBUG_MODE = os.getenv('DEBUG', 'True').lower() == 'true'
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8050))

# Color scheme
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

# Chart configuration
CHART_CONFIG = {
    'displayModeBar': False
}

CHART_HEIGHT = 325