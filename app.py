from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def log():
    return redirect(url_for('index'))

def index():
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)

