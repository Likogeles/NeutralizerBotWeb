from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/reports/<path:path>')
def send_report(path):
    return send_from_directory('reports', path)


if __name__ == '__main__':
    app.run(port=4050, debug=True)
