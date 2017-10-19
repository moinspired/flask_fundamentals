from flask import Flask, render_template, request, redirect, session
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def test():
    session['count'] = 0
    return redirect('/')


@app.route('/reload', methods=['POST'])
def test2():
    session['count'] *= 2
    return redirect('/')

app.run(debug=True)
