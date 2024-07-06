from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Configurando o driver do Selenium

class Crawler():
    def __init__(self, init, end, name_if):
      self.init = init
      self.end = end
      self.name_if = name_if
      
    def crawler(self):
      options = webdriver.ChromeOptions()
      options.add_argument('--headless')
      service = Service(ChromeDriverManager().install())
      driver = webdriver.Chrome(service=service, options=options)

    
      try:
            
            all_links = []
            
            url = 'https://www.in.gov.br/acesso-a-informacao/dados-abertos/base-de-dados'
            driver.get(url)

            input_text = driver.find_element(By.CSS_SELECTOR, 'input#search-bar')
            input_text.send_keys(self.name_if)

            # Encontrando o botão "toggle-search-advanced" e clicando nele
            button_advance = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a#toggle-search-advanced'))
            )
            button_advance.click()

            # Tipo de resultado
            result_exact = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#tipo-pesquisa-1'))
            )
            result_exact.click()

            #ato
            

            # Seção de busca
            section_dou = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#do2'))
            )
            section_dou.click()

            # Edição
            ediction = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#personalizado'))
            )
            ediction.click()
            #periodo
            periodo_init = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'data-inicio'))
            )
            #data_inicio = datetime.strptime('01/12/2023', '%d/%m/%Y')

            # Limpando o campo e enviando a nova data
            driver.execute_script(f"arguments[0].value = '{self.init}';", periodo_init)
            #periodo_init.send_keys(data_inicio.strftime('%d/%m/%Y'))
            
            

            periodo_end = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'data-fim'))
            )
            #data_fim = datetime.strptime('28/12/2023', '%d/%m/%Y')

            # Limpando o campo e enviando a nova data
            driver.execute_script(f"arguments[0].value = '{self.end}';", periodo_end)
            #periodo_end.send_keys(data_fim.strftime('%d/%m/%Y'))

            # Buscar conteúdo
            search = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button'))
            )
            search.click()

            # Aguardar a navegação
            WebDriverWait(driver, 10).until(EC.url_changes(url))

            

            while url:
                link_elements = driver.find_elements(By.CSS_SELECTOR, 'h5.title-marker a')

                links = [element.get_attribute('href') for element in link_elements]
                links = [link for link in links if link]
                

                all_links.extend(links)
                
                

                proximo = driver.find_element(By.CSS_SELECTOR, 'button#rightArrow')
                is_disabled = proximo.get_attribute('disabled')

                if is_disabled:
                    url = None
                else:
                    ActionChains(driver).click(proximo).perform()
                    WebDriverWait(driver, 10).until(EC.url_changes(url))

                    
            all_links.reverse()
            return all_links

      except Exception as error:
        print("Erro exception", error)
      finally:
        driver.quit()
        
        
