from flask import Flask, render_template, request
import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'payments.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/predict")
def predict_form():
    return render_template('predict.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/pred", methods=['POST','GET'])
def predict():
    try:
        x = [[x for x in request.form.values()]]
        print(x)
        x = np.array(x)
        print(x)
        pred = model.predict(x)
        print(pred[0])
        return render_template('submit.html', prediction_text=str(pred))

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=False)