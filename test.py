links = ['https://www.in.gov.br/web/dou/-/portaria-n-2-504-de-9-de-outubro-de-2018-45175799', 
         'https://www.in.gov.br/web/dou/-/portaria-de-24-de-janeiro-de-2018-2108559']



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
from bs4 import BeautifulSoup
import requests
import re

def verificar(links):
    urls = []
    for i in links:
        html = requests.get(i)
        objetct = BeautifulSoup(html.content, 'html.parser')
        orgao = objetct.find("span", class_='orgao-dou-data')
        if orgao:
            orgao_text = orgao.get_text()
            
            if re.search(r'\b' + re.escape("Alagoas") + r'\b', orgao_text):
                urls.append(i)
                
        return urls
    
c = verificar(links)

for b in c:
    print(b)