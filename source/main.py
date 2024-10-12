import logging
import os
from datetime import datetime

from controllers.window import Window
from services.api.api_handler import APIHandler
from services.automation_service import AutomationService
from services.bots.get_public_revenue_bot import GetPublicRevenueBot
from services.data.handle_data import HandleData
from views.config_view import ConfigView
from views.main_view import MainView
from views.open_files_view import OpenFileView

# Configurando o Log
if not os.path.exists(os.path.join(os.getcwd(), "source/files")):
    os.mkdir(os.path.join(os.getcwd(), "source/files"))
    os.mkdir(os.path.join(os.getcwd(), "source/files/logs"))
    os.mkdir(os.path.join(os.getcwd(), "source/files/download"))
    os.mkdir(os.path.join(os.getcwd(), "source/files/output"))

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
root.set_views(views=(MainView, ConfigView, OpenFileView))
root.views["MainView"].automation = automation
root.mainloop()
