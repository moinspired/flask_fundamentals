from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('complete.html')

@app.route('/ninja/<name>')
    def Aninja(name):
        if name == 'blue':
            return render_template('leonardo.html')
    elif name == 'red':
            return render_template('raphael.html')
    elif name == 'orange':
            return render_template('michelangelo.html')
    else:
        return render_template('donatello.html')

if __name__ == "__main__":
    app.run(debug=True)
