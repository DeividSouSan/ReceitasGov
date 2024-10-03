import logging
import os
from time import sleep

from selenium.webdriver.common.by import By
from services.bots.download_bot import DownloadBot


class GetPublicRevenueBot(DownloadBot):
    """
    Automação para baixar os dados das receitas fornecidas pelo Portal da Transparência.
    """

    def __init__(self):
        web_url = "https://portaldatransparencia.gov.br/"
        max_time = 2

        super().__init__(web_url, max_time)

    def start(self) -> None:
        """
        Inicia o processo de donwload da receita.
        """
        logging.info(f"Iniciando o bot para baixar os dados da receita em: {self.url}")

        self.clear_download_folder()

        self.driver.get(self.url)

        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[5]/div/div/div[1]/button",
        ).click()

        self.driver.find_element(By.XPATH, "//*[@id='receitas-links']/li[2]/a").click()

        self.driver.find_element(
            By.XPATH, "/html/body/main/div[2]/div/div[2]/div[2]/ul/li[2]/a"
        ).click()

        time_spent = 0
        while self.is_folder_empty():
            sleep(1)
            time_spent += 1

            if time_spent > self.max_time:
                logging.info(
                    f"Tempo máximo de espera atingido. Tempo esperado {self.time_spent} segundos, tempo máximo {self.max_time} segundos."
                )
                break

        if not self.is_folder_empty():
            logging.info("Download concluído com sucesso.")

        self.driver.quit()
