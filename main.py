# How to scrape data from a simple ranking website for movies
from bs4 import BeautifulSoup
import requests
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

# Find all h3 elements with class "title" within the specified div
movie_titles = soup.find_all('h3', class_='title')

# List comprehsion get text in list
movie_texts = [tags.text for tags in movie_titles]


# Define a regular expression pattern to extract the rank and name
pattern = re.compile(r'(\d+)\)\s+(.+)')

# Lists to store ranks and names
ranks = []
names = []

# Process each movie text
for text in movie_texts:
    match = pattern.match(text)
    if match:
        rank = match.group(1)
        name = match.group(2)
        ranks.append(rank)
        names.append(name)

# Print the results
print("Ranks:", ranks)
print("Names:", names)

# Combine ranks and names into a list of tuples
movie_data = list(zip(ranks, names))

# Sort the list of tuples by rank in descending order
sorted_movie_data = sorted(movie_data, key=lambda x: int(x[0]))

# Specify the file path where you want to write the data
file_path = 'movie_data.txt'


print(sorted_movie_data)

with open(file_path, 'w', encoding='utf-8') as file2:
    for rank, name in sorted_movie_data:
        file2.write(f"{rank} {name}\n")
