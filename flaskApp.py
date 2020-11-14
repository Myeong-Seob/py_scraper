from flask import Flask, render_template, request, redirect, send_file
from saramin import get_saramin_jobs
from jobKorea import get_jobKorea_jobs
from export import save_csv, save_json


def get_jobs(word):
    saramin = get_saramin_jobs(word)
    jobKorea = get_jobKorea_jobs(word)
    jobs = saramin + jobKorea
    return jobs


app = Flask("Jobs")
db = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/detail")
def detail():
    word = request.args.get("word")
    if word:
        existingWord = db.get(word)
        if existingWord:
            jobs = existingWord
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("detail.html", word=word, jobs=jobs, numJobs=len(jobs))


@app.route("/exportcsv")
def export_csv():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_csv(jobs)
        return "Done :)"
    except:
        return redirect("/")


@app.route("/exportjson")
def export_json():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_json(jobs)
        return "Done :)"
    except:
        return redirect("/")


app.run(host="0.0.0.0", port=7000, debug=True)
