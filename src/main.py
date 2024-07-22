import argparse
from scrapper import MercadoLivreScraper
from extractor import ProductDetailsExtractor
from dataframe import DataFrameHandler
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description='Scrape Mercado Livre for product details.')
    parser.add_argument('-url', required=True, help='URL to scrape')
    args = parser.parse_args()

    url = args.url

    all_products = []

    # Processa a URL
    print("Starting product search...")
    while url:
        print(f"Processing URL: {url}")
        scraper = MercadoLivreScraper(url)
        soup = scraper.fetch_page_data()
        
        if soup:
            extractor = ProductDetailsExtractor(soup)
            products = extractor.extract_products()
            print(f"Found {len(products)} products in URL: {url}")
            all_products.extend(products)
            
            # Get the next page URL
            url = scraper.get_next_page_url(soup)
        else:
            print(f"Failed to fetch data from URL: {url}")
            url = None  # Stop the loop if there's an error

    print(f"Total products found: {len(all_products)}")

    print("Generating DataFrame...")
    df_handler = DataFrameHandler(all_products)
    df_handler.add_discount_column()
    df_handler.convert_discount_to_percentage()
    df_handler.sort_by_discount()

    df_handler.save_to_excel()
    print("DataFrame generated and saved to products.xlsx successfully")

if __name__ == '__main__':
    main()
