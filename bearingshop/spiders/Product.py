import json
import os
import re
import scrapy


def image_name_beautifier(image_name):
    return image_name.translate({ord(c): " " for c in "'\","})


def process_image_url(image_arr):
    return [img_url if img_url.startswith('http') else ('http:' + img_url) for img_url in image_arr]


class Category(scrapy.Spider):
    name = 'product'
    start_urls = set()

    if os.path.isfile("v1/product-url.json"):
        with open('v1/product-url.json') as json_file:
            data = json.load(json_file)
            for p in data:
                start_urls.add(p['product-url'])

    def parse(self, response):
        # f = open("response.html", "w")
        # f.write(response.body.decode("utf-8"))
        # f.close()
        page = response.xpath('//div[contains(@class,"ma-main-container")]/div[contains(@class,"container")]')
        product_path = page.xpath('//div[contains(@class,"product-shop")]')

        category = page.xpath('//div[contains(@class,"breadcrumbs")]//ul/li')
        categories = category.xpath('./a/text()').getall()
        categories.remove('Home')

        name = product_path.xpath('./div[@class="product-name"]/h1/text()').get()
        price_path = product_path.xpath('./div[@class="box-container2"]//div[@class="price-box"]')
        sale_price = ''
        regular_price = ''
        if price_path.xpath('./p[@class="special-price"]/span[@class="price"]/text()').get():
            sale_price = price_path.xpath('./p[@class="special-price"]/span[@class="price"]/text()').get()
            sale_price = float(sale_price.replace("$", "").replace(",", "")) * 85
            regular_price = price_path.xpath('./p[@class="old-price"]/span[@class="price"]/text()').get()
            regular_price = float(regular_price.replace("$", "").replace(",", "")) * 85
        else:
            regular_price = price_path.xpath('./span[@class="regular-price"]/span[@class="price"]/text()').get()
            regular_price = float(regular_price.replace("$", "").replace(",", "")) * 85

        short_description = ''
        short_description_path = product_path.xpath('./div[contains(@class,"short-description")]')
        short_description_arr = short_description_path.xpath('./div[contains(@class,"std")]/text()').getall()
        short_description = '\n'.join(short_description_arr)

        if short_description_path.xpath('./div[contains(@class,"std")]/p'):
            short_description_arr = short_description_path.xpath('./div[contains(@class,"std")]/p/text()|./div[contains(@class,"std")]/p/span/text()|./div[contains(@class,"std")]/p/b/text()').getall()
            short_description_arr = [x for x in short_description_arr if x.strip()]
            length = len(short_description_arr)
            if length > 0:
                for i in range(0, length, 2):
                    try:
                        short_description = short_description + short_description_arr[i] + short_description_arr[i+1] + '\n'
                    except IndexError:
                        f = open("error.txt", "a")
                        f.write('IndexError')
                        f.write(response.url)
                        f.write('\n')
                        f.close()

        short_description = short_description.replace("if you need support on selection of bearings,contact us at", "").replace("info@bearingshop.org", "")

        description_path = page.xpath('//div[@id="product_tabs_description_contents"]//div[@class="std"]')
        description_arr = description_path.xpath('./h1/text()|./h2/text()|./h3/text()|./h4/text()|./h5/text()|./p/text()|./p/span/text()|./p/strong/text()|./p/b/text()').getall()
        description = '\n'.join(description_arr)

        description = description.replace("if you need support on selection of bearings,contact us at", "").replace("info@bearingshop.org", "")

        trs = page.xpath("//div[@class='product-view']//div[@id='product_tabs_description_contents']/div[@class='std']/table/tbody/tr/td/table/tbody/tr")
        if trs:
            description = description + '\n\n'
            for t in trs:
                print(re.sub(r'\s+', ' ', " ".join([x.strip() for x in t.xpath(".//text()").extract()])))
                description = description + re.sub(r'\s+', ' ', " ".join([x.strip() for x in t.xpath(".//text()").extract()])) + '\n'

        product_img = page.xpath('//div[@class="product-img-box"]/div[@class="more-views ma-more-img"]/ul/li')

        image_arr = process_image_url(product_img.xpath('./a[@class="cloud-zoom-gallery"]/@href').getall()) # info@chitraexpress.com.bd
        images = set()
        for url in image_arr:
            img_file = image_name_beautifier(url.strip().split('/')[-1])
            images.add(img_file)

        product = {
            'SL NO': '',
            'Type': 'simple',
            'SKU': '',
            'Name': name,
            'Published': 1,
            'Is featured?': 0,
            'Visibility in catalog': 'visible',
            'Short Description': short_description,
            'Description': description,
            'In stock?': 1,
            'Sold individually?': 0,
            'Allow customer reviews?': 1,
            'Purchase note': 'Thanks for purchasing',
            'Sale price': sale_price,
            'Regular price': regular_price,
            'Categories': categories,
            'Tags': '',
            'Shipping class': 'Dhaka Only',
            'Images': ','.join(map(str, images)),
            'Position': 0,
            'Meta: _specifications_display_attributes': 'yes',
            'Meta: _per_product_admin_commission_type': 'percentage',
            'product-url': response.url,
            'image_url': image_arr,
        }

        yield product
