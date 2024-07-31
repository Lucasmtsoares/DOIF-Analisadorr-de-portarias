from app.core.crawler import Crawler

if_uni = "Acre"
if_ = "ifac"
ifs = ["Instituto Federal de Educação, Ciência e Tecnologia do Acre", "Instituto Federal do Acre"]
init = "01/01/2018"
end = "31/01/2018"
n = Crawler(if_, ifs, if_uni, init, end).crawler()

print(n)
    
print(f"Tamanho: {len(n)}")

"""

def urls_filter_clean(urls):
        
        links = list(dict.fromkeys(urls))
        return links


c = ["Lucas", "Jose", "Ifal","Lucas", "Lucas", "Ifal", "Jose", "123"]

n = urls_filter_clean(c)

print(n)

"""