import time

from bs4 import BeautifulSoup
import requests
import translators as ts
import os

os.chdir("/new/Web_Scrapping/Flask/templates")
unfinished = []

for filename in os.listdir():
    with open(f"{filename}", "r") as rfile:
        html = rfile.read()
        soup = BeautifulSoup(html, "html.parser")
        with open(f"{filename[:-5]}-it.html", "w") as wfile:
            time.sleep(1)
            print(filename)
            try:
                translated_text = ts.translate_html(str(soup), translator='google', to_language='it')
            except IndexError:
                print("Translation not available")
                unfinished.append(filename)
            wfile.write(translated_text)
            wfile.write("\n")

for filename in unfinished:
    print("Start converting unfinished :")
    time.sleep(1)
    with open(f"{filename}", "r") as rfile:
        html = rfile.read()
        soup = BeautifulSoup(html, "html.parser")
        os.chdir("/new/Web_Scrapping/Flask/templates")
        with open(f"{filename[:-5]}-it.html", "w") as wfile:
            time.sleep(1)
            print(filename)
            try:
                translated_text = ts.translate_html(str(soup), translator='bing', to_language='it')
            except IndexError:
                print("Translation not available")
                unfinished.append(filename)
            wfile.write(translated_text)
            wfile.write("\n")
'''
url = 'https://12factor.net/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = [url + (a.get('href')[2:]) for a in soup.find_all('a', href=True) if a['href'].startswith('./')]
unfinished_links = ['https://12factor.net/port-binding', 'https://12factor.net/backing-services', 'https://12factor.net/admin-processes']

for link in links:
    time.sleep(1)
    html = requests.get(link)
    new_soup = BeautifulSoup(html.content, 'html.parser')
    list_article = new_soup.find_all("article")
    with open(f"{link[21:]}-it.html", "w") as wfile:
        assert link[:21] == 'https://12factor.net/'
        for idx in range(len(list_article)):
            article = str(list_article[idx])
            try:
                translated_text = ts.translate_html(str(article), translator='google', to_language='it')
            except IndexError:
                translated_text = "Translation not available"
                unfinished_links.append(link)
            wfile.write(translated_text)
            wfile.write("\n")
            print(idx)

for link in unfinished_links:
    time.sleep(1)
    html = requests.get(link)
    new_soup = BeautifulSoup(html.content, 'html.parser')
    list_article = new_soup.find_all("article")
    with open(f"{link[21:]}-it.html", "w") as wfile:
        assert link[:21] == 'https://12factor.net/'
        for idx in range(len(list_article)):
            article = str(list_article[idx])
            try:
                translated_text = ts.translate_html(str(article), translator='google', to_language='it')
            except IndexError:
                translated_text = "Translation not available"
                unfinished_links.append(link)
            wfile.write(translated_text)
            wfile.write("\n")
            print(idx)
'''