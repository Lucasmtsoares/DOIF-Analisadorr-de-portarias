"""lista = ['a', 'b', 'a', 'c', 'b']
lista_sem_duplicatas = list(dict.fromkeys(lista))
print(lista_sem_duplicatas)"""

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
        self.ifs_ex = Map().map_ifs_extenso()
        self.ifs_ex_lim = Map().map_ifs_extenso_lim()
        self.interval = Map().map_interval(self.year)
        print("Salve!!")
        
    def update(self):
        print("Iniciando atualização...")
        
        for v,interv in self.interval.items():
            for n,(ifs_acr, ifs_ex, ifs_ex_lim) in enumerate(zip_longest(self.ifs_acr, self.ifs_ex, self.ifs_ex_lim)):
                instancia = ifs_acr
                if instancia:
                    print(instancia)
                    
                    #print(f"Lista {ifs} >")
                    indexs = Crawler(interv["init"], interv["end"], instancia).crawler()
                    t = len(indexs)
                    print(len(indexs))
                    break
                    #publication = Publication(ifs, year, n, indexs)
                
                
           
ob = UpdateDatabase(year).update()



"""


"""