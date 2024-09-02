import os
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class GetPublicRevenueBot:
    """
    Automação para baixar os dados das receitas fornecidas pelo Portal da Transparência.
    """

    def __init__(self, web_url: str, download_time: int):
        self.url = web_url
        self.donwload_folder = f"{os.getcwd()}/csv/"
        self.download_wait_time = download_time

        chrome_options = ChromeOptions()
        prefs = {"download.default_directory": self.donwload_folder}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")

        self.driver = Chrome(options=chrome_options)

    def clear_download_folder(self) -> None:
        """
        Limpa a pasta de downloads (csv) se ela não estiver vazia.
        """
        n_files = len(os.listdir(self.donwload_folder))

        if n_files > 0:
            for file in os.listdir(self.donwload_folder):
                os.remove(os.path.join(self.donwload_folder, file))

    def start(self) -> None:
        """
        Inicia o processo de donwload da receita.
        """

        self.clear_download_folder()

        self.driver.get(self.url)

        self.driver.find_element(By.ID, "despesas-card").click()
        self.driver.find_element(By.CSS_SELECTOR, "#receitas-links").find_elements(
            By.TAG_NAME, "a"
        )[1].click()
        self.driver.find_element(
            By.CLASS_NAME, "box-tabela-completa__opcoes"
        ).find_elements(By.TAG_NAME, "a")[1].click()

        sleep(self.download_wait_time)

        self.driver.quit()
