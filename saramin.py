import requests
from bs4 import BeautifulSoup

URL = "http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=python"

soup = requests.get(URL)
saramin = BeautifulSoup(soup.text, "html.parser")
content_id = saramin.find("div", {"id": "content"})
content_class = content_id.find_all("div", {"class": "content"})
for content in content_class:
    item_recruit = content.find("div", {"class": "item_recruit"})
    print(item_recruit)
