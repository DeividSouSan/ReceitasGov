import logging
import os
from datetime import datetime

from gui.frames.config_page import ConfigPage
from gui.frames.main_page import MainPage
from gui.frames.read_files_page import ReadFilePage
from gui.window import Window

# Configurando o Log
log_path = os.path.join(os.getcwd(), "source/logs")
log_name = f"app_usage_{datetime.now().strftime('%d%m%Y_%H_%M_%S')}.log"
logging.basicConfig(filename=f"{log_path}/{log_name}", level=logging.INFO)

# Iniciando a janela principal
root = Window(frames=[MainPage, ConfigPage, ReadFilePage])
root.mainloop()
