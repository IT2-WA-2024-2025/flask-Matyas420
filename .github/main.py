from flask import Flask, render_template

app = Flask(__name__)

#----------- Úvod -----------

@app.route("/")
def Home_page():
    return  render_template('index.html')

@app.route("/kontakt")
def kontakt():
    return render_template('contact.html')

@app.route("/product/<id>")
def product(id:int):
    return f"Toto bude stránka s produkty {id}"

@app.route("/category/<jmeno>")
def category(jmeno):
    return f"Toto bude stránka s kategoriemi {jmeno}"

#-------- První cvičení --------

@app.route("/about")
def about():
    return "Informace o stránce"

@app.route("/contact")
def contact():
    return "Toto bude stránka s kontakty"

@app.route("/article")
def article():
    return "Zobrazí obsah stránku"

@app.route("/article/<id>")
def arctile(id):
    return f"Zobrazí přesné informace o uživateli {id}"

if __name__ == "__main__":
    app.run(debug=True)



