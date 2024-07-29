"""from app.service.update.crawler import Crawler
from app.models.Publication import Publication
from app.service.database.publicationDAO import Post

index = Crawler("01/01/2020", "31/01/2020")

links = index.crawler()

print(links)
    

item = Post() 
n = item.post("ifpe", 2020, "Janeiro", links)
print(n)

item = Post()
item.delete("Publications")


index = Crawler("01/01/2020", "31/01/2020")

links = index.crawler() 

n = Publication("ifal", 2018, "Janeiro", links)

from app.service.update.update import UpdateDatabase

UpdateDatabase().update()
print(n.urls)"""

m = 2018
n = {
    "janeiro":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    },
    "fevereiro":{
        "init": f"01/01/{m}",
        "end": f"28/01/{m}"
    },
    "marco":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    },
    "abril":{
        "init": f"01/01/{m}",
        "end": f"30/01/{m}"
    },
    "maio":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    },
    "junho":{
        "init": f"01/01/{m}",
        "end": f"30/01/{m}"
    },
    "julho":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    },
    "agosto":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    },
    "setembro":{
        "init": f"01/01/{m}",
        "end": f"30/01/{m}"
    },
    "outubro":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    },
    "novembro":{
        "init": f"01/01/{m}",
        "end": f"30/01/{m}"
    },
    "dezembro":{
        "init": f"01/01/{m}",
        "end": f"31/01/{m}"
    }
}


"""
print(n["janeiro"]["init"])
for v in n:
    print(v["janeiro"])
    
from app.service.update.update import UpdateDatabase

object = UpdateDatabase()
n = object.update(2018)

print(n)

from app.service.database.publicationDAO import PublicationDAO

item = PublicationDAO()
item.delete("publications_dou")"""

from app.service.update.update import UpdateDatabase

object = UpdateDatabase()
object.update(2018)

