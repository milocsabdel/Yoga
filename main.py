from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")
  
@app.route('/nos-prix')
def nos_prix():
  return render_template("nos-prix.html")

@app.route('/notre-equipe')
def notre_equipe():
  return render_template("notre-equipe.html")

@app.route('/la-section-des-enfants')
def la_section_des_enfants():
  return render_template("la-section-des-enfants.html")


app.run(host='0.0.0.0', port=81)


