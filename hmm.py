# Import libraries
import re
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import random

# Initialize the Flask app
app = Flask(__name__)

# Load the models from pickle files
with open("models.pkl", "rb") as model_file:
    all_models = pickle.load(model_file)


# Home page route
@app.route("/", methods=["GET", "POST"])
def hello():
    return render_template("index.html")


# About Us page route
@app.route("/aboutUs", methods=["GET"])
def aboutUs():
    return render_template("aboutUs.html")


# API for prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extracting form data
        data = request.get_json()
        name = data["name"]
        email = data["email"]
        gender = data["gender"]
        age = float(data["age"])
        blood_pressure = float(data["bloodPressure"])
        cholesterol = float(data["cholesterol"])
        exercise = float(data["exercise"])
        pain = float(data["pain"])
        heart_rate = float(data["heartRate"])

        # Randomly choose a prediction result
        prediction = random.choice(["You will live", "You will die"])

        # Redirect to the result page with the prediction result
        return redirect(url_for("result", name=name, email=email, result=prediction))
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Result page route
@app.route("/result", methods=["GET"])
def result():
    name = request.args.get("name")
    email = request.args.get("email")
    result = request.args.get("result")
    return render_template("result.html", name=name, email=email, result=result)


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
