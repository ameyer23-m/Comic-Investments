import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.marvel.com/comics/series'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <a> tags within <li> tags
    series_links = soup.find_all('li')

    # Extract the text from the <a> tags and store them in a list
    series_names = [link.a.text for link in series_links]

    # Write the list of series names to a text file
    with open('Marvel_comic_series_names.txt', 'w') as f:
        for series_name in series_names:
            f.write(series_name + '\n')

    print('List of comic series names has been saved to Marvel_comic_series_names.txt')

else:
    print('Failed to retrieve the webpage.')
