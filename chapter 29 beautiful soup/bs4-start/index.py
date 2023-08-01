from bs4 import BeautifulSoup
import lxml

with open("website1.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# these methods below will only give info from the first element form many same element 

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)
print(soup.a)

print(soup) # printing entire html content
print(soup.prettify()) # printing entire html with correct indentation


# here is how you can access all of your dsire elements not just the first one

all_anchor_tags = soup.find_all(name="a") # this will give you a list of all of your a tags

for tag in all_anchor_tags:
    print(tag, tag.getText(), tag.get("href"))
    # tag.getText() is for the tag text, tag.get("href") for any kind of attribute used in your tag

# now if you want to find one spicific element by unique id you can use find method

headings = soup.find(name="h1", id="name")
print(headings)

# finding element by class is little bit different just add an underscore after class keyword

heading = soup.find(name="h3", class_="heading")
print(heading)

# and remember find will only give the first matching element not all of them if you want all of then use find all


# same goes for select and selet one like find and find all
#find by css selectors

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name") # selcting with id
print(name)

heading = soup.select_one(selector=".heading") # selecting ith class
print(heading)

