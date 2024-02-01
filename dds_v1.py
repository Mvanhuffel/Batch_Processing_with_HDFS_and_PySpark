import requests
import json
import logging
from datetime import datetime
from config import API_TOKEN  # Correctly imported

# Setup basic logging configuration
logging.basicConfig(filename='shopify_data_ingestion.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

SHOP_NAME = 'dummy-data-science'
API_VERSION = '2023-01'
BASE_URL = f'https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/'

def get_headers():
    return {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": API_TOKEN,  # Use the imported API_TOKEN here
    }

def get_products():
    endpoint = 'products.json'
    url = BASE_URL + endpoint
    headers = get_headers()
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        logging.info('Successfully fetched products from Shopify')
        return response.json()
    except Exception as e:
        logging.error('Failed to fetch products from Shopify', exc_info=True)
        return None

def save_data(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        logging.info(f'Data successfully saved to {filename}')
    except Exception as e:
        logging.error(f'Failed to save data to {filename}', exc_info=True)

if __name__ == '__main__':
    logging.info('Starting Shopify data ingestion script')
    products = get_products()
    if products:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"C:\\Users\\Mtvan\\Documents\\All Projects\\Python\\Dummy Data Science\\data\\products_{timestamp}.json"
        save_data(products, filename)
    else:
        logging.error('No products fetched, terminating script')









