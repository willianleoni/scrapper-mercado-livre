class ProductDetailsExtractor:
    def __init__(self, soup):
        self.soup = soup

    def extract_products(self):
        products = []
        product_list = self.soup.find_all('li', class_='ui-search-layout__item')
        
        for product in product_list:
            title = self.get_title(product)
            link = self.get_link(product)
            store = self.get_store(product)
            rating = self.get_rating(product)
            price = self.get_price(product)
            discounted_price = self.get_discounted_price(product)
            shipping = self.get_shipping(product)

            products.append({
                'title': title,
                'link': link,
                'store': store,
                'rating': rating,
                'price': price,
                'discounted_price': discounted_price,
                'shipping': shipping
            })
        
        return products

    def get_title(self, product):
        title_tag = product.find('h2', class_='ui-search-item__title')
        return title_tag.text.strip() if title_tag else None

    def get_link(self, product):
        link_tag = product.find('a', class_='ui-search-link')
        return link_tag['href'] if link_tag else None

    def get_store(self, product):
        store_tag = product.find('p', class_='ui-search-official-store-label')
        return store_tag.text.strip() if store_tag else None

    def get_rating(self, product):
        rating_tag = product.find('span', class_='ui-search-reviews__rating-number')
        return rating_tag.text.strip() if rating_tag else None

    def get_price(self, product):
        price_tag = product.find('div', class_='ui-search-price ui-search-price--size-medium')
        if price_tag:
            price_span = price_tag.find('span', class_='andes-money-amount__fraction')
            return price_span.text.strip() if price_span else None
        return None

    def get_discounted_price(self, product):
        discount_price_tag = product.find('div', class_='ui-search-price__second-line')
        if discount_price_tag:
            discount_price_span = discount_price_tag.find('span', class_='andes-money-amount__fraction')
            return discount_price_span.text.strip() if discount_price_span else None
        return None

    def get_shipping(self, product):
        shipping_tag = product.find('span', class_='ui-pb-highlight', style=True)
        return shipping_tag.text.strip() if shipping_tag else None
