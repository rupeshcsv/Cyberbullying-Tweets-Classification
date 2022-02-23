from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        text = request.form['text']
    return render_template('home.html', result_text=f'{text}')


if __name__ == '__main__':
    app.run()
