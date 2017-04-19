from bs4 import BeautifulSoup
import urllib.request
html = urllib.request.urlopen("https://www.google.co.jp/")

soup = BeautifulSoup(html)

print(soup.find_all("a")[0].get("href"))
