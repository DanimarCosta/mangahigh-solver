from selenium import webdriver
import time

# Abre a pagina
navegador = webdriver.Chrome()
navegador.get('https://www.mangahigh.com/pt-br/')

# Credenciais de login
user = ''
password = ''
id_school = ''

# Faz o login
navegador.find_element_by_xpath('//*[@id="page-index"]/nav/div[1]/a[1]').click() # login
time.sleep(15)
navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[4]/div/div').click()