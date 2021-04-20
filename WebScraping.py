# If we want to scrap website
# 1: Use API(request)
# 2: Html web scrapping using beautiful soup (bs4)

# Step 0 : Install all the requiredment
# pip install requests ( allows you to send HTTP requests)
# pip install bs4 (Beautiful Soup is used for pulling data out of HTML and XML files.)
# pip install html5lib (for parsing HTML. It is designed for HTML specification, as is implemented by all major web browser)

import requests
from bs4 import BeautifulSoup
url = "https://www.geeksforgeeks.org/"

# Step 1 : Get the html
r = requests.get(url)
htmlContent = r.content

# Step 2 : Parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
soup.prettify()

# Step 3 : Html tree traversal
#Get the title of html page
title = soup.title
print(title.prettify())

#Get all the paragraph
para = soup.find_all('p')
print(para)

#Get all anchors tab
anchor = soup.find_all('a')

#Get all link
for link in anchor:
    print(link.get('href'))
