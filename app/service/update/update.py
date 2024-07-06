from app.models.Map import Map
from app.service.update.crawler import Crawler
from app.service.database.publicationDAO import PublicationDAO
from app.models.Publication import Publication
import time


class UpdateDatabase:
    def __init__(self):
        print("Salve!!")
        
    def update(self, year):
        print("Iniciando atualização...")
        all_ifs = Map().map_ifs()
        interval = Map().map_interval(year)
        create_publication = PublicationDAO()
        for ifs in all_ifs:
            for n, i in interval.items():
                print(f"Lista {ifs} >")
                indexs = Crawler(i["init"], i["end"], ifs).crawler()
                
                publication = Publication(ifs, year, n, indexs)
                result = create_publication.create(publication)
                print(result)
        create_publication.close()      
            