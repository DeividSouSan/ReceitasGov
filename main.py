from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from requests import Request
from time import sleep
from datetime import datetime

data = {
    "author": "Deivid Souza Santana",
    "date": datetime.now().date().isoformat()
}

driver = Chrome()
driver.get("https://portaldatransparencia.gov.br/")

desp_receitas = driver.find_element(By.ID, 'despesas-card')
desp_receitas.click()

while True:
    pass