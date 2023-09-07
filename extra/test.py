from search_engines import Google, Bing
import requests
from requests.auth import HTTPProxyAuth

proxy = "brd.superproxy.io:22225"
username = "brd-customer-hl_93b5fa1a-zone-data_center"
password = "ask3gh8zga95"

proxies = {"http": f"http://{proxy}"}
auth = HTTPProxyAuth(username, password)
session = requests.session()
session.proxies = proxies
session.auth = auth

print(session.proxies)
print(session.auth)

try:
    response = session.get("https://stackoverflow.com/questions/32986228/difference-between-using-requests-get-and-requests-session-get")
    print(response.status_code)
except Exception as e:
    print(str(e))
    print("ERROR")
    pass
#proxy = username = password = None
engine = Google(proxy = proxy, username = username, password = password, language = "ES")
#engine = Google(proxy = proxy, username = username, password = password, language = "ES")

results = engine.search("MSI GT77 Titan 12UGS-008 17.3 / Nvidia GeForce RTX 3070 Ti UHD Intel Core i9-12900HX 1.5GHz / 128GB RAM / 2TB SSD", pages = 1)
#results = engine.search("Huawei Matedock 2 Blanco", pages = 1)
print(results.titles())