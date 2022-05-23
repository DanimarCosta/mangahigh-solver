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
navegador.execute_script('alert("Insira seu login e pressione enter no terminal")')
step = input(':')

#document.querySelector('#solutions')
# Faz a atividade
step = input('Pressione enter: ')
navegador.find_element_by_xpath('//*[@id="question"]/div').click()