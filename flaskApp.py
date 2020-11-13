from flask import Flask, render_template, request, redirect, send_file
from saramin import get_saramin_jobs
from jobKorea import get_jobKorea_jobs


app = Flask("Jobs")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/detail")
def detail():
    word = request.args.get("word")
    return render_template("detail.html", word=word)


app.run(host="0.0.0.0", port=7000, debug=True)
