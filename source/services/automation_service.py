from api.api_handler import APIHandler
from bots.get_public_revenue_bot import GetPublicRevenueBot
from data.data_handler import DataProcess


class AutomationService:
    @staticmethod
    def start(self):
        bot = GetPublicRevenueBot("https://portaldatransparencia.gov.br/", 2)
        bot.start()

        data_handler = DataProcess("Deivid Souza Santana")
        data_handler.jsonify(
            [
                "Órgão",
                "Espécie",
                "Orçamento Atualizado (Valor Previsto)",
                "Receita Realizada (Valor Arrecadado)",
            ]
        )
        data_handler.make_output()

        api_handler = APIHandler("https://66d30ae0184dce1713cf1e02.mockapi.io/data")
        api_handler.post_data()
