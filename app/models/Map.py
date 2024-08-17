class Map:
    def __init__(self):
        self.ifs_acronimo = ["IFAC","IFAL","IFAP","IFAM","IFBA","IF Baiano","IFCE","IFB","IFG","IF Goiano","IFES","IFMA","IFMG","IFNMG","IF Sudeste MG","IFSULDEMINAS","IFTM","IFMT","IFMS","IFPA","IFPB","IFPE","IF Sertão PE","IFPI","IFPR","IFRJ","IFF","IFRN","IFRS","IFFar","IFSUL","IFRO","IFRR","IFSC","IFC","IFSP","IFS","IFTO"
        ]
        
        self.ifs_extenso = [
        "Instituto Federal de Educação, Ciência e Tecnologia do Acre","Instituto Federal de Educação, Ciência e Tecnologia de Alagoas","Instituto Federal de Educação, Ciência e Tecnologia do Amapá","Instituto Federal de Educação, Ciência e Tecnologia do Amazonas","Instituto Federal de Educação, Ciência e Tecnologia da Bahia","Instituto Federal de Educação, Ciência e Tecnologia Baiano","Instituto Federal de Educação, Ciência e Tecnologia do Ceará","Instituto Federal de Educação, Ciência e Tecnologia de Brasília","Instituto Federal de Educação, Ciência e Tecnologia de Goiás", "Instituto Federal de Educação, Ciência e Tecnologia Goiano","Instituto Federal de Educação, Ciência e Tecnologia do Espírito Santo","Instituto Federal de Educação, Ciência e Tecnologia do Maranhão","Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais","Instituto Federal de Educação, Ciência e Tecnologia do Norte de Minas Gerais","Instituto Federal de Educação, Ciência e Tecnologia do Sudeste de Minas Gerais","Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais","Instituto Federal de Educação, Ciência e Tecnologia do Triângulo Mineiro",
        "Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso","Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso do Sul","Instituto Federal de Educação, Ciência e Tecnologia do Pará","Instituto Federal de Educação, Ciência e Tecnologia da Paraíba","Instituto Federal de Educação, Ciência e Tecnologia de Pernambuco","Instituto Federal de Educação, Ciência e Tecnologia do Sertão Pernambucano", "Instituto Federal de Educação, Ciência e Tecnologia do Piauí","Instituto Federal de Educação, Ciência e Tecnologia do Paraná","Instituto Federal de Educação, Ciência e Tecnologia do Rio de Janeiro","Instituto Federal de Educação, Ciência e Tecnologia Fluminense","Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte","Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Sul","Instituto Federal de Educação, Ciência e Tecnologia Farroupilha","Instituto Federal de Educação, Ciência e Tecnologia Sul-rio-grandense","Instituto Federal de Educação, Ciência e Tecnologia de Rondônia","Instituto Federal de Educação, Ciência e Tecnologia de Roraima","Instituto Federal de Educação, Ciência e Tecnologia de Santa Catarina","Instituto Federal de Educação, Ciência e Tecnologia Catarinense","Instituto Federal de Educação, Ciência e Tecnologia de São Paulo","Instituto Federal de Educação, Ciência e Tecnologia de Sergipe","Instituto Federal de Educação, Ciência e Tecnologia do Tocantins"
         ]
        
        self.ifs_extenso_lim = ["Instituto Federal do Acre","Instituto Federal de Alagoas","Instituto Federal do Amapá","Instituto Federal do Amazonas","Instituto Federal da Bahia","Instituto Federal Baiano","Instituto Federal do Ceará","Instituto Federal de Brasília","Instituto Federal de Goiás","Instituto Federal Goiano","Instituto Federal do Espírito Santo","Instituto Federal do Maranhão","Instituto Federal de Minas Gerais","Instituto Federal do Norte de Minas Gerais","Instituto Federal do Sudeste de Minas Gerais","Instituto Federal do Sul de Minas Gerais","Instituto Federal do Triângulo Mineiro","Instituto Federal de Mato Grosso","Instituto Federal de Mato Grosso do Sul","Instituto Federal do Pará","Instituto Federal da Paraíba","Instituto Federal de Pernambuco","Instituto Federal do Sertão Pernambucano","Instituto Federal do Piauí","Instituto Federal do Paraná","Instituto Federal do Rio de Janeiro","Instituto Federal Fluminense","Instituto Federal do Rio Grande do Norte","Instituto Federal do Rio Grande do Sul","Instituto Federal Farroupilha","Instituto Federal Sul-rio-grandense","Instituto Federal de Rondônia","Instituto Federal de Roraima","Instituto Federal de Santa Catarina","Instituto Federal Catarinense","Instituto Federal de São Paulo","Instituto Federal de Sergipe","Instituto Federal do Tocantins"
        ]
        
        self.ifs_federacao = ["Acre","Alagoas","Amapá","Amazonas","Bahia","Baiano","Ceará","Brasília","Goiás","Goiano","Espírito Santo","Maranhão","Minas Gerais","Norte de Minas Gerais","Sudeste de Minas Gerais","Sul de Minas Gerais","Triângulo Mineiro","Mato Grosso","Mato Grosso do Sul","Pará","Paraíba","Pernambuco","Sertão Pernambucano","Piauí","Paraná","Rio de Janeiro","Fluminense","Rio Grande do Norte","Rio Grande do Sul","Farroupilha","Sul-rio-grandense","Rondônia","Roraima","Santa Catarina","Catarinense","São Paulo","Sergipe","Tocantins"
        ]
    def map_ifs_acronimo(self):        
        return self.ifs_acronimo
    
    def map_ifs_extenso(self):
        return self.ifs_extenso

    def map_ifs_extenso_lim(self):
        return self.ifs_extenso_lim
        
    def map_ifs_federacao(self):        
        return self.ifs_federacao
    
    def map_interval(self, year):
        
        year_verificted = self.verificar(year)
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
    def verificar(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
       
        
#if baiano, if sertao pe, ifg, ifpb, 
            
            

