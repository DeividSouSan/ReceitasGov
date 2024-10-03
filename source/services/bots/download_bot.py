import logging
import os
from abc import ABC, abstractmethod

from selenium.webdriver import Chrome, ChromeOptions


class DownloadBot(ABC):
    def __init__(self, web_url: str, max_time: int):
        self.url = web_url
        self.donwload_folder = os.path.join(os.getcwd(), "source/files/download")

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

    def is_folder_empty(self) -> bool:
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

    @abstractmethod
    def start(self) -> None:
        pass
