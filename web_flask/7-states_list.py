#!/usr/bin/python3
"""
starts a Flask web application module
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def hbnb_state_list():
    """
        fn for fetching data
        from the storage engine
    """
    states_list = storage.all(State)
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def hbnb_teardown_app():
    """
        close the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
