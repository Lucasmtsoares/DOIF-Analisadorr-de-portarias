TEM = "https://www.in.gov.br/web/dou/-/portaria-n-2-504-de-9-de-outubro-de-2018-45175799"
NTEM = "https://www.in.gov.br/web/dou/-/portaria-de-24-de-janeiro-de-2018-2108559"

from bs4 import BeautifulSoup
import requests

def verificar(link):
    html = requests.get(link)
    objetct = BeautifulSoup(html.content, 'html.parser')
    div = objetct.find("div")
    print(div)
    
    
verificar(TEM)