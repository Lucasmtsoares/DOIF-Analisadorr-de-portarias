from app.service.update.update import UpdateDatabase
year = 2018
instance = UpdateDatabase(year)
instance.update()


"""

from app.service.database.publicationDAO import PublicationDAO

n = PublicationDAO()
n.delete("publications_dou")"""