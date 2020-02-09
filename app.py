# Flask API based on the queries previously developed
from flask import Flask, jsonify

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Engine to connect to sqlite database
engine = create_engine("sqlite:///c:/Users/User/Documents/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """List of all API routes."""
    return (
        f"Welcome to the Hawaii weather API!"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
     # session (link) from python to the database
    session = Session(query)

    """Return the precipitation data as json"""
    past_yr = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date > '2016-08-23').\
            order_by(Measurement.date).all()
    session.close()

    # Convert to dataframe
    hawaii_weather = pd.DataFrame(past_yr, columns=['date', 'prcp'])
    # hawaii_weather.rename(columns={'date':'Date', 'prcp':'Precipitation',   inplace=True)
    return jsonify(hawaii_weather)

@app.route("/api/v1.0/stations")
def station():
    # session from python to database
    session = Session(query)

    """Return json list of stations from the dataset"""
    active_stations = session.query(Measurement.station, 
        func.count(Measurement.tobs)).group_by(Measurement.station).all()
    session.close()

    # Convert list of tuples into normal list
    station_list = list(np.ravel(results))

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def observations():
    # session from python to database
    session = Session(query)

    """Query for the dates and temperature observations from a year ago     as json list"""
    past_yr_obs = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date > '2016-08-23').\
            order_by(Measurement.tobs.desc()).all()
    session.close()

    hawaii_tobs = pd.DataFrame(past_yr_obs, columns=['date', 'tobs'])
    # hawaii_tobs.rename(columns={'date':'Date', 'tobs':'Temp.    Observations'},inplace=True)

    return jsonify(hawaii_tobs)

@app.route("/api/v1.0/<start>")
def start_date(start=none):
    session = Session(query)
    """Return json list of max, min, and avg temperature for given start range"""

    # Select statement
    sel = [func.max(Measurement.tobs), func.min(Measurement.tobs, func.avg(Measurement.tobs)]

    stats = session.query(*sel).filter(Measurement.date > start)).all()

    session.close()

    # returns flattened 1D array of temperature statistics
    temps = list(np.ravel(stats))
    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def end_date(end=none):
    # session from python to database
    session = Session(query)

    """Return json list of max, min, and avg temperature for given start or start-end range"""
    station_stats = session.query(Measurement.station, func.max     (Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)).group_by(Measurement.station).all()

    # Select statement
    sel = [func.max(Measurement.tobs), func.min(Measurement.tobs, func.avg(Measurement.tobs)]

    stats = session.query(*sel).filter(Measurement.date > start)).filter(Measurement.date < end).all()

    session.close()

    # returns flattened 1D array of temperature statistics
    temps = list(np.ravel(stats))
    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)