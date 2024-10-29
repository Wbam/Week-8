from flask import Flask, request, jsonify
import joblib
import logging

# Initialize Flask application
app = Flask(__name__)

# Load models
models = {
    'random_forest': joblib.load('notebooks/trained_model_Random Forest.joblib'),
    'mlp': joblib.load('notebooks/trained_model_Multi-Layer Perceptron.joblib'),
    'logistic_regression': joblib.load('notebooks/trained_model_Logistic Regression.joblib'),
    'gradient_boosting': joblib.load('notebooks/trained_model_Gradient Boosting.joblib'),
    'decision_tree': joblib.load('notebooks/trained_model_Decision Tree.joblib')
}

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.path} {request.json}")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    model_choice = data.get('model', 'random_forest')  

    if model_choice not in models:
        app.logger.error(f"Model '{model_choice}' not found.")
        return jsonify({'error': f"Model '{model_choice}' not found."}), 400

    model = models[model_choice]
    features = data['features']

    try:
        prediction = model.predict([features])
        app.logger.info(f"Prediction: {prediction}")
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
