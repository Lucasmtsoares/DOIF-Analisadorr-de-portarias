

institutos_federais = [
    "Instituto Federal de Educação, Ciência e Tecnologia do Acre",
    "Instituto Federal de Educação, Ciência e Tecnologia de Alagoas",
    "Instituto Federal de Educação, Ciência e Tecnologia do Amapá",
    "Instituto Federal de Educação, Ciência e Tecnologia do Amazonas",
    "Instituto Federal de Educação, Ciência e Tecnologia da Bahia",
    "Instituto Federal de Educação, Ciência e Tecnologia Baiano",
    "Instituto Federal de Educação, Ciência e Tecnologia do Ceará",
    "Instituto Federal de Educação, Ciência e Tecnologia de Brasília",
    "Instituto Federal de Educação, Ciência e Tecnologia de Goiás",
    "Instituto Federal de Educação, Ciência e Tecnologia Goiano",
    "Instituto Federal de Educação, Ciência e Tecnologia do Espírito Santo",
    "Instituto Federal de Educação, Ciência e Tecnologia do Maranhão",
    "Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais",
    "Instituto Federal de Educação, Ciência e Tecnologia do Norte de Minas Gerais",
    "Instituto Federal de Educação, Ciência e Tecnologia do Sudeste de Minas Gerais",
    "Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais",
    "Instituto Federal de Educação, Ciência e Tecnologia do Triângulo Mineiro",
    "Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso",
    "Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso do Sul",
    "Instituto Federal de Educação, Ciência e Tecnologia do Pará",
    "Instituto Federal de Educação, Ciência e Tecnologia da Paraíba",
    "Instituto Federal de Educação, Ciência e Tecnologia de Pernambuco",
    "Instituto Federal de Educação, Ciência e Tecnologia do Sertão Pernambucano",
    "Instituto Federal de Educação, Ciência e Tecnologia do Piauí",
    "Instituto Federal de Educação, Ciência e Tecnologia do Paraná",
    "Instituto Federal de Educação, Ciência e Tecnologia do Rio de Janeiro",
    "Instituto Federal de Educação, Ciência e Tecnologia Fluminense",
    "Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte",
    "Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Sul",
    "Instituto Federal de Educação, Ciência e Tecnologia Farroupilha",
    "Instituto Federal de Educação, Ciência e Tecnologia Sul-rio-grandense",
    "Instituto Federal de Educação, Ciência e Tecnologia de Rondônia",
    "Instituto Federal de Educação, Ciência e Tecnologia de Roraima",
    "Instituto Federal de Educação, Ciência e Tecnologia de Santa Catarina",
    "Instituto Federal de Educação, Ciência e Tecnologia Catarinense",
    "Instituto Federal de Educação, Ciência e Tecnologia de São Paulo",
    "Instituto Federal de Educação, Ciência e Tecnologia de Sergipe",
    "Instituto Federal de Educação, Ciência e Tecnologia do Tocantins"
]

institutos_federais2 = ["Instituto Federal do Acre","Instituto Federal de Alagoas","Instituto Federal do Amapá","Instituto Federal do Amazonas","Instituto Federal da Bahia","Instituto Federal Baiano","Instituto Federal do Ceará","Instituto Federal de Brasília","Instituto Federal de Goiás","Instituto Federal Goiano","Instituto Federal do Espírito Santo","Instituto Federal do Maranhão","Instituto Federal de Minas Gerais","Instituto Federal do Norte de Minas Gerais","Instituto Federal do Sudeste de Minas Gerais","Instituto Federal do Sul de Minas Gerais","Instituto Federal do Triângulo Mineiro","Instituto Federal de Mato Grosso","Instituto Federal de Mato Grosso do Sul","Instituto Federal do Pará","Instituto Federal da Paraíba","Instituto Federal de Pernambuco","Instituto Federal do Sertão Pernambucano","Instituto Federal do Piauí","Instituto Federal do Paraná","Instituto Federal do Rio de Janeiro","Instituto Federal Fluminense","Instituto Federal do Rio Grande do Norte","Instituto Federal do Rio Grande do Sul","Instituto Federal Farroupilha","Instituto Federal Sul-rio-grandense","Instituto Federal de Rondônia","Instituto Federal de Roraima","Instituto Federal de Santa Catarina","Instituto Federal Catarinense","Instituto Federal de São Paulo","Instituto Federal de Sergipe","Instituto Federal do Tocantins"
]

institutos_federais3 = ["Acre","Alagoas","Amapá","Amazonas","Bahia","Baiano","Ceará","Brasília","Goiás","Goiano","Espírito Santo","Maranhão","Minas Gerais","Norte de Minas Gerais","Sudeste de Minas Gerais","Sul de Minas Gerais","Triângulo Mineiro","Mato Grosso","Mato Grosso do Sul","Pará","Paraíba","Pernambuco","Sertão Pernambucano","Piauí","Paraná","Rio de Janeiro","Fluminense","Rio Grande do Norte","Rio Grande do Sul","Farroupilha","Sul-rio-grandense","Rondônia","Roraima","Santa Catarina","Catarinense","São Paulo","Sergipe","Tocantins"
]


