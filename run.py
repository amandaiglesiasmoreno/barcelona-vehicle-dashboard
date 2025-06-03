"""
Main entry point for the Barcelona Vehicle Propulsion Dashboard.
"""
from src.app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)