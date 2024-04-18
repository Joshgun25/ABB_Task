import requests
from bs4 import BeautifulSoup
import re

# Function to scrape website and extract text content
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting text content
    text_content = ""
    for element in soup.find_all():
        text_content += element.get_text() + "\n"
    
    # Process data before writing to file
    text_content = process_text(text_content)
    
    # Write processed data to file
    store_data_to_file(text_content, 'abb_website_text.txt')

# Storing text content in a file
def store_data_to_file(text_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text_content)

def process_text(text):
    # Split the text into sentences
    sentences = re.split(r'\s*[.!?]\s*', text)

    # Clean and normalize each sentence
    cleaned_sentences = [sentence.lower().strip() for sentence in sentences]

    # Remove empty sentences
    cleaned_sentences = [sentence for sentence in cleaned_sentences if sentence]

    # Convert list of cleaned sentences to a single string with newline characters
    cleaned_text = '\n'.join(cleaned_sentences)

    # Remove empty lines and reduce multiple consecutive empty spaces to a single space
    cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)
    cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)

    return cleaned_text
