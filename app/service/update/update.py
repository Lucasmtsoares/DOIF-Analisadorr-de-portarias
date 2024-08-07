from app.models.Map import Map
from app.core.crawler import Crawler
from app.service.database.publicationDAO import PublicationDAO
from app.models.Publication import Publication
import time
from itertools import zip_longest

year = 2018
class UpdateDatabase:
    def __init__(self, year):
        self.year = year
        self.ifs_acr = Map().map_ifs_acronimo()
        self.ifs_add = [Map().map_ifs_extenso(), Map().map_ifs_extenso_lim()]
        self.if_fereacao = Map().map_ifs_federacao()
        self.interval = Map().map_interval(self.year)
        print("Salve!!")
        
    def update(self):
        print("Iniciando atualização...")
        
        for v,interv in self.interval.items():
            for n,(ifs_acr, ifs_add, if_federacao) in enumerate(zip_longest(self.ifs_acr, self.ifs_add, self.if_fereacao)):
                instancia = ifs_acr
                if instancia:
                    print(instancia)
                    
                    #print(f"Lista {ifs} >")
                    indexs = Crawler(ifs_acr, ifs_add, if_federacao, interv["init"], interv["end"]).crawler()
                    t = len(indexs)
                    print(len(indexs))
                    break
                    #publication = Publication(ifs, year, n, indexs)
                
                
           
ob = UpdateDatabase(year).update()

