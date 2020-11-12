import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def get_jobs(word):
    URL = f"http://www.jobkorea.co.kr/Search/?stext={word}"
    jobs = []
    soup = requests.get(URL, headers=headers)
    jobkorea = BeautifulSoup(soup.text, "html.parser")
    list_default = jobkorea.find("div", {"class": "list-default"})
    items = list_default.find_all("li")
    for item in items:
        title = item.find("a", {"class": "title"}).get_text(strip=True)
        date = item.find("span", {"class": "date"}).get_text(strip=True)
        location = item.find("span", {"class": "loc long"}).get_text(strip=True)
        company = item.find("a", {"class": "dev_view"})["title"]
        value = item["data-gno"]
        detail_URL = (
            f"http://www.jobkorea.co.kr/Recruit/GI_Read/{value}?Oem_Code=C1&logpath=1"
        )
        job = {
            "FROM": "jobKorea(잡코리아)",
            "title": title,
            "date": date,
            "location": location,
            "company": company,
            "detail": detail_URL,
        }
        jobs.append(job)
    return jobs


def get_jobKorea_jobs(word):
    jobKorea = get_jobs(word)
    return jobKorea
