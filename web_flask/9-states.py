#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
# Assuming 'models' is a module containing 'storage', 'State', and 'City' classes
from models import storage, State, City
app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_route(state_id=None):
    """display the states and cities listed in alphabetical order"""
    # Assuming 'storage.all' method returns a dictionary of 'State' objects
    all_states = storage.all(State)
    states_sorted = sorted(all_states.values(), key=lambda x: x.name)
    state_selected = None
    cities_sorted = []
    if state_id:
        # Assuming 'storage.get' method to retrieve a 'State' object by its ID
        state_selected = storage.get(State, 'State.' + state_id)
        if state_selected:
            # Sort cities of the state in alphabetical order
            cities_sorted = sorted(state_selected.cities, key=lambda x: x.name)
    return render_template('9-states.html', states=states_sorted, state=state_selected, cities=cities_sorted)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
