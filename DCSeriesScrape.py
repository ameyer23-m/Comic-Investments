import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url ='https://www.dcuniverseinfinite.com/browse/comics'
# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <h3> tags with class "thumbnail__title"
    series_elements = soup.find_all('h3', class_='thumbnail__title')

    # Extract the text from the <h3> tags and store them in a list
    series_names = [element.text.strip() for element in series_elements]

    # Print the list of series names
    print(series_names)

else:
    print('Failed to retrieve the webpage.')
