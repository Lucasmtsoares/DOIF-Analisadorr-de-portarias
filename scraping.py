
k = ['https://www.in.gov.br/web/dou/-/portaria-n-3-069-de-28-de-dezembro-de-2017-1560962', 'https://www.in.gov.br/web/dou/-/portaria-n-1-de-3-de-janeiro-de-2018-1587535', 'https://www.in.gov.br/web/dou/-/portaria-n-3-073-de-28-de-dezembro-de-2017-1608114', 'https://www.in.gov.br/web/dou/-/portaria-n-23-de-4-de-janeiro-de-2018-1652192','https://www.in.gov.br/web/dou/-/portaria-de-pessoal-ifac-n-531-de-23-de-maio-de-2024-561777094', 'https://www.in.gov.br/web/dou/-/portaria-de-pessoal-ifac-n-546-de-3-de-junho-de-2024-563367158'  ]

from app.core.scraping import Scraping
import re


v = Scraping(k).scraping()
"""
n = "Saia daqui Lucas Matheus Da Silva"

if re.search(r'\b' + re.escape("A") + r'\b', n) or re.search(r'\b' + re.escape("Luca") + r'\b', n) or re.search(r'\b' + re.escape("Salve") + r'\b', n):
    print("Tem sim!!")
else:
    print("Tem NÂO!!")"""