from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

file1 = open('models/model_lr.pkl', 'rb')
model1 = pickle.load(file1)
file1.close()

predictions = {'age': 'Age-based cyber-bullying',
               'gender': 'Gender-based cyber-bullying',
               'not_cyberbullying': 'No cyber-bullying',
               'other_cyberbullying': 'General cyber-bullying',
               'religion': 'Religion-based cyber-bullying',
               'ethnicity': 'Ethnicity-based cyber-bullying'}


@app.route('/', methods=['GET', 'POST'])
def home():
    text = 'error'
    if request.method == 'POST':
        text = request.form['text']
        prediction = model1.predict([text])[0]
        return render_template('home.html', result_text=f'{predictions[prediction]}')
    else:
        return render_template('home.html', result_text='Result appears here')


# @app.route('/', methods=['GET', 'POST'])
# def result():
#     text = 'error'
#     if request.method == 'POST':
#         text = request.form['text']
#     prediction = model1.predict([text])[0]
#     return render_template('home.html', result_text=f'{predictions[prediction]}')


if __name__ == '__main__':
    app.run()
