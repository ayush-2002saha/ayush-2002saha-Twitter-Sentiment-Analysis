from flask import Flask, request, jsonify, render_template
import joblib  # Or use any other library for model loading (e.g., torch, tensorflow)
import os

app = Flask(__name__)

# Load models for positive and negative sentiment
model_pos_path = "models/model_pos"
model_neg_path = "models/model_neg"

# Example function to load models (adjust this as per your model format)
def load_model(model_path):
    # Placeholder for model loading
    # Replace with actual model loading logic, e.g., joblib, torch.load(), etc.
    return "your_model_object"

model_pos = load_model(model_pos_path)
model_neg = load_model(model_neg_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    tweet = data.get('tweet')

    # Add your sentiment prediction logic here
    sentiment = "positive" if "happy" in tweet.lower() else "negative"

    return jsonify({
        "tweet": tweet,
        "sentiment": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)