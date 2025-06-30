from flask import Flask, render_template, request

app = Flask(__name__)

# Simple dummy model: just does some math on the inputs
def dummy_model_predict(features):
    return int(sum(features) % 500)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [
            1 if request.form['holiday'] == "Holiday" else 0,
            float(request.form['temp']),
            float(request.form['rain']),
            float(request.form['snow']),
            1 if request.form['weather'] == "Clear" else 0,
            int(request.form['year']),
            int(request.form['month']),
            int(request.form['day']),
            int(request.form['hours']),
            int(request.form['minutes']),
            int(request.form['seconds']),
        ]
        prediction = dummy_model_predict(inputs)
        return render_template('index.html', result=prediction)
    except Exception as e:
        return render_template('index.html', result="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
