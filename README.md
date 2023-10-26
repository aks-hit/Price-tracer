# Price-tracer

```markdown
# Amazon Price Tracer

## Description
The Amazon Price Tracer is a Python script that extracts product information, including the product title and price, from an Amazon product page. It uses the `requests` library to fetch the page's HTML and `BeautifulSoup` for parsing.

## Prerequisites
- Python 3.x installed
- Required libraries: `requests`, `BeautifulSoup` (install using `pip install requests beautifulsoup4`)

## Usage
1. Make sure you have Python and the required libraries installed.
2. Create an instance of the `PriceTracer` class by providing the URL of the Amazon product page you want to scrape.
3. Call the `product_title()` and `product_price()` methods to retrieve the product title and price, respectively.

   Example:
   ```python
   device = PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Storage-6000mAh-Battery/dp/B0B4F2TTTS/ref=sr_1_3?crid=3E1HRUFUHK4MM&keywords=phones&qid=1698301879&sprefix=phones%2Caps%2C276&sr=8-3")
   print(device.product_title())
   print(device.product_price())
   ```

## Output
- The script will print the product title and price if the relevant HTML elements are found on the page.

## Customization
- You can use this script to scrape other Amazon product pages by creating new instances of the `PriceTracer` class with different URLs.

## Note
- Be sure to comply with Amazon's terms of service and legal regulations when scraping their website.

## Author
Akshit Singh
