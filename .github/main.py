from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home_page():
    return "Zde bude úvodní stránka pro náš blog"

@app.route("/kontakt")
def kontakt():
    return "Toto bude stránka s kontakty"

@app.route("/titulni-stranka")
def stranka():
    return "Toto bude titulní stránka"

@app.route("/product/<id>")
def product(id:int):
    return "Toto bude stránka s produkty"

@app.route("/category/<jmeno>")
def category(jmeno):
    return f"Toto bude stránka s kategoriemi {jmeno}"

@app.route("/")
def uzivatel(jmeno):
    return f"Profil uživatele: {jmeno}"

if __name__=="__main__":
    app.run(debug=True)

