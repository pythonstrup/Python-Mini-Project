from bs4 import BeautifulSoup
# import lxml -> soup = BeautifulSoup(contents, "lxml") can be worked
import requests


URL = "https://www.marieclaire.com/culture/g2509/movies-to-watch-before-30/"

response = requests.get(URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
titles = soup.find_all(name="span", class_="listicle-slide-hed-text")

must_movies = [movie.getText() for movie in titles]

with open("Must-Watch_movies", "w") as file:
    for movie in must_movies:
        file.write(f"{must_movies.index(movie) + 1}) {movie}\n")








#
# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a", class_="storylink")
#
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# # print(article_texts)
# # print(article_links)
# print(article_upvotes)
#
# max_value = max(article_upvotes)
# max_index = article_upvotes.index(max_value)
# print(article_texts[max_index])
# print(article_links[max_index])








# with open("website.html", encoding='UTF8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a") # anchor tag in paragraph tag
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)



