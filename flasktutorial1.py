from flask import Flask, render_template, request

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

@app.route('/anarchademics/')
def anarchademics():
    return render_template("anarchademics.html")

@app.route('/chimes/')
def chimes():
    return render_template("chimes.html")

@app.route('/darkGourds/')
def darkGourds():
    return render_template("darkGourds.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
       factor1=request.form["factor1"]
       factor2=request.form["factor2"]
       theSum = int(factor1)*int(factor2)
       print(factor1, factor2)
       return render_template("chimes.html", theSum= theSum)

@app.route("/decInches", methods=['POST'])
def decInches ():
    if request.method=='POST':
        f = request.form["intLength"]
        s = request.form["fraxLength"]

        #total length decimal inches
        d = float(int(f) + int(s)/16)
        #nodes in decimal inches
        n = d * 0.224
        #nodes integer portion
        i = int(n)
        #converting decimal portion to sixteenths of inches
        r = round((n - i) * 16, 1)

        message = "The nodes are located at " + str(i) + " and " + str(r) + " sixteenths of an inch from each end."
        return render_template("chimes.html", message = message)

if __name__ == "__main__":
    app.run(debug=True)
