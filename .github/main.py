from flask import Flask, render_template, send_from_directory, request
from datetime import datetime
app = Flask(__name__)
#---- Pro správné fungování stránky ----

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

#----------- Úvod -----------


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
        {"title": "Jak začít s Pythonem", "date": "2025-03-31", "author": "kyle Crane"},
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

#-------- GET ----------------


@app.route("/", methods=['GET', 'POST'])
def home_page():
     string = None
     if request.method == 'POST':
       jmeno = request.form.get('jméno')
       prijmeni = request.form.get('příjmení')
       email = request.form.get('email')
       uzivatelske_jmeno = request.form.get('uživatelské_jméno')
       rodne_cislo = request.form.get('rodné_číslo')
 
       if not jmeno or not prijmeni or not email or not uzivatelske_jmeno or not rodne_cislo:
          string = "Musíte vyplnit všechna pole"
       else:
          if rodne_cislo.isdigit():
             if string is None:
                string = (
                 f"Zadali jste: {jmeno} {prijmeni}, E-mail: {email}, "
                 f"Uživatelské jméno: {uzivatelske_jmeno}, Rodné číslo: {rodne_cislo}."
             )
     return render_template("index.html", datum=datetime.now().strftime('%d.%m.%Y %H:%M:%S'), string=string)
        
        

if __name__ == "__main__":
    app.run(debug=True)



