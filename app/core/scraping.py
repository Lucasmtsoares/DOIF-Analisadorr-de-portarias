from app.core.crawler import Crawler
from app.models.Publication import Publication
from bs4 import BeautifulSoup as Be
import requests
import re
import time


class Scraping():
    def scraping(self, if_, date):
        date_init = '01/01/2018'
        date_end = '31/12/2018'
        
        
        if date == '2019':
            date_init = '01/01/2019'
            date_end = '31/12/2019'
        elif date == '2020':
            date_init = '01/01/2020'
            date_end = '31/12/2020'
        elif date == '2021':
            date_init = '01/01/2021'
            date_end = '31/12/2021'
        elif date == '2022':
            date_init = '01/01/2022'
            date_end = '31/12/2022'
        elif date == '2023':
            date_init = '01/01/2023'
            date_end = '31/12/2023'
        
        
        #start_time = time.time()
        index = Crawler(date_init, date_end)
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


