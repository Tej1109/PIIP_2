from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)




@app.route('/')
def Home():
    return render_template("webpage.html")


@app.route('/predict',methods=['POST'])
def predict():
    print("H")
    features=[x for x in request.form.values()]
    print(features)
    for i in range(len(features)):
        if features[i] == "on":
            features[i] = 1
    if len(features) == 9:
        features.append("0")
    model = pickle.load(open(f'RegModel {features[0]}.sav','rb'))
    int_features = [float(j) for j in features[1:]]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output= prediction

    if output:
        return render_template('webpage.html',prediction_text = f"The number of {features[0]} is {int(output)}")

if __name__ == '__main__':
    app.run(debug = 'True')