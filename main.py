from flask import Flask, render_template
from replit import db

app = Flask('app')

db["posts"] = [{
  "title": "la recette de spaghettis",
  "content": "on commence par"
},{
  "title": "la recette de courgette",
  "content": "blabla"
},{
  "title": "la recette de spaghettis",
  "content": "on commence par"
}]
              
@app.route('/')
def index():
  return render_template("index.html")

  
@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/team')
def team():
  return render_template("team.html")
  
@app.route('/posts')
def posts():
  return render_template("posts.html", posts=db["posts"])
               
@app.route('/posts/<id>')
def show(id):
  return render_template("show.html", post=db["posts"][int(id)])
    
  
app.run(host='0.0.0.0', port=8080)