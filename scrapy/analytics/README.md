# Analytics

Analyzing data from scrapy. There are two different databases:

* RFEF (Real Federacion Española de Futbol): Info from each match played. Field, date, match day, local and visitor club info, etc.

* Laliga: Essentially a snapshot of the classification for each match day.

Ideally we are interested to inherit the information from the classifcation at each match day in the RFEF data structure. So that, for each match (or, more precisely, for each team in each match) we want to append the data related with its position in the classification.