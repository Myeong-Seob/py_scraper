import csv
import json


def save_csv(jobs):
    file = open(f"jobs.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["From", "Title", "Company", "Location", "Date", "Link"])
    for job in jobs:
        writer.writerow(job.values())
    return


def save_json(jobs):
    with open("jobs.json", "w") as file:
        file.write(json.dumps(jobs, ensure_ascii=False, indent=4))
    return
