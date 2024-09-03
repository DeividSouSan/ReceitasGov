import json
import logging
import os
from datetime import datetime

import pandas as pd


class DataProcess:
    """
    Processa e manipula os dados do DataFrame e salva em arquivos JSON.
    """

    def __init__(self, author: str):

        self.output = {
            "author": author,
            "date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }

        self.dataframe = pd.read_csv(
            os.path.join(os.getcwd(), "source/data/csv/receitas.csv"), delimiter=";"
        )

        if os.path.exists("source/logs/output"):
            logging.info(f"Diretório output já existe.")
        else:
            os.mkdir("source/logs/output")
            logging.info(f"Diretório output foi criado.")

    def jsonify(self, columns: list) -> any:
        """
        Manipula os dados do DataFrame selecionando apenas as colunas passadas. O json é salvo em um arquivo
        chamado 'data.json' e também é retornado pela função.

        Args:
            columns (list): Lista com os nomes das colunas que deseja selecionar.
        """

        if columns:
            json_data = self.dataframe[columns].to_json(orient="records")
        else:
            json_data = self.dataframe.to_json(orient="records")

        with open("source/logs/output/data.json", "w", encoding="utf-8") as file:
            json.dump(json.loads(json_data), file, ensure_ascii=False, indent=4)

        logging.info(f"Dataframe convertido para JSON com sucesso.")
        return json_data

    def output(self, data: any) -> dict:
        """
        Transforma um arquivo JSON em um dicionário e salva em um arquivo chamado 'output.json', o conteúdo do dicionáro
        é retornado pela função.

        Args:
            data (str): JSON com os dados.
        """

        self.output["data"] = json.loads(data)

        with open("source/logs/output/output.json", "w", encoding="utf-8") as file:
            json.dump(self.output, file, ensure_ascii=False, indent=4)

        logging.info(f"Dados de saída salvos com sucesso.")

        return self.output
