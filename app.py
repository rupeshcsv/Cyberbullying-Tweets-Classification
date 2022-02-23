from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

file1 = open('models/model_lr.pkl', 'rb')
model1 = pickle.load(file1)
file1.close()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    text = 'error'
    if request.method == 'POST':
        text = request.form['text']
    prediction = model1.predict([text])[0]
    return render_template('home.html', result_text=f'{prediction}')


if __name__ == '__main__':
    app.run()
