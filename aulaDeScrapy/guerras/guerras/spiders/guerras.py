import scrapy
from scrapy.selector import Selector

class GuerraSpider(scrapy.Spider):
    name = "guerras"
    #allowed_domains = ["exemple.com"]
    start_urls = ["http://pt.wikipedia.org/wiki/Lista_de_guerras_por_n%C3%BAmero_de_mortos"]

    def parse(self, response):
        selector = Selector(response)
        tabelas = selector.xpath("//table[contains(@class, 'wikitable')]")
        linhas = tabelas.xpath(".//tr[position()>1]")
        for linha in linhas:
            dados = linha.xpath(".//td//text()").getall()
            yield {
                'conflito': dados[0],
                'mortes': dados[1],
                'ano': dados[2],
                'localização': dados[3],
                'dados': dados[4],
            }