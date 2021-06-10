from requests import get
from bs4 import BeautifulSoup

# FIRST STEP -> REQUEST AND RESPONSE
resp = get("https://quotes.toscrape.com/")  # request and get response

# 2ND STEP -> MAKE RESPONSE BODY IN PERFECT EXTRACTABLE FORM
soup = BeautifulSoup(resp.text, "lxml")  # html.parser make raw_response body to perfect form

# data = [1, 2, 3, 4]
# data[0]
# 3RD STEP -> EXTRACT SELECTED DATA
output = soup.select("span.text")

print(output[0].text)

print("hello")

