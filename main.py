from flask import Flask, render_template
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
  post = {
    "title": "La recette des spaghettis",
    "content": "On commence par ...",
  }
  return render_template("posts.html", post=post)
    
  
app.run(host='0.0.0.0', port=8080)