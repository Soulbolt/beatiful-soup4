from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)  # Extracts the text content inside the tags(title) in this occasion
# print(soup) # Displays all html content
# print(soup.prettify())  # Displays html content with proper indents.
# print(soup.a)  # Gets the first matching tag(a, p, h1, etc...)

all_anchor_tags = soup.find_all(name="a")  # Find all tags by given tag name.

# for tag in all_anchor_tags:  # Loop to get text content on each given tag: tag.getText()
    # print(tag.getText())
    # print(tag.get("href"))  # tag.get("href") gets the links

heading = soup.find(name="h1", id="name")  # Find specific tag by tag name and id name
# print(heading)

section_heading = soup.find(name="h3", class_="heading")  # Use class_ to avoid conflicts with the class in the html
print(section_heading.getText())  #  We can get different results by using getText(), .name, .get("class")

# This is a way to get a specifc anchor tag that is inside other tags
company_url = soup.select_one(selector="p a")  # p tag and a tag, can use #name to select by id
print(company_url)

headings = soup.select(".heading")  # Prints out a list of all matching class heading tags
print(headings)
