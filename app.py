from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def log():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html', title='Home')
def index():
    return redirect(url_for('index'))
@app.route('/index')
def index():
    return render_template('index.html', title='Test')
if __name__ == '__main__':
    app.run(debug=True)

