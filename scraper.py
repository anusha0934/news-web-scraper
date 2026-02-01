import requests
from bs4 import BeautifulSoup

url = input("Enter news article URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("title")
print("Title:", title.text if title else "No title found")

paragraphs = soup.find_all("p")
content = "\n".join(p.text for p in paragraphs)

print("\nArticle Content:\n")
print(content)