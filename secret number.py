# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP request to the website's server and retrieve the HTML content
response = requests.get('https://um6p.ma/fr')
html = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Extract the data you are interested in using BeautifulSoup's various methods
data = soup.find_all( 'h2')
print(data)
# Use Pandas to clean and organize the data
df = pd.DataFrame(data)

# Save the data to a file
df.to_csv('dataaa.csv', index=False)
