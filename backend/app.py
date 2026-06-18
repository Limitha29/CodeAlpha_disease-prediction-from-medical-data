from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# LOAD MODELS
heart_model = joblib.load("heart_model.pkl")
diabetes_model = joblib.load("diabetes_model.pkl")
cancer_model = joblib.load("cancer_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        disease = data["disease"]
        features = np.array(data["features"], dtype=float).reshape(1, -1)

        # ================= HEART =================
        if disease == "heart":

            age = features[0][0]
            gender = features[0][1]
            chest_pain = features[0][2]
            bp = features[0][3]
            chol = features[0][4]
            hr = features[0][5]

            print("Disease:", disease)
            print("Features:", features)

            # Simple heart disease logic
            if (
                age > 55
                and bp > 140
                and chol > 240
                and hr < 120
            ):
                prediction = 0
            else:
                prediction = 1

            print("Prediction:", prediction)

            result = (
                "❤️ Heart Disease Detected"
                if prediction == 0
                else "✅ No Heart Disease"
            )

        # ================= DIABETES =================
        elif disease == "diabetes":

            prediction = diabetes_model.predict(features)[0]

            print("Disease:", disease)
            print("Features:", features)
            print("Prediction:", prediction)

            result = (
                "🩸 Diabetic"
                if prediction == 1
                else "✅ Not Diabetic"
            )

        # ================= CANCER =================
        else:

            prediction = cancer_model.predict(features)[0]

            print("Disease:", disease)
            print("Features:", features)
            print("Prediction:", prediction)

            result = (
                "🎗️ Cancer Detected"
                if prediction == 0
                else "✅ No Cancer"
            )

        return jsonify({"result": result})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"result": f"Error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)