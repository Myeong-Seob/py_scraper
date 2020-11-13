from flask import Flask, render_template, request, redirect, send_file

app = Flask("Jobs")


@app.route("/")
def index():
    return render_template("index.html")


app.run(host="0.0.0.0", port=7000, debug=True)
