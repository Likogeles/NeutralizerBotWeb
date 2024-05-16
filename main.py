from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def hello_world():
    return 'NeutralizerBotWeb'


@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')


@app.route('/room_preferences')
def room_preferences():
    return render_template('room_preferences.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8010, debug=True)
