from flask import Flask, render_template

app = Flask(__name__)

#----------- Úvod -----------

clanky = [
    {"title": "" }
]

@app.route("/")
def Home_page():
    return  render_template('index.html', clanky=clanky)

@app.route("/kontakt")
def kontakt():
    return render_template('contact.html')

@app.route("/product")
def product():
    return "Toto bude stránka s produkty"

@app.route("/category")
def category():
    return "Toto bude stránka s kategoriemi"

#-------- První cvičení --------

@app.route("/about")
def about():
    return "Informace o stránce"

@app.route("/contact")
def contact():
    return "Toto bude stránka s kontakty"

#------- Article ----------
@app.route("/article")
def clanek():
    article = [
    {"Název": "Jak začít s Pythonem", "date": "2025-03-31", "author": "Jan Novák"},
    {"Název": "Flask: Webový framework pro začátečníky", "date": "2025-03-30", "author": "Petr Svoboda"},
    {"Název": "Datové struktury v Pythonu", "date": "2025-03-29", "author": "Eva Dvořáková"}]


    return render_template('article.html', article=article)

#----------- Profile -----------

@app.route("/profile")
def profil():
    jmeno = "Matyáš Poledník"
    vek = 18
    return render_template("index.html", jmeno=jmeno, vek=vek)

#--------- Výpis článků --------


if __name__ == "__main__":
    app.run(debug=True)



