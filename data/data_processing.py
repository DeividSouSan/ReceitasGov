from datetime import datetime
import json
import logging
import os
import pandas as pd


class DataProcess:
    """
    Processa e manipula os dados do DataFrame e salva em arquivos JSON.
    """
    def __init__(self, author: str):
        self.author = author
        
        base_path = os.getcwd()
        self.dataframe = pd.read_csv(f"{base_path}/csv/receitas.csv", delimiter=";")

        if os.path.exists("output"):
            logging.info(f"Diretório output já existe.")
        else:
            os.mkdir("output")
            logging.info(f"Diretório output foi criado.")
            

    def handle_data(self, columns: list) -> any:
        """
        Manipula os dados do DataFrame selecionando apenas as colunas passadas. O json é salvo em um arquivo 
        chamado 'data.json' e também é retornado pela função.

        Args:
            columns (list): Lista com os nomes das colunas que deseja selecionar.
        """

        if columns:
            json_data = self.dataframe[columns].to_json(orient='records')
        else:
            json_data = self.dataframe.to_json(orient='records')

        with open("output/data.json", 'w', encoding='utf-8') as file:
            json.dump(json.loads(json_data), file, ensure_ascii=False, indent=4)

        logging.info(f"Dataframe convertido para JSON com sucesso.")
        return json_data

    def output_data(self, data: any) -> dict:
        """
        Transforma um arquivo JSON em um dicionário e salva em um arquivo chamado 'output.json', o conteúdo do dicionáro
        é retornado pela função.

        Args:
            data (str): JSON com os dados.
        """

        output = {
            "author": self.author,
            "date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            "data": json.loads(data)
            }

        with open('output/output.json', 'w', encoding='utf-8') as file:
            json.dump(output, file, ensure_ascii=False, indent=4)
            
        logging.info(f"Dados de saída salvos com sucesso.")
        return output
