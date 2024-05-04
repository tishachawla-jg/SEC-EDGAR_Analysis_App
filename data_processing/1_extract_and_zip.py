# Import necessary libraries
from sec_edgar_downloader import Downloader
import shutil
from google.colab import files

# Initialize a downloader instance
dl = Downloader("Tisha", "XXXXX@gmail.com")

# Get all 10-K filings for the ticker between Jan 1, 1995, and Dec 31, 2023
dl.get("10-K", "AAPL", after="1995-01-01", before="2023-12-31")

# Specify the folder where the downloaded filings are stored
download_folder = 'sec-edgar-filings'

# Compress the downloaded filings into a ZIP file
shutil.make_archive('filings', 'zip', download_folder)

# Download the ZIP file
files.download('filings.zip')
