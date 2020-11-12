import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


URL = f"http://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit&Page_No=1"
soup = requests.get(URL, headers=headers)
jobkorea = BeautifulSoup(soup.text, "html.parser")
list_default = jobkorea.find("div", {"class": "list-default"})
items = list_default.find_all("li")
print(len(items))