institutos_federais4 = ["IFAC","IFAL","IFAP","IFAM","IFBA","IF Baiano","IFCE","IFB","IFG","IF Goiano","IFES","IFMA","IFMG","IFNMG","IF Sudeste MG","IFSULDEMINAS","IFTM","IFMT","IFMS","IFPA","IFPB","IFPE","IF Sertão PE","IFPI","IFPR","IFRJ","IFF","IFRN","IFRS","IFFar","IFSUL","IFRO","IFRR","IFSC","IFC","IFSP","IFS","IFTO"
]


v = "Pernambuco"
x = "Reitoria"
from bs4 import BeautifulSoup
import requests
import re

from bs4 import BeautifulSoup
import requests
import re

# Lista de links para verificar
k = ['https://www.in.gov.br/web/dou/-/portaria-n-3-069-de-28-de-dezembro-de-2017-1560962', 'https://www.in.gov.br/web/dou/-/portaria-n-1-de-3-de-janeiro-de-2018-1587535', 'https://www.in.gov.br/web/dou/-/portaria-n-3-073-de-28-de-dezembro-de-2017-1608114', 'https://www.in.gov.br/web/dou/-/portaria-n-23-de-4-de-janeiro-de-2018-1652192', 'https://www.in.gov.br/web/dou/-/portaria-n-32-de-5-de-janeiro-de-2018-1652205', 'https://www.in.gov.br/web/dou/-/portaria-n-53-de-9-de-janeiro-de-2018-1706675', 'https://www.in.gov.br/web/dou/-/portaria-n-54-de-9-de-janeiro-de-2018-1706688', 'https://www.in.gov.br/web/dou/-/portaria-n-62-de-9-de-janeiro-de-2018-1706701', 'https://www.in.gov.br/web/dou/-/portaria-n-52-de-9-de-janeiro-de-2018-1735378', 'https://www.in.gov.br/web/dou/-/portaria-n-78-de-11-de-janeiro-de-2018-1816696', 'https://www.in.gov.br/web/dou/-/portaria-n-79-de-11-de-janeiro-de-2018-1816709', 'https://www.in.gov.br/web/dou/-/portaria-n-80-de-11-de-janeiro-de-2018-1816722', 'https://www.in.gov.br/web/dou/-/portaria-n-81-de-11-de-janeiro-de-2018-1816735', 'https://www.in.gov.br/web/dou/-/portaria-n-10-de-4-de-janeiro-de-2018-1819720', 'https://www.in.gov.br/web/dou/-/portaria-n-129-de-18-de-janeiro-de-2018-2047769', 'https://www.in.gov.br/web/dou/-/portarias-de-18-de-janeiro-de-2018-2047782', 'https://www.in.gov.br/web/dou/-/portaria-n-133-de-18-de-janeiro-de-2018-2047795', 'https://www.in.gov.br/web/dou/-/portaria-n-172-de-24-de-janeiro-de-2018-2107818', 'https://www.in.gov.br/web/dou/-/portaria-n-144-de-22-de-janeiro-de-2018-2150616', 'https://www.in.gov.br/web/dou/-/portaria-n-179-de-25-de-janeiro-de-2018-2190788', 'https://www.in.gov.br/web/dou/-/portaria-n-202-de-29-de-janeiro-de-2018-2231008', 'https://www.in.gov.br/web/dou/-/portaria-n-199-de-29-de-janeiro-de-2018-2276483', 'https://www.in.gov.br/web/dou/-/portaria-n-200-de-29-de-janeiro-de-2018-2276496', 'https://www.in.gov.br/web/dou/-/portaria-n-201-de-29-de-janeiro-de-2018-2276509', 'https://www.in.gov.br/web/dou/-/portarias-de-12-de-janeiro-de-2018-1821692', 'https://www.in.gov.br/web/dou/-/portaria-de-24-de-janeiro-de-2018-2108559', 'https://www.in.gov.br/web/dou/-/portarias-de-29-de-janeiro-de-2018-2233584', 'https://www.in.gov.br/web/dou/-/portaria-n-23-de-4-de-janeiro-de-2018-1652192', 'https://www.in.gov.br/web/dou/-/portaria-n-172-de-24-de-janeiro-de-2018-2107818', 'https://www.in.gov.br/web/dou/-/portaria-de-24-de-janeiro-de-2018-2108559', 'https://www.in.gov.br/web/dou/-/portaria-n-202-de-29-de-janeiro-de-2018-2231008']



# Variáveis de verificação
v = "Alagoas"
palavras = ["Reitoria", "Gabinete"]

def verificar(v, links):
        urls_all = []
        for link in links:
            try:
                html = requests.get(link)
                html.raise_for_status()
                objetct = BeautifulSoup(html.content, 'html.parser')
                orgao = objetct.find("span", class_='orgao-dou-data')
                
                if orgao:
                    orgao_text = orgao.get_text()
                    if re.search(r'\b' + re.escape(v) + r'\b', orgao_text) or \
                       re.search(r'\bReitoria\b', orgao_text) or \
                       re.search(r'\bGabinete\b', orgao_text):
                        urls_all.append(link)
            except requests.RequestException as e:
                print(f"Erro ao fazer a requisição!!")
            except Exception as e:
                print("Erro ao processar o link")
        
        return urls_all

# Chamando a função e imprimindo os links que atendem ao critério
c = verificar(v,k)

print(c)
    
print(f"Tamanho oi: {len(c)}")
print(f"Tamanho oiiii: {len(k)}")