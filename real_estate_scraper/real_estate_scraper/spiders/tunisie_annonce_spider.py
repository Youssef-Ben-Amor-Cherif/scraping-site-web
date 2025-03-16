import scrapy
import re
from real_estate_scraper.items import RealEstateItem

class TunisieAnnonceSpider(scrapy.Spider):
    name = "tunisie_annonce"
    allowed_domains = ["www.tunisie-annonce.com"]
    start_urls = ["http://www.tunisie-annonce.com/AnnoncesImmobilier.asp"]

    def parse(self, response):
        # Log the current page URL
        self.logger.info(f"Scraping page: {response.url}")

        # Target Table 1 (index 1, 1-based XPath)
        for row in response.xpath("//table[1]//tr"):
            cols = row.xpath("./td")
            if len(cols) == 13:  # Listings have 13 columns
                item = RealEstateItem()
                
                # Extract fields
                item["location"] = cols[1].xpath("./a/text()").get(default="N/A").strip()
                item["nature"] = cols[3].xpath("./text()").get(default="N/A").strip()
                item["property_type"] = cols[5].xpath("./text()").get(default="N/A").strip()
                item["title"] = cols[7].xpath("./a/text()").get(default="N/A").strip()
                annonce_url = cols[7].xpath("./a/@href").get()
                item["url"] = response.urljoin(annonce_url) if annonce_url else response.url
                item["price"] = cols[9].xpath("./text()").get(default="N/A").strip()
                item["publication_date"] = cols[11].xpath("./text()").get(default="N/A").strip()
                item["area"] = "N/A"
                item["description"] = "N/A"
                item["contact"] = "N/A"

                if annonce_url:
                    yield response.follow(annonce_url, callback=self.parse_listing, meta={"item": item})
                else:
                    yield item

        # Find and follow the "Next" link
        next_page = response.xpath('//a[img/@src="/images/n_next.gif"]/@href').get()
        if next_page:
            self.logger.info(f"Found next page: {next_page}")
            yield response.follow(next_page, callback=self.parse)
        else:
            self.logger.info("No next page found, stopping pagination")

    def parse_listing(self, response):
        item = response.meta["item"]
        yield item