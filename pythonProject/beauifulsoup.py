from bs4 import BeautifulSoup
import requests

# Send a GET request to the URL and retrieve the HTML content
url = "https://example.com"
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print the text content of all <h1> elements
h1_tags = soup.find_all('h1')
for h1 in h1_tags:
    print(h1.text)
