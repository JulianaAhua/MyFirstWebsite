from flask import Flask 

app = Flask("__name__")

@app.route("/")
def home():
    return "<p> welcome to codeplateau homepage </p>"

@app.route("/about_us")
def about():
    return "<p> we are codeplateau, making a difference </p>"

@app.route("/contact")
def contact():
    return "<p> visit our digital platorms or call us on 080naija for life</p>"

@app.route("/products")
def products():
    return "<p> we sell everything code, we build apps, we hack</p>"

@app.route("/services")
def services():
    return "<p> we render remote and home services</p>"


