from bs4 import BeautifulSoup
import requests
# Scraping a live website.
response = requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
# print(soup.title)
# story_article = soup.find(name="span", class_="titleline")  # Getting the first news article
# article_text = story_article.get_text()  # Getting only the text inside the tags
# article_link = story_article.find(name="a").get("href")  # This works but is not the same as in the course. Course does not use .find(name="a") since the website has been restrcutured
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

# Get all articles
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
# Loop through each article
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]  # Use of split([0]) to remove the space and text and keep number
# print(article_texts, article_links, article_upvotes)
# Find highest upvotes and print its respectice article text and link
# for index in range(len(article_upvotes)):
#     highest_number = max(article_upvotes)
#     if highest_number == article_upvotes[index]:
#         title = article_texts[index]
#         link = article_links[index]
#         print(title, link)

# Simpler way to get index and print article + link without a loop
highest_number = max(article_upvotes)
number_index = article_upvotes.index(highest_number)
print(article_texts[number_index])
print(article_links[number_index])




# # import lxml

# with open("website.html", encoding="utf-8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.string)  # Extracts the text content inside the tags(title) in this occasion
# # print(soup) # Displays all html content
# # print(soup.prettify())  # Displays html content with proper indents.
# # print(soup.a)  # Gets the first matching tag(a, p, h1, etc...)

# all_anchor_tags = soup.find_all(name="a")  # Find all tags by given tag name.

# # for tag in all_anchor_tags:  # Loop to get text content on each given tag: tag.getText()
#     # print(tag.getText())
#     # print(tag.get("href"))  # tag.get("href") gets the links

# heading = soup.find(name="h1", id="name")  # Find specific tag by tag name and id name
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")  # Use class_ to avoid conflicts with the class in the html
# print(section_heading.getText())  #  We can get different results by using getText(), .name, .get("class")

# # This is a way to get a specifc anchor tag that is inside other tags
# company_url = soup.select_one(selector="p a")  # p tag and a tag, can use #name to select by id
# print(company_url)

# headings = soup.select(".heading")  # Prints out a list of all matching class heading tags
# print(headings)
