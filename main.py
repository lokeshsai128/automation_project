import os 
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
 
# Define directories
download_dir = os.path.join(os.getcwd(), 'downloads')
extracted_data_dir = os.path.join(os.getcwd(), 'extracted_data')

# Ensure directories exist
os.makedirs(download_dir, exist_ok=True)
os.makedirs(extracted_data_dir, exist_ok=True)

def setup_driver():
    """Setup Selenium WebDriver."""
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome();
    driver.set_window_size(1920, 1080)
    return driver

def download_files(driver, url):
    """Navigate website and download files."""
    driver.get(url)
    download_links = driver.find_elements(By.XPATH, '//a[contains(@href, "download")]')

    for link in download_links:
        href = link.get_attribute('href')
        try:
            driver.get(href)
            time.sleep(2)  # Wait for the download to complete
        except Exception as e:
            print(f"Error downloading {href}: {e}")

def process_csv(file_path):
    """Process CSV file and extract data."""
    data = pd.read_csv(file_path)
    extracted_data = data[['ColumnOfInterest']]
    output_path = os.path.join(extracted_data_dir, f'extracted_{os.path.basename(file_path)}')
    extracted_data.to_csv(output_path, index=False)

def process_files():
    """Read and extract data from downloaded files."""
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)
        if filename.endswith('.csv'):
            try:
                process_csv(file_path)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        else:
            print(f"Skipping unsupported file type: {filename}")

def main():
    url = 'http://google.com'  #Need to try with our URL
    driver = setup_driver()
    try:
        download_files(driver, url)
    finally:
        driver.quit()
    process_files()

if __name__ == '__main__':
    main()
