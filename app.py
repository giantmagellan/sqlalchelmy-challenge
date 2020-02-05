# Flask API based on the queries previously developed
from flask import Flask, jsonify

app = Flask(__name__)

precipitation_df = pd.Dataframe({
    hawaii_dropna["Date"]:hawaii_dropna["Precipitation"]})

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
