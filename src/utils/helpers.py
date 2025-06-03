
"""
Helper functions for the Barcelona Vehicle Dashboard.
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from config.settings import COLORS
from src.utils.constants import SUSTAINABLE_TYPES, DEFAULTS


def filter_dataframe(df, year=None, district=None, neighborhood=None, propulsion_types=None):
    """
    Filter dataframe based on provided criteria.
    
    Args:
        df (pd.DataFrame): Original dataframe
        year (int): Year to filter by
        district (str): District to filter by
        neighborhood (str): Neighborhood to filter by
        propulsion_types (list): List of propulsion types to filter by
        
    Returns:
        pd.DataFrame: Filtered dataframe
    """
    filtered_df = df.copy()
    
    if year is not None:
        filtered_df = filtered_df[filtered_df['year'] == year]
    
    if district:
        filtered_df = filtered_df[filtered_df['district'] == district]
    
    if neighborhood:
        filtered_df = filtered_df[filtered_df['neighborhood'] == neighborhood]
    
    if propulsion_types:
        filtered_df = filtered_df[filtered_df['type_of_propulsion'].isin(propulsion_types)]
    
    return filtered_df


def calculate_percentages(df, group_col, value_col='number'):
    """
    Calculate percentages for grouped data.
    
    Args:
        df (pd.DataFrame): Input dataframe
        group_col (str): Column to group by
        value_col (str): Column with values to calculate percentages for
        
    Returns:
        pd.DataFrame: Dataframe with percentages
    """
    total = df[value_col].sum()
    result = df.groupby(group_col)[value_col].sum().reset_index()
    result['percentage'] = (result[value_col] / total * 100).round(1) if total > 0 else 0
    return result


def calculate_sustainable_percentage(df):
    """
    Calculate the percentage of sustainable vehicles (Electric + Hybrid).
    
    Args:
        df (pd.DataFrame): Vehicle dataframe
        
    Returns:
        float: Sustainable vehicles percentage
    """
    total = df['number'].sum()
    if total == 0:
        return 0
    
    sustainable_df = df[df['type_of_propulsion'].isin(SUSTAINABLE_TYPES)]
    sustainable_total = sustainable_df['number'].sum()
    
    return (sustainable_total / total * 100)


def calculate_yoy_change(df, current_year, district=None, neighborhood=None):
    """
    Calculate year-over-year change in electric vehicle percentage.
    
    Args:
        df (pd.DataFrame): Vehicle dataframe
        current_year (int): Current year
        district (str): District filter
        neighborhood (str): Neighborhood filter
        
    Returns:
        tuple: (yoy_change, color)
    """
    min_year = df['year'].min()
    if current_year <= min_year:
        return 0, COLORS['subtext']
    
    # Current year data
    current_df = filter_dataframe(df, current_year, district, neighborhood)
    current_total = current_df['number'].sum()
    current_electric = current_df[current_df['type_of_propulsion'] == 'Electric']['number'].sum()
    current_percent = (current_electric / current_total * 100) if current_total > 0 else 0
    
    # Previous year data
    prev_year = current_year - 1
    prev_df = filter_dataframe(df, prev_year, district, neighborhood)
    prev_total = prev_df['number'].sum()
    prev_electric = prev_df[prev_df['type_of_propulsion'] == 'Electric']['number'].sum()
    prev_percent = (prev_electric / prev_total * 100) if prev_total > 0 else 0
    
    yoy_change = current_percent - prev_percent
    
    if yoy_change > 0:
        return yoy_change, COLORS['Hybrid']
    elif yoy_change < 0:
        return yoy_change, '#F87171'  # Light red
    else:
        return yoy_change, COLORS['subtext']


def format_number(number):
    """Format number with thousands separator."""
    return f"{number:,}"


def create_base_chart_layout(title, colors=COLORS):
    """
    Create base layout for charts.
    
    Args:
        title (str): Chart title
        colors (dict): Color scheme
        
    Returns:
        dict: Chart layout configuration
    """
    return {
        'title': {
            'text': title, 
            'font': {
                'size': 14, 
                'color': colors['text'], 
                'family': 'Inter, system-ui, sans-serif'
            }
        },
        'template': 'plotly_white',
        'margin': dict(l=20, r=20, t=40, b=20),
        'font': dict(
            family="Inter, system-ui, sans-serif", 
            size=11, 
            color=colors['text']
        ),
        'plot_bgcolor': colors['panel'],
        'paper_bgcolor': colors['panel']
    }