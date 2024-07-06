

class Map:
    def map_ifs(self):
        IFS = ['ifac', 'ifal', 'ifap', 'ifam', 'ifba', 'ifce', 'ifb', 'ifes', 'ifg', 'ifmt', 'ifma', 'ifms', 'ifmg', 'ifpa', 'ifpb', 'ifpr', 'ifpe', 'ifpi', 'ifrj', 'ifrn', 'ifsul', 'ifro', 'ifrr', 'ifsp', 'ifsc', 'ifs', 'ifto']
        
        return IFS
    
    def map_interval(self, year):
        
        year_verificted = verificar(year)
        if year_verificted==False:
            interval = {
                "janeiro":{
                    "init": f"01/01/{year}",
                    "end": f"31/01/{year}"
                },
                "fevereiro":{
                    "init": f"01/02/{year}",
                    "end": f"28/02/{year}"
                },
                "marco":{
                    "init": f"01/03/{year}",
                    "end": f"31/03/{year}"
                },
                "abril":{
                    "init": f"01/04/{year}",
                    "end": f"30/04/{year}"
                },
                "maio":{
                    "init": f"01/05/{year}",
                    "end": f"31/05/{year}"
                },
                "junho":{
                    "init": f"01/06/{year}",
                    "end": f"30/06/{year}"
                },
                "julho":{
                    "init": f"01/07/{year}",
                    "end": f"31/07/{year}"
                },
                "agosto":{
                    "init": f"01/08/{year}",
                    "end": f"31/08/{year}"
                },
                "setembro":{
                    "init": f"01/09/{year}",
                    "end": f"30/09/{year}"
                },
                "outubro":{
                    "init": f"01/10/{year}",
                    "end": f"31/10/{year}"
                },
                "novembro":{
                    "init": f"01/11/{year}",
                    "end": f"30/11/{year}"
                },
                "dezembro":{
                    "init": f"01/12/{year}",
                    "end": f"31/12/{year}"
                }
            }
            
            return interval
        else:
            interval = {
                "janeiro":{
                    "init": f"01/01/{year}",
                    "end": f"31/01/{year}"
                },
                "fevereiro":{
                    "init": f"01/02/{year}",
                    "end": f"29/02/{year}"
                },
                "marco":{
                    "init": f"01/03/{year}",
                    "end": f"31/03/{year}"
                },
                "abril":{
                    "init": f"01/04/{year}",
                    "end": f"30/04/{year}"
                },
                "maio":{
                    "init": f"01/05/{year}",
                    "end": f"31/05/{year}"
                },
                "junho":{
                    "init": f"01/06/{year}",
                    "end": f"30/06/{year}"
                },
                "julho":{
                    "init": f"01/07/{year}",
                    "end": f"31/07/{year}"
                },
                "agosto":{
                    "init": f"01/08/{year}",
                    "end": f"31/08/{year}"
                },
                "setembro":{
                    "init": f"01/09/{year}",
                    "end": f"30/09/{year}"
                },
                "outubro":{
                    "init": f"01/10/{year}",
                    "end": f"31/10/{year}"
                },
                "novembro":{
                    "init": f"01/11/{year}",
                    "end": f"30/11/{year}"
                },
                "dezembro":{
                    "init": f"01/12/{year}",
                    "end": f"31/12/{year}"
                }
            }
            return interval
        
            
            
            
def verificar(ano):
    if ano%4==0:
        if ano%100==0:
            if ano%400==0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False
