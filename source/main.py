import logging
import os
from datetime import datetime

from controllers.window import Window
from services.api.api_handler import APIHandler
from services.api.api_post_i import APIPostI
from services.automation_service import AutomationService
from services.bots.get_public_revenue_bot import GetPublicRevenueBot
from services.data.handle_data import HandleData
from views.config_view import ConfigPage
from views.main_view import MainPage
from views.open_files_view import ReadFilePage

# Configurando o Log
log_path = os.path.join(os.getcwd(), "source/files/logs")
log_name = f"app_usage_{datetime.now().strftime('%d%m%Y_%H_%M_%S')}.log"
try:
    logging.basicConfig(filename=f"{log_path}/{log_name}", level=logging.INFO)
except FileNotFoundError:
    os.mkdir(log_path)
    logging.basicConfig(filename=f"{log_path}/{log_name}", level=logging.INFO)

# Configurando a automação
automation = AutomationService(GetPublicRevenueBot, HandleData, APIHandler)

# Iniciando a janela principal
root = Window()
root.set_views(views=[MainPage, ConfigPage, ReadFilePage])
root.views["MainPage"].automation = automation
root.mainloop()
