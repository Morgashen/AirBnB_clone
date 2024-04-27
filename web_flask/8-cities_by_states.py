#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State objects and their cities present in DBStorage sorted by name."""
    states = storage.all(State).values()
    # Sort states by name
    states_sorted = sorted(states, key=lambda state: state.name)
    # Load cities for each state
    for state in states_sorted:
        # If using DBStorage, cities are already loaded through the relationship
        # If using FileStorage, use the public getter method cities
        state.cities = sorted(state.cities if storage_t == 'db' else state.cities(), key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states_sorted)

@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
