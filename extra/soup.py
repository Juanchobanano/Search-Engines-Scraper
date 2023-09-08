from bs4 import BeautifulSoup
selectors = {
    'url': 'a[href]', 
    'title': 'a', 
    'text': 'div[data-sncf="1"]',
    'links': 'div#search div.g', 
    'next': 'a[href][aria-label="Page {page}"]'
}
with open("tags.html", "r") as f:
    soup = BeautifulSoup(f.read())
#print(soup)

tags = soup.select(selectors['links'])
for link in tags:
    with open("link.html", "w") as f:
        f.write(str(link))
        break
#results = [self._item(l) for l in tags]