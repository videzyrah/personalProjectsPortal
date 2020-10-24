from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/diy/')
def diy():
    return render_template("diy.html")

@app.route('/basslines/')
def basslines():
    return render_template("basslines.html")

@app.route('/ppp/')
def ppp():
    return render_template("ppp.html")

@app.route('/darkGourds/')
def ppp():
    return render_template("DarkGourds.html")

if __name__ == "__main__":
    app.run(debug=True)
