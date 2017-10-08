# laliga

### Scrapy console

```shell
scrapy shell "http://www.laliga.es/en/statistics-historical/standings/primera/2003-04/jornada-38/"
```

### Crawling

```shell
scrapy crawl laliga_spider -o laliga.json -t json
```

### Notes


Include encoding option in settings.py

```shell
FEED_EXPORT_ENCODING = 'utf-8'
```

# Approach

### JSON desired output

For each team, journey and season, we want to scrape the following info.

```json
{
   "jornada":31,
   "partidos_perdidos":7,
   "puntos":67,
   "partidos_ganados":20,
   "equipo":"Real Madrid",
   "posicion":1,
   "goles_contra":37,
   "temporada":2003,
   "goles_favor":65,
   "partidos_empatados":4
}

```