"""
Constants and enums for the Barcelona Vehicle Dashboard.
"""

# Propulsion types
PROPULSION_TYPES = {
    'GASOLINE': 'Gasoline',
    'DIESEL': 'Diesel',
    'ELECTRIC': 'Electric',
    'HYBRID': 'Hybrid',
    'OTHERS': 'Others',
    'UNKNOWN': 'Unknown'
}

# Sustainable propulsion types
SUSTAINABLE_TYPES = [PROPULSION_TYPES['ELECTRIC'], PROPULSION_TYPES['HYBRID']]

# Chart types
CHART_TYPES = {
    'DISTRIBUTION': 'distribution',
    'TRENDS': 'trends',
    'TOP_NEIGHBORHOODS': 'top_neighborhoods'
}

# Default values
DEFAULTS = {
    'DISTRICT': 'Ciutat Vella',
    'NEIGHBORHOOD': 'Sant Pere, Santa Caterina i la Ribera',
    'TOP_N_NEIGHBORHOODS': 5
}