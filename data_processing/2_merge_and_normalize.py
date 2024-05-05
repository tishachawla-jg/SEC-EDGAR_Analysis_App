import os
import zipfile
import json
from bs4 import BeautifulSoup  # We'll use BeautifulSoup to handle HTML

def extract_html_content(text_content):
    """ Extracts and cleans HTML content within <TEXT> tags using BeautifulSoup. """
    try:
        soup = BeautifulSoup(text_content, 'html.parser')
        # Extract text from HTML
        return soup.get_text(separator=' ', strip=True)
    except Exception as e:
        return f"Failed to parse HTML: {str(e)}"

def preprocess_and_extract_text(content):
    """ Attempts to extract the content within <TEXT>...</TEXT> tags. """
    start_tag = '<TEXT>'
    end_tag = '</TEXT>'
    try:
        start_index = content.index(start_tag) + len(start_tag)
        end_index = content.index(end_tag)
        text_content = content[start_index:end_index]
        return extract_html_content(text_content)
    except ValueError:
        return "Could not find <TEXT> tags"

def merge_full_submission_texts_to_json(zip_path, output_json_file):
    with zipfile.ZipFile(zip_path, 'r') as z:
        all_folders = [item for item in z.namelist() if item.endswith('/')]
        folders = [f for f in all_folders if f.startswith('MSFT/10-K/') and f.count('/') == 3]
        merged_texts = {}

        for folder in folders:
            file_path = os.path.join(folder, 'full-submission.txt')
            if file_path in z.namelist():
                with z.open(file_path) as file:
                    content = file.read().decode('utf-8')
                    normalized_content = preprocess_and_extract_text(content)
                    folder_key = folder.strip('/')
                    merged_texts[folder_key] = normalized_content

        with open(output_json_file, 'w') as f_out:
            json.dump(merged_texts, f_out, indent=4)

zip_path = '/content/filings.zip'
output_json_file = 'extracted_html_content.json'

# Assuming this function merges the full submission texts into JSON
merge_full_submission_texts_to_json(zip_path, output_json_file)

# Read the JSON file content
with open(output_json_file, 'r') as json_file:
    data = json.load(json_file)

# Write the JSON data to a .txt file in pretty-printed form
with open('extracted_html_content.txt', 'w') as txt_file:
    json.dump(data, txt_file, indent=4)
