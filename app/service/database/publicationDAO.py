from app.models.Connection import Connection
from bson import ObjectId

class PublicationDAO:
    def __init__(self):
        connection = Connection()
        self.client = connection.connection()
        self.db = self.client['publications_dou']
    
    
        
    def create(self, publication):
        collection = self.db[publication.collecion]

        # Construindo o campo a ser adicionado/atualizado
        update = {
            f"months.{publication.months}": {
                "URLs": publication.urls
            }
        }

        # Atualizando o documento existente ou inserindo um novo
        result = collection.update_one(
            {"year": publication.year},
            {"$set": update},
            upsert=True  # Cria um novo documento se não encontrar nenhum correspondente
        )
        
        return result.upserted_id if result.upserted_id else "Documento atualizado"
    def close(self):
        self.client.close()
        
    def read(self):
        collection = self.db["ifac"]
        filter = {"year": 2018}
        month = "Janeiro"
        projection = {f"months.{month}.URLs": 1, "_id": 0}  # Inclui apenas o campo URLs e exclui _id
        document = collection.find_one(filter, projection)
        self.client.close()
        return document
    
    def list(self):
        #self.client = self.get()
        n = self.client.list_database_names()
        self.client.close()
        return n
        
    def delete(self, name):
        self.client.drop_database(name)
        self.client.close()
        
    def delete_doc(self):
        
        colecao = self.db["ifac"]
        id = {"_id": ObjectId("666a8b1886a708d806f6c073")}
        colecao.find_one_and_delete(id)
        self.client.close()
        
    
        
        
        
        