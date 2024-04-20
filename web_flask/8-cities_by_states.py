#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
# Assuming 'models' is a module containing 'storage', 'State', and 'City' classes
from models import storage, State, City
app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    # Assuming 'storage.all' method returns a dictionary of 'State' objects
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    for state in states:
        # Assuming each 'State' object has a 'cities' attribute which is a list of 'City' objects
        state.cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
