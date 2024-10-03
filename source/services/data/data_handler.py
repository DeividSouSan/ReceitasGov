import logging
import os
from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd


class DataHandler(ABC):
    """
    Processa e manipula os dados do DataFrame e salva em arquivos JSON.
    """

    def __init__(self, author: str):

        self.output = {
            "author": author,
            "date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }

        if os.path.exists("source/logs/output"):
            logging.info(f"Diretório output já existe.")
        else:
            os.mkdir("source/logs/output")
            logging.info(f"Diretório output foi criado.")

    @abstractmethod
    def process_data(self) -> None:
        pass

    @abstractmethod
    def make_output_files(self) -> None:
        pass
