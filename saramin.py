import requests
from bs4 import BeautifulSoup
import json
import os.path


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def get_jobs(word):
    URL = f"http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={word}"
    soup = requests.get(URL, headers=headers)
    saramin = BeautifulSoup(soup.text, "html.parser")
    content_id = saramin.find("div", {"id": "content"})
    content_class = content_id.find("div", {"class": "content"})
    content_box = content_class.find_all("div", {"class": "item_recruit"})
    jobs = []
    for item in content_box:
        item_value = item["value"]
        detail_URL = f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={item_value}&recommend_ids=eJxNj8kBAzEIA6vJH2EuvVPI9t9FSJw1%2BxyPBHhRospxpcUr3%2BuBl%2B2HNLcaf3D74oLg%2BC6zUi8PbFRExUGKISdMovuDwiU5o5IiMmi9fcI9maIHs9PoRbzPqAjOZFshD8ti%2BFiEq88XwVzZYf93M8DTpRZ%2B9u5CA9%2FwBz8VSMo%3D&view_type=search&searchword=python&searchType=search&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n#seq=0"
        h2 = item.find("h2", {"class": "job_tit"})
        title = h2.find("a")["title"]
        job_date = item.find("div", {"class": "job_date"})
        date = job_date.find("span").get_text()
        job_condition = item.find("div", {"class": "job_condition"})
        spans = job_condition.find_all("a")
        if len(spans) < 2:
            location = spans[0].get_text()
        else:
            first = spans[0].get_text()
            second = spans[1].get_text()
            location = first + " " + second
        strong = item.find("strong", {"class": "corp_name"})
        company = strong.find("a")["title"]
        detail = detail_URL

        job = {
            "FROM": "saramin(사람인)",
            "title": title,
            "date": date,
            "location": location,
            "company": company,
            "detail": detail,
        }
        jobs.append(job)
    return jobs


def get_saramin_jobs(word):
    saramin_jobs = get_jobs(word)
    return saramin_jobs