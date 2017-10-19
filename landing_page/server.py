from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninjas')
def ninja():
    return render_template("ninja.html")

@app.route('/dojos/new', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']
        name = request.form['name']
        return render_template('ninja.html', age= age, name=name)
    return render_template('dojos.html')
if __name__ == "__main__":
    app.run()
