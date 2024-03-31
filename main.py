import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

def count_image_occurrences(url, image_pattern):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all <img> tags in the HTML
            img_tags = soup.find_all('img')
            
            # Check if any image file matches the pattern
            for img in img_tags:
                if re.search(image_pattern, img.get('src', '')):
                    return url, 1
            
            return url, 0
        else:
            return url, 0
    except requests.exceptions.RequestException:
        return url, 0

# Specify the sitemap URL and image pattern
sitemap_url = "https://luxexpress.eu/sitemap.xml"
image_pattern = r'egg'

try:
    # Send a GET request to the sitemap URL
    response = requests.get(sitemap_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the URLs from the sitemap
    # Extract the URLs from the sitemap
        urls = [url for url in re.findall(r'<loc>(.*?)</loc>', response.text) if not ('/en/' in url or '/ru/' in url)]
        
        total_count = 0
        
        # Use ThreadPoolExecutor for concurrent execution
        with ThreadPoolExecutor() as executor:
            # Submit tasks to count image occurrences for each URL
            futures = [executor.submit(count_image_occurrences, url, image_pattern) for url in urls if url.startswith('https://')]
            
            # Process the results as they become available
            for future in as_completed(futures):
                url, count = future.result()
                if count > 0:
                    total_count += count
                    print(f"URL: {url}, Count: {count}")
        
        print(f"\nFound {total_count} eggs.")
    else:
        print(f"Failed to retrieve the sitemap. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")