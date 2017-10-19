from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flesh

app = Flask(__name__)


bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
    ))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark '{}'".format(url) )
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
