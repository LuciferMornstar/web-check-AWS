import scrapy

class ContactSpider(scrapy.Spider):
    name = "contact_spider"
    start_urls = [
        'https://example.com',  # Replace with the target website URL
    ]

    def parse(self, response):
        for contact in response.css('div.contact-info'):  # Adjust the selector based on the website structure
            yield {
                'name': contact.css('span.name::text').get(),
                'email': contact.css('span.email::text').get(),
                'phone': contact.css('span.phone::text').get(),
            }

        next_page = response.css('a.next::attr(href)').get()  # Adjust the selector for pagination if needed
        if next_page is not None:
            yield response.follow(next_page, self.parse)