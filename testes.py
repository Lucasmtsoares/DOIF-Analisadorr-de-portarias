"""lista = ['a', 'b', 'a', 'c', 'b']
lista_sem_duplicatas = list(dict.fromkeys(lista))
print(lista_sem_duplicatas)"""

from app.models.Map import Map
from app.core.crawler import Crawler
from app.service.database.publicationDAO import PublicationDAO
from app.models.Publication import Publication
import time
from itertools import zip_longest
"""
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

def repete():
    lista = ['https://www.in.gov.br/web/dou/-/portaria-n-3-069-de-28-de-dezembro-de-2017-1560962', 'https://www.in.gov.br/web/dou/-/portaria-n-1-de-3-de-janeiro-de-2018-1587535', 'https://www.in.gov.br/web/dou/-/portaria-n-3-073-de-28-de-dezembro-de-2017-1608114', 'https://www.in.gov.br/web/dou/-/portaria-n-23-de-4-de-janeiro-de-2018-1652192', 'https://www.in.gov.br/web/dou/-/portaria-n-32-de-5-de-janeiro-de-2018-1652205', 'https://www.in.gov.br/web/dou/-/portaria-n-53-de-9-de-janeiro-de-2018-1706675', 'https://www.in.gov.br/web/dou/-/portaria-n-54-de-9-de-janeiro-de-2018-1706688', 'https://www.in.gov.br/web/dou/-/portaria-n-62-de-9-de-janeiro-de-2018-1706701', 'https://www.in.gov.br/web/dou/-/portaria-n-52-de-9-de-janeiro-de-2018-1735378', 'https://www.in.gov.br/web/dou/-/portaria-n-78-de-11-de-janeiro-de-2018-1816696', 'https://www.in.gov.br/web/dou/-/portaria-n-79-de-11-de-janeiro-de-2018-1816709', 'https://www.in.gov.br/web/dou/-/portaria-n-80-de-11-de-janeiro-de-2018-1816722', 'https://www.in.gov.br/web/dou/-/portaria-n-81-de-11-de-janeiro-de-2018-1816735', 'https://www.in.gov.br/web/dou/-/portaria-n-10-de-4-de-janeiro-de-2018-1819720', 'https://www.in.gov.br/web/dou/-/portaria-n-129-de-18-de-janeiro-de-2018-2047769', 'https://www.in.gov.br/web/dou/-/portarias-de-18-de-janeiro-de-2018-2047782', 'https://www.in.gov.br/web/dou/-/portaria-n-133-de-18-de-janeiro-de-2018-2047795', 'https://www.in.gov.br/web/dou/-/portaria-n-172-de-24-de-janeiro-de-2018-2107818', 'https://www.in.gov.br/web/dou/-/portaria-n-144-de-22-de-janeiro-de-2018-2150616', 'https://www.in.gov.br/web/dou/-/portaria-n-179-de-25-de-janeiro-de-2018-2190788', 'https://www.in.gov.br/web/dou/-/portaria-n-202-de-29-de-janeiro-de-2018-2231008', 'https://www.in.gov.br/web/dou/-/portaria-n-199-de-29-de-janeiro-de-2018-2276483', 'https://www.in.gov.br/web/dou/-/portaria-n-200-de-29-de-janeiro-de-2018-2276496', 'https://www.in.gov.br/web/dou/-/portaria-n-201-de-29-de-janeiro-de-2018-2276509', 'https://www.in.gov.br/web/dou/-/portaria-n-23-de-4-de-janeiro-de-2018-1652192', 'https://www.in.gov.br/web/dou/-/portaria-n-172-de-24-de-janeiro-de-2018-2107818', 'https://www.in.gov.br/web/dou/-/portaria-n-202-de-29-de-janeiro-de-2018-2231008']
    lista_sem_duplicatas = list(dict.fromkeys(lista))
    
    print(f"Tamanho: {len(lista_sem_duplicatas)}")
    
    
repete()

#Forneci 31 urls
#das 31 urls 27 são do ifal
#das 27 urls 24 são unicas!!