from pathlib import Path
import pickle

import numpy as np
from flask import Flask, jsonify, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "model_file.p"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}. "
        "Make sure FlaskAPI/models/model_file.p exists."
    )

app = Flask(__name__)


def load_model():
    """Load the serialized salary model."""
    with MODEL_PATH.open("rb") as pickled:
        data = pickle.load(pickled)
    return data["model"]


MODEL = load_model()


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}

    if "input" not in payload:
        return jsonify({"error": "Request body must contain an 'input' field."}), 400

    try:
        features = np.asarray(payload["input"], dtype=float).reshape(1, -1)
    except (TypeError, ValueError):
        return jsonify({"error": "'input' must contain numeric feature values."}), 400

    try:
        prediction = MODEL.predict(features)[0]
    except Exception as exc:
        return jsonify({"error": f"Prediction failed: {exc}"}), 500

    return jsonify({"response": float(prediction)}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
