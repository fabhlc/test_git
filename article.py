from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
import os

article = input("Url of article? (Toronto Star or The Globe and Mail)")

# article = "https://www.thestar.com/news/gta/2019/07/05/heres-what-youd-need-to-earn-to-buy-a-mid-priced-home-in-your-toronto-neighbourhood-and-what-a-typical-family-there-earns-hint-not-nearly-enough.html"
# article = "https://www.theglobeandmail.com/business/economy/article-how-canadas-suburban-dream-became-a-debt-filled-nightmare/"

soup = BeautifulSoup(urlopen(article.strip()), 'html.parser')

if 'star.com' in article:
    container = soup.find("div", class_='main-content')
elif 'globeandmail.com' in article:
    container = soup.find_all("p", class_='c-article-body__text')

with open('tmp/article.html', 'w') as f:
    for i in container:
        f.writelines(i.text)
        f.write('<p><p>')

webbrowser.open(os.path.join(os.getcwd(), 'tmp/article.html'), new=2)