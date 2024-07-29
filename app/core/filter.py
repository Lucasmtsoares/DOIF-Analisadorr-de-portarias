from app.models.Map import Map
from app.core.crawler import Crawler
class Filter:
    def __init__(self, year):
        self.ifs_acronimo = Map().map_ifs_acronimo()
        self.ifs_extenso = Map().map_ifs_extenso()
        self.ifs_estenso_lim = Map().map_ifs_extenso_lim()
        self.interval = Map().map_interval(year)
        
        
    def result_crawler(self):
        urls = []
        for instituto in self.ifs_acronimo:
            crawler = Crawler()