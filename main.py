from saramin import get_saramin_jobs
from jobKorea import get_jobKorea_jobs
import json


def sum_jobs(word):
    print(f"Finding {word} Jobs.. ")
    saramin = {f"{word}": get_saramin_jobs(word)}
    jobKorea = {f"{word}": get_jobKorea_jobs(word)}
    ask = ask_user()
    if ask == 1:
        print(saramin)
        print(jobKorea)
    elif ask == 2:
        saramin_path = f"saramin.json"
        with open(saramin_path, "w") as file:
            file.write(json.dumps(saramin, ensure_ascii=False, indent=4))

        jobKorea_path = f"jobKorea.json"
        with open(jobKorea_path, "w") as file:
            file.write(json.dumps(jobKorea, ensure_ascii=False, indent=4))
        print("Done :)")


def ask_user():
    while True:
        print("Search is Done")
        print("Want see results in console or json(save file)??")
        try:
            ask = int(
                input(
                    """
#console: 1
#json: 2
#exit: 3
        """
                )
            )
        except:
            print("Please answer 1 or 2 or 3")
        else:
            if ask == 1:
                return 1
            elif ask == 2:
                return 2
            else:
                print("Good Bye")
                break


def search_job():
    ask = str(
        input(
            """
        What do you looking for?
        => """
        )
    )
    if ask == "":
        print("Please insert the word")
    else:
        sum_jobs(ask)


search_job()
