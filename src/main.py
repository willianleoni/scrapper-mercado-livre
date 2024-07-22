import argparse
from scrapper import MercadoLivreScraper
from extractor import ProductDetailsExtractor
from dataframe import products_to_dataframe, add_discount_column, convert_discount_to_percentage, sort_by_discount, save_to_excel
from tqdm import tqdm

def main():
    # Configura o argumento da linha de comando
    parser = argparse.ArgumentParser(description='Scrape Mercado Livre for product details.')
    parser.add_argument('-url', required=True, help='URL to scrape')
    args = parser.parse_args()

    url = args.url

    # Inicializa uma lista para armazenar todos os produtos
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

    # Converte a lista de todos os produtos em um DataFrame
    print("Generating DataFrame...")
    df = products_to_dataframe(all_products)
    df = add_discount_column(df)
    df = convert_discount_to_percentage(df)
    df = sort_by_discount(df)

    # Salva o DataFrame como um arquivo Excel
    save_to_excel(df)
    print("DataFrame generated and saved to products.xlsx successfully:")

if __name__ == '__main__':
    main()
