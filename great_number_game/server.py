from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def checkGuess():
    session['randomValue'] = int(random.randint(0,3))
    session['guessNum'] = int(request.form['num'])

    if session['guessNum'] < session['randomValue']:
        return render_template('index.html', content=session['randomValue'], text="low" )
    elif session['guessNum'] > session['randomValue']:
        return render_template('index.html',content = session['randomValue'], text="high")
    else:
        return render_template('index.html', content = session['randomValue'], text="equal")
@app.route('/reset', methods=['POST'])
def reseting():
    return redirect('/')
app.run(debug=True)
