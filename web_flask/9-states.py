#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects present in DBStorage sorted by name."""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_sorted)

@app.route('/states/<id>', strict_slashes=False)
def states_detail(id):
    """Display a HTML page for a specific State object and its Cities."""
    state = storage.get(State, id)
    if state:
        # If using DBStorage, cities are already loaded through the relationship
        # If using FileStorage, use the public getter method cities
        cities_sorted = sorted(state.cities if storage_t == 'db' else state.cities(), key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities_sorted)
    else:
        return render_template('9-states.html', not_found=True)

@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
