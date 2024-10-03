from services.api.api_post_i import APIPostI
from services.automation_i import AutomationI
from services.bots.download_bot import DownloadBot
from services.data.data_handler import DataHandler


class AutomationService(AutomationI):
    def __init__(
        self, download_bot: DownloadBot, data_handler: DataHandler, post_api: APIPostI
    ):
        self.download_bot = download_bot
        self.data_process = data_handler
        self.api_handler = post_api

    def start(self):
        bot = self.download_bot()
        bot.start()

        data_handler = self.data_process(author="Deivid Souza Santana")
        data = data_handler.process_data()
        data_handler.make_output_files(data)

        self.api_handler().post_data("https://66d30ae0184dce1713cf1e02.mockapi.io/data")
