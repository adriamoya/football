# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClasifcacionItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	temporada = scrapy.Field()
	jornada = scrapy.Field()
	equipo = scrapy.Field()
	posicion = scrapy.Field()
	puntos = scrapy.Field()
	partidos_jugados = scrapy.Field()
	partidos_ganados = scrapy.Field()
	partidos_perdidos = scrapy.Field()
	partidos_empatados = scrapy.Field()
	goles_favor = scrapy.Field()
	goles_contra = scrapy.Field()
	pass
