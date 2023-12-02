import scrapy
from coinscraper.items import CoinItem
import time

class CoinspiderSpider(scrapy.Spider):
    name = "coinspider"
    allowed_domains = ["en.numista.com"]
    start_urls = ["https://en.numista.com/catalogue/india-1.html?q=200"] 



    def parse(self, response):
        coins = response.css('div.resultat_recherche')

        for coin in coins:
            relative_url = coin.css('strong a ::attr(href)').get()
            coin_url = 'https://en.numista.com/' + relative_url
            yield response.follow(coin_url, callback=self.parse_coin_page)
       

       
            

    def parse_coin_page(self, response):
        table_rows = response.css("table tr")
        coin_item = CoinItem()

        coin_item['url'] = response.url,
        coin_item['coin_name'] = response.css('#main_title h1::text').get(),
        coin_item['field1'] = table_rows[0].css("td a::text").get(),
        coin_item['field2'] = table_rows[1].css("td ::text").get(),
        coin_item['field3' ] = table_rows[2].css("td ::text").get(),
        coin_item['field4'] = table_rows[3].css("td ::text").get(),
        coin_item['field5'] = table_rows[4].css("td ::text").get(),
        coin_item['field6'] = table_rows[5].css("td ::text").get(),
        coin_item['field7'] = table_rows[6].css("td ::text").get(),
        coin_item['field8']=  table_rows[7].css("td ::text").get(),
        coin_item['field9']=  table_rows[8].css("td ::text").get(),
        coin_item['field10']=  table_rows[9].css("td ::text").get(),
        coin_item['field11']=  table_rows[10].css("td ::text").get(),
        coin_item['field12']=  table_rows[11].css("td ::text").get(),
        coin_item['field13']=  table_rows[11].css("td ::text").get(),
        coin_item['field14']=  table_rows[11].css("td ::text").get(),
        coin_item['field15']=  table_rows[11].css("td ::text").get(),
        coin_item['observe_description'] = response.css('#fiche_descriptions > p::text').get(),
        coin_item['reverse_description'] = response.css('#fiche_descriptions > h3:contains("Reverse") + p::text').get(),
        coin_item['mintage'] =  response.css('td.tirage ::text').getall(),
        coin_item['observe_img'] = response.css('div#fiche_photo a.coin_pic:first-child img::attr(src)').get(),
        coin_item['reverse_img'] = response.css('div#fiche_photo a.coin_pic:nth-child(2) img::attr(src)').get(),
        
        
        yield coin_item
