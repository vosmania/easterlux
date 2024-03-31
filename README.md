# main.py

This script is used to count the occurrences of a specific image pattern in the sitemap of a website. It uses Python's `requests` and `BeautifulSoup` libraries to send HTTP requests and parse HTML content, respectively. It also uses `concurrent.futures` for concurrent execution.
The purpose of this script is to find all easter eggs with minimal effort.

## Usage

```sh
python main.py
```

## Functions

- `count_image_occurrences(url, image_pattern)`: This function sends a GET request to the specified URL, parses the HTML content, finds all `<img>` tags, and checks if any image file matches the pattern. It returns the URL and the count of matching images.

## Variables

- `sitemap_url`: The URL of the sitemap to be parsed.
- `image_pattern`: The image pattern to be searched for in the sitemap.

## Requirements

- Python 3
- `requests` library
- `BeautifulSoup` library

## Installation

To install the required libraries, run the following command:

```sh
pip install requests beautifulsoup4
```

## Note

This script excludes URLs that contain '/en/' or '/ru/' from the sitemap.
