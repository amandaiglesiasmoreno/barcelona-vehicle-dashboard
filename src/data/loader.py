"""
Data loading utilities for the Barcelona Vehicle Dashboard.
"""
import pandas as pd
from config.settings import CSV_FILE


def load_data():
    """
    Load and preprocess the vehicle data.
    
    Returns:
        pd.DataFrame: Loaded and preprocessed vehicle data
    """
    try:
        df = pd.read_csv(CSV_FILE)
        
        # Basic data validation
        required_columns = ['year', 'district', 'neighborhood', 'type_of_propulsion', 'number']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        # Data type conversions
        df['year'] = df['year'].astype(int)
        df['number'] = pd.to_numeric(df['number'], errors='coerce').fillna(0)
        
        # Remove rows with zero vehicles
        df = df[df['number'] > 0]
        
        return df
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {CSV_FILE}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


def get_years(df):
    """Get sorted list of unique years."""
    return sorted(df['year'].unique())


def get_districts(df):
    """Get sorted list of unique districts."""
    return sorted(df['district'].unique())


def get_neighborhoods(df, district=None):
    """Get sorted list of neighborhoods, optionally filtered by district."""
    if district:
        return sorted(df[df['district'] == district]['neighborhood'].unique())
    return sorted(df['neighborhood'].unique())


def get_propulsion_types(df):
    """Get sorted list of unique propulsion types."""
    return sorted(df['type_of_propulsion'].unique())