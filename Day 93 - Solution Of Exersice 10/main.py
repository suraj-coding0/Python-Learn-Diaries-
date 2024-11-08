import requests
import json


query = input("what types of new are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-06&sortBy=publishedAt&apiKey=7a6f21e04c5a446d99736bfb7f0ace9a"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------")