#!/usr/bin/env python
# -*- coding: latin-1 -*-

import scrapy
import re
import decimal
import datetime

from scrapy.conf import settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.request import Request
from scrapy.selector import Selector

from ..items import ClasifcacionItem

base_url = 'https://www.laliga.es/en/statistics-historical/standings/primera/'

'''
temporada
jornada
equipo
posicion
puntos
partidos_ganados
partidos_perdidos
partidos_empatados
goles_favor
goles_contra
'''

class ClasificacionSpider(scrapy.Spider):
	
	name = 'laliga_spider'	
	allowed_domains = ['www.laliga.es']
	start_urls = [
		"https://www.laliga.es/en/statistics-historical/standings/primera/2003-04/jornada-01/",
	]


	def parse(self, response):

		self.logger.info('SPIDER WORKING ........')
		
		for cod_temporada in range(2003,2017,1):
			for cod_jornada in range(1,39,1):
				# cod_jornada = 20
				# cod_temporada = 2016

				extra_url = '%s-%s/jornada-%s/' % (cod_temporada, str(cod_temporada+1)[-2:], str(100+cod_jornada)[-2:])
				page_url = base_url + extra_url

				request = scrapy.Request(
					page_url,
					callback=self.parse_clasificacion,
					meta={'jornada': cod_jornada},
					dont_filter=True)

				yield request # request call back from each page


	def parse_clasificacion(self, response):

		jornada = response.request.meta['jornada']

		trows = response.xpath('//div[@id="titulo"]/following-sibling::table/thead/following-sibling::tbody/tr')		
		temporada = int(re.findall('\d+',response.xpath('//div[@id="titulo"]/div/text()').extract()[0].strip())[0])

		for trow in trows:

			list_info = trow.xpath('./td/text()').extract()
			list_info = [re.findall('\d+',item.strip())[0].strip() for item in list_info]

			clasif = ClasifcacionItem()
			
			clasif["jornada"] = jornada
			clasif["temporada"] = temporada
			clasif["equipo"] = trow.xpath('./td/span/text()').extract()[0].strip()
			clasif["posicion"] = int(list_info[0])
			clasif["puntos"] = int(list_info[1])
			clasif["partidos_jugados"] = int(list_info[2])
			clasif["partidos_ganados"] = int(list_info[3])
			clasif["partidos_perdidos"] = int(list_info[4])
			clasif["partidos_empatados"] = int(list_info[5])
			clasif["goles_favor"] = int(list_info[6])
			clasif["goles_contra"] = int(list_info[7])

			yield clasif # request call back from each page


