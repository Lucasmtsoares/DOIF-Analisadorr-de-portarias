
k = ["IFAC","IFAL","IFAP","IFAM","IFBA","IF Baiano","IFCE","IFB","IFG","IF Goiano","IFES","IFMA","IFMG","IFNMG","IF Sudeste MG","IFSULDEMINAS","IFTM","IFMT","IFMS","IFPA","IFPB","IFPE","IF Sertão PE","IFPI","IFPR","IFRJ","IFF","IFRN","IFRS","IFFar","IFSUL","IFRO","IFRR","IFSC","IFC","IFSP","IFS","IFTO"
        ]

from app.core.scraping import Scraping
import re
from bs4 import BeautifulSoup
import requests

#v = Scraping("ifal",k).scraping()

print(f"Tamanho: {len(k)}")