from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrering", methods=["GET", "POST"])
def registrering():

    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        kommentar = request.form["kommentar"]

        return render_template(
            "index.html",
            navn=navn,
            epost=epost,
            alder=alder,
            kommentar=kommentar
        )

    return render_template("registrering.html")

if __name__ == "__main__":
    app.run(debug=True)