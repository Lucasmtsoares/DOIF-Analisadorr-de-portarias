from api.core.scraping import Scraping
from datetime import datetime
from collections import defaultdict
from collections import Counter

class Analitic:
    def analitic(self):
        instance_scraping = Scraping()
        publications = instance_scraping.scraping()

        # Dicionário para armazenar as publicações por tipo e mês
        publications_by_type_and_month = defaultdict(lambda: defaultdict(list))
        for publication in publications:
            date_obj = datetime.strptime(publication.date, "%d/%m/%Y")
            month = date_obj.strftime("%B")
            publications_by_type_and_month[month][publication.type].append(publication)
            
        print("Contagem parcial:")
        for month, types_and_publications in publications_by_type_and_month.items():
            print(f"Month: {month}")
            for pub_type, publications_list in types_and_publications.items():
                print(f"  {pub_type}: {len(publications_list)}")

        # Dicionário final com contagem por tipo e mês
        result = defaultdict(dict)

        # Dicionário para mapear tipos de publicações para chaves
        type_map = {
            'Nomeacoes': 'Nomeacoes',
            'Exoneracoes': 'Exoneracoes',
            'Outros': 'Outros',
        }

        # Inicializar o dicionário counter
        counter = Counter({'Nomeacoes': 0,'Exoneracoes': 0, 'Outros': 0})

        for month, types_and_publications in publications_by_type_and_month.items():
            for pub_type, publications_list in types_and_publications.items():
                counter[type_map[pub_type]] = len(publications_list)

            result[month] = dict(counter)

        # Exibir ou retornar o resultado conforme necessário
        return dict(result)




"""from app.core.scraping import Scraping
from datetime import datetime
from collections import defaultdict

# ...



class Analitic:
        
    def analitic(self):
        instance_scraping = Scraping()
        publications = instance_scraping.scraping()
        # Dicionário para armazenar as publicações por tipo e mês
        publications_by_type_and_month = defaultdict(lambda: defaultdict(list))

        for publication in publications:
            date_obj = datetime.strptime(publication.date, "%d/%m/%Y")
            month = date_obj.strftime("%B")
            publications_by_type_and_month[month][publication.type].append(publication)
            print(f">> Added publication to >>>>>>> {month} - {publication.type}")
        # Dicionário final com contagem por tipo e mês
        
        print("Contagem parcial:")
        for month, types_and_publications in publications_by_type_and_month.items():
            print(f"Month: {month}")
            for pub_type, publications_list in types_and_publications.items():
                print(f"  {pub_type}: {len(publications_list)}")

        result = defaultdict(dict)
    
        # Preencher o dicionário final
        for month, types_and_publications in publications_by_type_and_month.items():
            
            result[month] = {
                'Nomeacoes': len(types_and_publications.get('Nomeacoes', [])),
                'Exoneracoes': len(types_and_publications.get('Exoneracoes', [])),
                'Outros': len(types_and_publications.get('Outros', [])),
            }

        # Exibir ou retornar o resultado conforme necessário
        return dict(result)
"""