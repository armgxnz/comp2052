from flask import Flask, render_template

app = Flask(__name__)

misLenguajes = ("PHP", "Python", "Java", "C#",
                 "C++", "JavaScript", "Ruby", "Rust")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html', lenguajes = misLenguajes)

if (__name__) == "__main__":
    app.run(debug=True)