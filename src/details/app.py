from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return f'<H1>Hello world</H1>'


app.run(host='0.0.0.0', port=8000, debug=True)