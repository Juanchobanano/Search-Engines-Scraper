from search_engines_kit import Google, Bing, Yahoo, Brave
import requests
from requests.auth import HTTPProxyAuth

proxy = None 
username = None
password = None

engine = Yahoo(proxy = proxy, username = username, password = password, language = "ES")
#
results, status = engine.search("MSI GT77 Titan 12UGS-008 17.3 / Nvidia GeForce RTX 3070 Ti UHD Intel Core i9-12900HX 1.5GHz / 128GB RAM / 2TB SSD", pages = 1)
print(len(results), status)
print(results.titles())
#results = engine.search("Hello world", pages = 2)
#print(results.titles())

#for result in results.titles():
#    print(result)
#
