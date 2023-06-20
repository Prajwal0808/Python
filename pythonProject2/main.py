import requests
from bs4 import BeautifulSoup

def crawl(url, max_depth):
    # Create a set to store visited URLs
    visited = set()

    # Recursive function to crawl URLs
    def crawl_recursive(url, depth):
        # Terminate if maximum depth is reached
        if depth > max_depth:
            return

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Process the page as needed (e.g., extract data, store information)
            # For example, print the page title
            print(soup.title.string)

            # Add the current URL to the visited set
            visited.add(url)

            # Find all <a> tags for hyperlinks
            links = soup.find_all('a')

            # Process each hyperlink
            for link in links:
                href = link.get('href')

                # Check if the hyperlink is a valid URL
                if href and href.startswith('http') and href not in visited:
                    # Recursively crawl the hyperlink
                    crawl_recursive(href, depth + 1)

        except requests.exceptions.RequestException:
            # Handle any request errors
            pass

    # Start crawling
    crawl_recursive(url, 0)

# Usage example
crawl('https://example.com', 2)
