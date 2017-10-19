from flask import Flask, render_template, request, redirect,session
import random

app = Flask(__name__)
app.secret_key = 'TrhisIsSecret'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def create_user():
    if not 'GOLD' in session:
        if 'farm' in request.form:
            session['GOLD'] = random.randint(10,20)
            session['place'] = 'farm'
            return redirect('/')
        if 'cave' in request.form:
            session['GOLD'] = random.randint(5,10)
            session['place'] = 'cave'
            return redirect('/')
        if 'house' in request.form:
            session['GOLD'] = random.randint(2,5)
            session['place'] = 'house'
            return redirect('/')
        if 'casino' in request.form:
            chance = random.randint(0,2)
            if chance == 0:
                session['GOLD'] += random.randint(0,50)
            else:
                session['GOLD'] -= random.randint(0,50)
            session['place'] = 'casino'
            return redirect('/')

    else:
        if 'farm' in request.form:
            session['GOLD'] += random.randint(10,20)
            session['place'] = 'farm'
            return redirect('/')
        if 'cave' in request.form:
            session['GOLD'] += random.randint(5,10)
            session['place'] = 'cave'
            return redirect('/')
        if 'house' in request.form:
            session['GOLD'] += random.randint(2,5)
            session['place'] = 'house'
            return redirect('/')
        if 'casino' in request.form:
            chance = random.randint(0,2)
            if chance == 0:
                session['GOLD'] += random.randint(0,50)
            else:
                session['GOLD'] -= random.randint(0,50)
            session['place'] = 'casino'
            return redirect('/')


app.run(debug=True)
