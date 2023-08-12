from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
# print(response.text)

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")

anchor_tags = soup.find_all(name="span", class_ = "titleline")
link_titles = [anchor_tag.a.getText() for anchor_tag in anchor_tags]
links = [anchor_tag.a.get("href") for anchor_tag in anchor_tags]

spans = soup.find_all(name="span", class_ = "score")
scores = [int(span.getText().split()[0]) for span in spans]

highest_number = max(scores)
index = scores.index(highest_number)
print(link_titles[index], links[index])
# print(scores)



