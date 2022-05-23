from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Abre a pagina
navegador = webdriver.Chrome()
navegador.get('https://platform.mangahigh.com/pt-br/login/student')

# Credenciais de login
navegador.execute_script("alert('Realize o login e entre na atividade, pressione enter no terminal')")
time.sleep(5)

user = ''
password = ''
id_school = ''

# Tentativa de fazer o login
try:
    # Usuario
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[1]/div/input').click()
    time.sleep(0.5)
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[1]/div/input').send_keys(user)
    time.sleep(1)

    # Senha
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[2]/div/input').click()
    time.sleep(0.5)
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[2]/div/input').send_keys(password)
    time.sleep(1)

    # Id Escola
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[3]/div/input').click()
    time.sleep(0.5)
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[3]/div/input').send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    time.sleep(0.5)
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[3]/div/input').click()
    time.sleep(0.5)
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[3]/div/input').send_keys(id_school)
    time.sleep(1)

    # Confirma
    navegador.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div/form/div[4]/div/div/p').click()

# Caso não for possivel fazer o login ignora
except:
    pass

# Espera entra na atividade
input('Pressione enter quando estiver dentro da atividade')

# Mostra as respostas
x = 0
for x in range(10):
    input("Pressione enter para ver a resposta")
    time.sleep(0.5)
    navegador.find_element_by_id("main-content").click()
    time.sleep(0.5)
    navegador.execute_script("alert(document.querySelector('#solutions'))")
    time.sleep(0.5)