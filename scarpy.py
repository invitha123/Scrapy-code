import scrapy

class InduSpider(scrapy.Spider):
    name = 'indu'
    start_urls = ['http://www.rgukt.ac.in']  # Replace with your target website URL

    def parse(self, response):
        # Extract all visible text from the page
        all_text = response.xpath('//body//text()').getall()
        
        # Join the extracted text into a single string and strip whitespace
        extracted_text = ' '.join(all_text).strip()
        
        # Print the extracted text
        print("Extracted Text:")
        print(extracted_text)
