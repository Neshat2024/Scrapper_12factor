from bs4 import BeautifulSoup
import requests
import time
import os

url = 'https://12factor.net/'
response = requests.get(url)
#hint = response.content == html
soup = BeautifulSoup(response.content, 'html.parser')

links = [url+(a.get('href')[2:]) for a in soup.find_all('a', href=True) if a['href'].startswith('./')]

for link in reversed(links):
    print(link)
    time.sleep(1)
    page = requests.get(link)
    new_soup = BeautifulSoup(page.content, "html.parser")
    list_article = new_soup.find_all("article")

    #THE DIRECTORY FOR STORING 'HTML' FILES IS '/new/Web_Scrapping/Flask/templates'
    os.chdir("/new/Web_Scrapping/Flask/templates")

    with open(f"{link[21:]}.html", "w") as wfile:
        assert link[:21] == 'https://12factor.net/'
        for idx in range(len(list_article)) :
            article = str(list_article[idx])
            wfile.write(article)
            wfile.write("\n")
os.rename('.html', 'base.html')

for link in links:
    time.sleep(1)
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_links = [url+(a.get('src')[1:]) for a in soup.find_all('img', src=True)]

    for link in img_links:
        print(link)
        response = requests.get(link)

        # THE DIRECTORY FOR STORING 'png' FILES IS '/new/Web_Scrapping/Flask/static/images'
        os.chdir("/new/Web_Scrapping/Flask/static/images")

        with open(f"{link[28:]}", "wb") as wfile:
            wfile.write(response.content)
