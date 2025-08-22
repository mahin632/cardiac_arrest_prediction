# Import libraries
import re
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the models from pickle files
all_models = pickle.load(open("models.pkl", "rb"))


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

        # Prepare the input data for the model
        input_data = np.array(
            [[age, blood_pressure, cholesterol, exercise, pain, heart_rate]]
        )

        # Perform prediction using the first model in the list
        prediction = all_models[0].predict(input_data)

        return jsonify(
            {"name": name, "email": email, "prediction": prediction.tolist()}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
