from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def info():
    name = request.form['name']
    location = request.form['location']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, comment=comment)

if __name__ == "__main__":
    app.run()
