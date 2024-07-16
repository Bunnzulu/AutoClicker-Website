from flask import Flask,render_template,request
from AutoClicker import Auto

app = Flask(__name__,template_folder= "Templates")


@app.route("/")
def Main_Page():
    return render_template("index.html")

@app.route("/Clicker",methods=["post"])
def Confirm_Page():
    data = request.form
    if Auto(int(data.get("Pause"))): return render_template("Confirm.html")


if __name__ == '__main__':
    app.run(debug=True)