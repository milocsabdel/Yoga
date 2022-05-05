from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

  
@app.route('/contact')
def contact():
  return"Page contact"
  
app.run(host='0.0.0.0', port=8080)