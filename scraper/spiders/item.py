import scrapy
import json

class ItemListSpider(scrapy.Spider):
    name = "item"
    allowed_domains = ["test-example.com"]

    custom_settings = {
    "DEFAULT_REQUEST_HEADERS": {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    }
}

    # Start from page 1
    def start_requests(self):
        url = (
            "https://www.test-example.com/api/category/12"
            "?currentPage=1&pageSize=20&format=json"
            "&sortBy=relevance&curated=true&curatedid=dummy-collection-12"
            "&gridColumns=5&advfilter=true"
            
        )
        yield scrapy.Request(url, callback=self.parse, cb_kwargs={"page": 1})

    def parse(self, response, page):
        data = json.loads(response.text)

        for product in data.get("products", []):
            price = product.get("price", {})
            offerPrice = product.get("offerPrice", {})
            yield {
                "catalogName": product.get("catalogName"),
                "name": product.get("name"),
                "couponStatus": product.get("couponStatus"),
                "images": product.get("images"),
                "price": price.get("formattedValue"),
                "offerPrice": offerPrice.get("formattedValue"),
                "segmentName": product.get("segmentNameText")
            }

        pagination = data.get("pagination", {})
        total_pages = pagination.get("totalPages", 1)

        if page < total_pages:
            next_page = page + 1
            next_url = (
                f"https://www.test-example.com/api/category/12"
                f"?currentPage={next_page}&pageSize=20&format=json"
                f"&sortBy=relevance&curated=true&curatedid=dummy-collection-12"
                f"&gridColumns=5&advfilter=true"
            )
            yield scrapy.Request(next_url, callback=self.parse, cb_kwargs={"page": next_page})