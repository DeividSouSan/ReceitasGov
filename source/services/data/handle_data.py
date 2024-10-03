import json
import logging
import os
from datetime import datetime

import pandas as pd
from services.data.data_handler import DataHandler


class HandleData(DataHandler):
    """
    Processa e manipula os dados do DataFrame e salva em arquivos JSON.
    """

    def __init__(self, author: str):
        logging.info(f"Iniciando o HandleData.")

        self.output = {
            "author": author,
            "date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }

        if os.path.exists("source/files/output"):
            logging.info(f"Diretório output já existe.")
        else:
            os.mkdir("source/files/output")
            logging.info(f"Diretório output foi criado.")

    def process_data(self) -> any:
        """
        Manipula os dados do DataFrame selecionando apenas as colunas passadas. O json é salvo em um arquivo
        chamado 'data.json' e também é retornado pela função.

        Args:
            columns (list): Lista com os nomes das colunas que deseja selecionar.
        """

        self.dataframe = pd.read_csv(
            os.path.join(os.getcwd(), "source/files/download/receitas.csv"),
            delimiter=";",
        )

        columns = [
            "Órgão",
            "Espécie",
            "Orçamento Atualizado (Valor Previsto)",
            "Receita Realizada (Valor Arrecadado)",
        ]

        json_data = self.dataframe[columns].to_json(orient="records")

        logging.info(f"Dados processados com sucesso. Colunas selecionadas: {columns}.")

        return json_data

    def make_output_files(self, data) -> None:
        """
        Transforma um arquivo JSON em um dicionário e salva em um arquivo chamado 'output.json'.
        """

        data = json.loads(data)

        # Salvando o arquivo data.json
        with open("source/files/output/data.json", "w", encoding="utf-8") as file:

            json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info(
                f"Dados baixados e convertidos em JSON salvos com sucesso em 'data.json'."
            )

        # Salvando o arquivo output.json
        with open("source/files/output/output.json", "w", encoding="utf-8") as file:
            self.output["data"] = data
            json.dump(self.output, file, ensure_ascii=False, indent=4)
            logging.info(
                f"Dados de saída com autor e data salvos com sucesso em 'output.json'."
            )
