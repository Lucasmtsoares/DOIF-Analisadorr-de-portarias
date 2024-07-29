from app.core.crawler import Crawler

if_ = "Instituto Federal do Acre"
ifs = ["Instituto Federal de Educação, Ciência e Tecnologia do Acre", "ifac"]
init = "01/01/2018"
end = "31/01/2018"
n = Crawler(if_, ifs, init, end).crawler()

print(n)
    
print(f"Tamanho: {len(n)}")