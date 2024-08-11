#teste isolado de funcionamento

k = ['https://www.in.gov.br/web/dou/-/portaria-de-pessoal-ifac-n-807-de-7-de-agosto-de-2024-577100534', 'https://www.in.gov.br/web/dou/-/portaria-de-pessoal-ifac-n-806-de-7-de-agosto-de-2024-577078832','https://www.in.gov.br/web/dou/-/portaria-de-pessoal-ifac-n-805-de-7-de-agosto-de-2024-577068173','https://www.in.gov.br/web/dou/-/portaria-de-pessoal-ifac-n-806-de-7-de-agosto-de-2024-577078832','https://www.in.gov.br/en/web/dou/-/portarias-de-25-de-julho-de-2024-574779018','https://www.in.gov.br/web/dou/-/retificacao-1647421']

print(f"Tamanho -> {len(k)}")
import re
import requests
from bs4 import BeautifulSoup

def filter_result(if_federacao, urls):
        urls_all = []
        for link in urls:
            try:
                html = requests.get(link)
                html.raise_for_status()
                objetct = BeautifulSoup(html.content, 'html.parser')
                orgao = objetct.find("span", class_='orgao-dou-data')
                
                if orgao:
                    orgao_text = orgao.get_text()
                    if re.search(r'\b' + re.escape(if_federacao) + r'\b', orgao_text) or \
                       re.search(r'\bReitoria\b', orgao_text) or \
                       re.search(r'\bGabinete\b', orgao_text):
                       urls_all.append(link)
                       print(f"Valido -> {link}")
                    else:
                        print(f'Invalido -> {link}')
            except requests.RequestException as e:
                print(f"Erro ao fazer a requisição!!")
            except Exception as e:
                print("Erro ao processar o link")
        return urls_all

def filter(if_federacao, urls):
    urls_all = []
    for link in urls:
        try:
            # Realiza a requisição HTTP
            html = requests.get(link)
            html.raise_for_status()  # Levanta uma exceção para status de erro HTTP
            beautifulSoup = BeautifulSoup(html.content, 'html.parser')
            
            # Localiza o órgão e a concierge no HTML
            orgao = beautifulSoup.find("span", class_='orgao-dou-data')
            concierge = beautifulSoup.find('p', class_='identifica')
            
            if concierge:
                concierge_text = concierge.get_text()
            else:
                concierge = beautifulSoup.find('h3', class_='titulo-dou')
                concierge_text = concierge.find('span').get_text()
            print(f'ESSA aqui -> {concierge_text}')
            
            # Verifica se a palavra "RETIFICAÇÂO" não está no texto de concierge
            if not re.search(r'\b' + re.escape("RETIFICAÇÃO") + r'\b', concierge_text):
                                            
                orgao_text = orgao.get_text()
                # Verifica se alguma das palavras desejadas está no texto de orgao
                if (re.search(r'\b' + re.escape(if_federacao) + r'\b', orgao_text) or
                    re.search(r'\bReitoria\b', orgao_text) or
                    re.search(r'\bGabinete\b', orgao_text)):
                    
                    urls_all.append(link)

        except requests.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")
        except Exception as e:
            print(f"Erro ao processar o link: {e}")
    
    return urls_all


def urls_filter_clean(urls):
        return list(dict.fromkeys(urls))



m = filter("Acre",k)
print(f"Filtro -> {len(m)}")
for p in m:
    print(f'Filter -> {p}')
    
j = urls_filter_clean(m)
print(f'Sem repetição -> {len(j)}')

for t in j:
        print(t)
        
"""       
frase = "Lucas Silva"

if not re.search(r'\b' + re.escape("RETIFICAÇÂO") + r'\b', frase):
        print("TRUE")
else:
    print("FALSE!")"""