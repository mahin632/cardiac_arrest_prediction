# 🫀 Cardiac Arrest Prediction
A machine learning-powered Flask web application that predicts the likelihood of cardiac arrest based on clinical and environmental factors.
This project combines data science, healthcare, and weather analytics to provide early warnings that may help in life-saving decision-making.

# 🚀 Features
1. Data-driven predictions using trained ML models (scikit-learn).

2. Weather integration — leverages daily weather data for risk assessment.

3. Flask web interface with user-friendly input forms.

4. Pre-trained model (models.pkl) for instant predictions.

5. Custom UI with templates/ and static/ resources.

# 📂 Project Structure
Cardiac_arrest_prediction-main/
│── app.py                # Flask web app entry point
│── hmm.py                # ML/Prediction-related code
│── models.pkl            # Pre-trained ML model
│── dataset.csv           # Cardiac dataset
│── daily_weather.csv     # Weather dataset
│── requirements.txt      # Python dependencies
│── templates/            # HTML templates (frontend)
│── static/               # CSS, JS, images
│── docs/ & reports       # PDFs, DOCX project reports

# ⚙️ Installation & Setup
1. Clone the repository
```bash
git clone https://github.com/mahin632/Cardiac_arrest_prediction.git
cd Cardiac_arrest_prediction-main
```
2. Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the Flask app
```bash
python app.py
```
Then open your browser at http://127.0.0.1:5000/ 

# 📊 Model & Data
Machine Learning: Uses scikit-learn models for classification.
Datasets:
dataset.csv → Patient health/clinical records.

# 🛠️ Tech Stack
- Frontend: HTML, CSS (Flask templates)

- Backend: Python, Flask

- ML/AI: Scikit-learn, NumPy

- Deployment: Localhost (extendable to cloud)

