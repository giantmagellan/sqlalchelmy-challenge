# Flask API based on the queries previously developed
from flask import Flask, jsonify

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

# Engine to connect to sqlite database
engine = create_engine("sqlite:///c:/Users/User/Documents/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii weather API!"<br/>
    )"Hello friend. Welcome to the 'Home' page."

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data as json"""
    return jsonify(precipitation_df)

@app.route("/api/v1.0/stations")
def station():
    """Return json list of stations from the dataset"""


@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/<start>")

@app.route("/api/v1.0/<start>/<end>")

if __name__ == "__main__":
    app.run(debug=True)
