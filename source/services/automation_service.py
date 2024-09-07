from api.api_handler import ApiHandler
from bots.get_public_revenue_bot import GetPublicRevenueBot
from data.data_handler import DataProcess


class AutomationService:
    def start(self, config: dict[str, str]):
        bot = GetPublicRevenueBot(
            config["Download"]["WEBSITE_URL"], int(config["Download"]["MAX_TIME"])
        )
        bot.start()

        data_handler = DataProcess(config["Author"]["AUTHOR"])
        data_handler.jsonify(config["Data"]["COLUMNS"])
        data_handler.make_output()

        api_handler = ApiHandler(config["API"]["API_URL"])
        api_handler.post_data()
