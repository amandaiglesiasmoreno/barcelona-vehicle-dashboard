# Barcelona Vehicle Propulsion Dashboard

A modern, interactive dashboard for analyzing vehicle propulsion trends in Barcelona. Built with Dash and Plotly, featuring a clean, minimalist design with comprehensive filtering and visualization capabilities.

## Features

- **Interactive Filtering**: Filter data by year, district, neighborhood, and propulsion type
- **Key Performance Indicators**: Track total vehicles, electric/hybrid adoption rates, and year-over-year changes
- **Multiple Visualizations**:
  - Distribution charts (bar/stacked bar)
  - Trend analysis (line charts)
  - Top neighborhoods by electric adoption
- **Responsive Design**: Clean, modern interface optimized for desktop viewing
- **Real-time Updates**: All charts and KPIs update dynamically based on filter selections

## Project Structure

```
barcelona-vehicle-dashboard/
├── README.md
├── requirements.txt
├── run.py                    # Application entry point
├── config/
│   ├── __init__.py
│   └── settings.py          # Configuration and constants
├── src/
│   ├── __init__.py
│   ├── app.py              # Main application factory
│   ├── data/
│   │   ├── __init__.py
│   │   └── loader.py       # Data loading utilities
│   ├── components/
│   │   ├── __init__.py
│   │   ├── filters.py      # Filter components
│   │   ├── kpis.py         # KPI components
│   │   └── charts.py       # Chart containers
│   ├── callbacks/
│   │   ├── __init__.py
│   │   └── main_callbacks.py # Dashboard interactivity
│   ├── layouts/
│   │   ├── __init__.py
│   │   └── main_layout.py  # Page layouts
│   └── utils/
│       ├── __init__.py
│       ├── constants.py    # Application constants
│       └── helpers.py      # Utility functions
├── assets/
│   └── styles.css          # Custom CSS (optional)
├── data/
│   └── vehicles_by_area_and_type.csv
└── tests/
    ├── __init__.py
    ├── test_data_loader.py
    ├── test_callbacks.py
    └── test_components.py
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/barcelona-vehicle-dashboard.git
   cd barcelona-vehicle-dashboard
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your data**:
   - Place your `vehicles_by_area_and_type.csv` file in the `data/` directory
   - Ensure the CSV has the required columns: `year`, `district`, `neighborhood`, `type_of_propulsion`, `number`

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Open your browser** and navigate to `http://localhost:8050`

## Data Format

The application expects a CSV file with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `year` | Integer | Year of the data |
| `district` | String | Barcelona district name |
| `neighborhood` | String | Neighborhood within the district |
| `type_of_propulsion` | String | Vehicle propulsion type (Gasoline, Diesel, Electric, Hybrid, Others, Unknown) |
| `number` | Integer | Number of vehicles |

## Configuration

The application can be configured through environment variables:

- `DEBUG`: Enable/disable debug mode (default: `True`)
- `HOST`: Host address (default: `0.0.0.0`)
- `PORT`: Port number (default: `8050`)

Example:
```bash
export DEBUG=False
export PORT=8080
python run.py
```

## Development

### Architecture

The application follows a modular architecture:

- **Config**: Centralized configuration and constants
- **Data Layer**: Data loading and preprocessing
- **Components**: Reusable UI components
- **Layouts**: Page structure and composition
- **Callbacks**: Interactive behavior and data updates
- **Utils**: Helper functions and utilities

### Adding New Features

1. **New Filters**: Add components in `src/components/filters.py`
2. **New Charts**: Create chart functions in `src/callbacks/main_callbacks.py`
3. **New KPIs**: Add KPI components in `src/components/kpis.py`
4. **Styling**: Modify colors and styles in `config/settings.py`

### Testing

Run tests using pytest:
```bash
pip install pytest
pytest tests/
```

## Deployment

### Using Gunicorn

For production deployment:

```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 --workers 4 run:app.server
```

### Using Docker

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8050

CMD ["python", "run.py"]
```

### Environment Variables for Production

```bash
export DEBUG=False
export HOST=0.0.0.0
export PORT=8050
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/)
- Designed with modern web standards and accessibility in mind
- Color scheme inspired by contemporary dashboard design trends