import scrapy

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]

    def parse(self, response):
        for serie in response.css('.titleColumn'):
            titulo = serie.css('.titleColumn a::text').get()
            ano = serie.css('.secondaryInfo::text').get()[1:-1]
            
            # Seleciona o elemento pai "ratingValue" e depois obtém o elemento "strong" dentro dele
            nota = serie.xpath('../td[@class="ratingColumn imdbRating"]//strong/text()').get()
            
            yield {
                'titulo': titulo,
                'ano': ano,
                'nota': nota
            }