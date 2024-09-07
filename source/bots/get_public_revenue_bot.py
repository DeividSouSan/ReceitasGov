import logging
import os
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class GetPublicRevenueBot:
    """
    Automação para baixar os dados das receitas fornecidas pelo Portal da Transparência.
    """

    def __init__(self, web_url: str, max_time: int):
        self.url = web_url
        self.donwload_folder = os.path.join(os.getcwd(), "source/data/csv")

        if not os.path.exists(self.donwload_folder):
            os.mkdir(self.donwload_folder)

        # Wait time related
        self.max_time = max_time
        self.time_spent = 0

        chrome_options = ChromeOptions()
        prefs = {"download.default_directory": self.donwload_folder}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")

        self.driver = Chrome(options=chrome_options)

    def is_folder_empty(self):
        files = len(os.listdir(self.donwload_folder))
        result = not bool(files)

        logging.info(f"Verificando se a pasta de downloads está vazia: {result}")

        return result

    def clear_download_folder(self) -> None:
        """
        Limpa a pasta de downloads (csv) se ela não estiver vazia.
        """

        if not self.is_folder_empty():
            for file in os.listdir(self.donwload_folder):
                os.remove(os.path.join(self.donwload_folder, file))

        logging.info(
            f"Pasta de downloads limpa: {self.donwload_folder} tem {len(os.listdir(self.donwload_folder))} arquivo(s)."
        )

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

        while self.is_folder_empty():
            sleep(1)
            self.time_spent += 1

            if self.time_spent > self.max_time:
                logging.info(
                    f"Tempo máximo de espera atingido. Tempo esperado {self.time_spent} segundos, tempo máximo {self.max_time} segundos."
                )
                break

        if not self.is_folder_empty():
            logging.info("Download concluído com sucesso.")

        self.driver.quit()
