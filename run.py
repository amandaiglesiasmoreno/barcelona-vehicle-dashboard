"""
Main entry point for the Barcelona Vehicle Propulsion Dashboard.
"""
from src.app import create_app

app = create_app()
server = app.server

if __name__ == '__main__':
    app.run(debug=True)