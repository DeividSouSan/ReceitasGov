from datetime import datetime
import json
import os
import pandas as pd

class DataProcess:
    def __init__(self, author: str):
        self.my_data = {
            "author": author,
            "date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        }
        
        self.file = pd.read_csv(f"{os.getcwd()}/csv/receitas.csv", delimiter=";")
        
        if os.path.exists("output"):
            pass
        else:
            os.mkdir("output")

    def get_json(self) -> str:
        """
        Processa os dados do arquivo CSV e retorna um JSON.
        
        Args:
            log (bool): Se True, salva o JSON em um arquivo.
        """
        self.file = self.file[['Órgão', 'Espécie', 'Orçamento Atualizado (Valor Previsto)', 'Receita Realizada (Valor Arrecadado)']]
        
        json_data = self.file.to_json(orient='records')
        
        with open("output/data.json", 'w', encoding='utf-8') as f:
            json.dump(json.loads(json_data), f, ensure_ascii=False, indent=4)

        return json_data
    
    def process(self, data) -> dict:
        """
        Processa os dados do JSON e retorna um dicionário.
        
        Args:
            data (str): JSON com os dados.
            log (bool): Se True, salva o dicionário em um arquivo JSON.
        """
        self.my_data["data"] = json.loads(data)
        
            
        with open('output/output.json', 'w', encoding='utf-8') as f:
            json.dump(self.my_data, f, ensure_ascii=False, indent=4)

        return self.my_data