from datetime import datetime
import json
import pandas as pd

class DataProcess:
    def __init__(self, author: str, path: str):
        self.my_data = {
            "author": author,
            "date": datetime.now().date().isoformat()
        }
        
        self.file = pd.read_csv(f"{path}/receitas.csv", delimiter=";")

    def get_json(self, log: bool = False) -> str:
        """
        Processa os dados do arquivo CSV e retorna um JSON.
        
        Args:
            log (bool): Se True, salva o JSON em um arquivo.
        """
        self.file = self.file[['Órgão', 'Espécie', 'Orçamento Atualizado (Valor Previsto)', 'Receita Realizada (Valor Arrecadado)']]
        
        json_data = self.file.to_json(orient='records')
        
        if log:
            with open("logs/data.json", 'w', encoding='utf-8') as f:
                json.dump(json.loads(json_data), f, ensure_ascii=False, indent=4)

        return json_data
    
    def process(self, data, log: bool = False) -> dict:
        """
        Processa os dados do JSON e retorna um dicionário.
        
        Args:
            data (str): JSON com os dados.
            log (bool): Se True, salva o dicionário em um arquivo JSON.
        """
        self.my_data["data"] = json.loads(data)
        
        if log:
            with open('logs/output.json', 'w', encoding='utf-8') as f:
                json.dump(self.my_data, f, ensure_ascii=False, indent=4)

        return self.my_data