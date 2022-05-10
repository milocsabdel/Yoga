from flask import Flask, render_template, request
from replit import db

app = Flask('app')

  
              
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


@app.route('/post/new')
def post_new():
  return render_template("post_new.html")


@app.route('/post/create', methods=['POST'])
def create():
  db['posts'].append({
   'titre': request.form["title"],
   'content':request.form["content"]
 })
  return render_template("index.html")
               
@app.route('/posts/<id>')
def show(id):
  return render_template("show.html", post=db["posts"][int(id)])

@app.route('/eleve')
def eleve():
  return render_template("eleves.html", posts=db["eleve"])
               
@app.route('/eleve/<id>')
def showeleves(id):
  return render_template("showeleves.html", eleve=db["eleves"][int(id)])


  
app.run(host='0.0.0.0', port=8080)