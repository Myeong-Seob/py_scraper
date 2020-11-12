import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}
URL = "http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=python"

soup = requests.get(URL, headers=headers)
saramin = BeautifulSoup(soup.text, "html.parser")
content_id = saramin.find("div", {"id": "content"})
content_class = content_id.find("div", {"class": "content"})
content_box = content_class.find_all("div", {"class": "item_recruit"})
for item in content_box:
    h2 = item.find("h2", {"class": "job_tit"})
    title = h2.find("a")["title"]
    job_date = item.find("div", {"class": "job_date"})
    date = job_date.find("span").get_text()
    job_condition = item.find("div", {"class": "job_condition"})
    spans = job_condition.find_all("a")
    first = spans[0].get_text()
    second = spans[1].get_text()
    location = first + " " + second
    print(location)
