# Movie Ranking Scraper

## Overview

This Python script demonstrates a simple web scraping technique to extract movie rankings from a webpage and organize the data. The code utilizes the BeautifulSoup library to parse HTML content and the requests library to fetch data from a movie ranking website. The extracted information is then processed, and the movie ranks and names are printed and stored in a text file.

## Prerequisites

Ensure you have the necessary libraries installed before running the script. You can install them using the following:

```bash
pip install beautifulsoup4 requests
```

## How it Works

1. The script sends a request to a specified URL of a movie ranking webpage and retrieves the HTML content.

2. BeautifulSoup is used to parse the HTML and locate all `<h3>` elements with the class "title," which usually represent movie titles on the webpage.

3. A regular expression pattern is defined to extract the movie rank and name from each `<h3>` element's text.

4. The extracted ranks and names are stored in separate lists.

5. The script then prints the extracted movie ranks and names.

6. The ranks and names are combined into a list of tuples.

7. The list of tuples is sorted by rank in ascending order.

8. The sorted data is written to a text file named `movie_data.txt`, with each line containing the movie rank and name.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. Run the script:

   ```bash
   python script_name.py
   ```

4. View the results in the console and find the sorted movie data in `movie_data.txt`.

Feel free to modify the script according to your specific needs and explore more features of BeautifulSoup for web scraping.
