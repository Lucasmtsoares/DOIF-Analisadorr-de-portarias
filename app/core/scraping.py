"""from app.core.crawler import Crawler
from app.models.Portaria import Portaria
from bs4 import BeautifulSoup as Be
import requests
import re
import time


class Scraping():
    def scraping(self, if_, date):
        
        
        
        #start_time = time.time()
        index = Crawler()
        links = index.crawler()
        
        #end_time = time.time()
        #execution_time = end_time - start_time
        ato = ['NOMEAR', 'Nomear', 'Nomeou']
        ato2 = ['EXONERAR', 'Exonerar', 'Exonerou']
        nomeacoes = []
        exoneracoes = []
        outros = []
        
        publications = []

        for url in links:
            #for url in link:
                html = requests.get(url, timeout=20)
                soup = Be(html.content, 'html.parser')
                
                #type = soup.find()
                if_ = soup.find('span', class_='orgao-dou-data')
                content = soup.find('div', class_='texto-dou')
                concierge = soup.find('p', class_='identifica')
                date = soup.find('span', class_='publicado-dou-data')
                responsible = soup.find('p', class_='assina')
                
                if if_ is not None:
                    if_ = if_.text
                else:
                    if_ = "N/A"
                
                if content is not None:
                    content = content.text
                else:
                    content = "N/A"
                
                if concierge is not None:
                    concierge = concierge.text
                else:
                    concierge = "N/A"
                
                if date is not None:
                    date = date.text
                else:
                    date = "N/A"
                    
                if responsible is not None:
                    responsible = responsible.text
                else:
                    responsible = "N/A"
                publication_instance = Publication("tipo", if_, content, concierge, date, responsible)

                nomeacao_encontrada = False
                exoneracao_encontrada = False

                for termo in ato:
                    if re.search(r'\b' + termo + r'\b', publication_instance.content):
                        publication = Publication("Nomeacoes", publication_instance.if_, publication_instance.content, publication_instance.concierge, publication_instance.date, publication_instance.responsible)
                        publications.append(publication)
                        
                        nomeacoes.append(url)
                        nomeacao_encontrada = True
                        break

                if not nomeacao_encontrada:
                    for ex in ato2:
                        if re.search(r'\b' + ex + r'\b', publication_instance.content):
                            publication = Publication("Exoneracoes", publication_instance.if_, publication_instance.content, publication_instance.concierge, publication_instance.date, publication_instance.responsible)
                            publications.append(publication)
                            
                            exoneracoes.append(url)
                            exoneracao_encontrada = True
                            break

                if not nomeacao_encontrada and not exoneracao_encontrada:
                    publication = Publication("Outros", publication_instance.if_, publication_instance.content, publication_instance.concierge, publication_instance.date, publication_instance.responsible)
                    publications.append(publication)
                    outros.append(url)

    
        return publications


"""
k = ['https://www.in.gov.br/web/dou/-/portaria-n-3-069-de-28-de-dezembro-de-2017-1560962', 'https://www.in.gov.br/web/dou/-/portaria-n-1-de-3-de-janeiro-de-2018-1587535', 'https://www.in.gov.br/web/dou/-/portaria-n-3-073-de-28-de-dezembro-de-2017-1608114', 'https://www.in.gov.br/web/dou/-/portaria-n-23-de-4-de-janeiro-de-2018-1652192',  ]

from app.models.Publication import Publication
import time
from bs4 import BeautifulSoup
import requests
import re

year = 2018
class Scraping:
    def __init__(self, urls):
        #self.collecion = collecion
        self.urls = urls
        
    def scraping(self):
        print("Iniciando extracao...")
        for url in self.urls:
            html = requests.get(url, timeout=10)
            beautifulSoup = BeautifulSoup(html.content, 'html.parser')
            #if_collecion = self.collecion
            
            date = beautifulSoup.find('span', class_='publicado-dou-data').get_text()
            orgao = beautifulSoup.find('span', class_='orgao-dou-data').get_text()
            concierge = beautifulSoup.find('p', class_='identifica') #erro
            if not concierge:
                txt = beautifulSoup.find('h3', class_='titulo-dou')
                concierge = txt.find('span').get_text()
            content = beautifulSoup.find('div', class_='texto-dou').get_text()
            responsible = beautifulSoup.find('p', class_='assina').get_text()
            type = self.indentify_type(content=content)
            #publication = Publication()
            print(f'Objetos: {type,concierge, date, responsible}')
        
       
                
    def indentify_type(self, content):
        nomecao = re.compile(r'\b(NOMEAR|Nomear|nomear|NOMEIA|Nomeia|nomeia)\b')
        exoneracao = re.compile(r'\b(EXONERAR|Exonerar|exonerar|EXONERA|Exonera|exonera)\b')
        autorizar = re.compile(r'\b(AUTORIZAR)\b')
        
        #verificação
        if nomecao.search(content):
            return "Nomeação"
        elif exoneracao.search(content):
            return "Exoneração"
        elif autorizar.search(content):
            return "Autorizar"
        else:
            return "Outro"
        
   