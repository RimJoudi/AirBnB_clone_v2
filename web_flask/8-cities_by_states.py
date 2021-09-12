#!/usr/bin/python3
"""
starts a Flask web application module
"""
from flask import Flask, render_template
from models import storage
from models.state import State



app = Flask(__name__)


@app.teardown_appcontext
def hbnb_teardown_app(self):
    """
        close the current SQLAlchemy Session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def hbnb_cities_by_states():
    """
        fn for fetching data
        from the storage engine
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
