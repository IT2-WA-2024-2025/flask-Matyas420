from flask import Flask, render_template, send_from_directory
from datetime import datetime
app = Flask(__name__)
#---- Pro správné fungování stránky ----

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

#----------- Úvod -----------
@app.route("/kontakt")
def kontakt():
    return render_template('contact.html')

@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/category")
def category():
    return render_template('category.html')

#-------- První cvičení --------

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

#------- Article ----------

@app.route("/article")
def article():
    articles = [ 
        {"title": "Jak začít s Pythonem", "date": "2025-03-31", "author": "Jan Novák"},
        {"title": "Flask: Webový framework pro začátečníky", "date": "2025-03-30", "author": "Petr Svoboda"},
        {"title": "Datové struktury v Pythonu", "date": "2025-03-29", "author": "Eva Dvořáková"}
    ]
    
    return render_template('article.html', articles=articles)

#----------- Profile -----------

@app.route("/profile")
def profil():
    jmeno = "Matyáš Poledník"
    vek = 18
    return render_template("index.html", jmeno=jmeno, vek=vek)

#---------- Time -------------

@app.route('/')
def index():
    now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    return render_template('index.html', datum=now)

if __name__ == "__main__":
    app.run(debug=True)



