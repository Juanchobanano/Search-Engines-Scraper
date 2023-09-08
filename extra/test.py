from search_engines_kit import Google, Bing
import requests
from requests.auth import HTTPProxyAuth

proxy = "brd.superproxy.io:22225"
username = "brd-customer-hl_93b5fa1a-zone-data_center"
password = "ask3gh8zga95"

engine = Google(proxy = proxy, username = username, password = password, language = "ES")

results = engine.search("MSI GT77 Titan 12UGS-008 17.3 / Nvidia GeForce RTX 3070 Ti UHD Intel Core i9-12900HX 1.5GHz / 128GB RAM / 2TB SSD", pages = 1)
#print(results.titles())

for result in results.titles():
    print(result)