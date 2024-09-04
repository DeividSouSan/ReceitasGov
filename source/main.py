import logging
import os
from datetime import datetime

from gui.frames.config_page import ConfigPage
from gui.frames.main_page import MainPage
from gui.frames.read_files_page import ReadFilePage
from gui.window import Window

# Capturando o diretório atual
path = os.getcwd()

# Configurando o log
logs_path = (
    f"{path}/source/logs/app_usage_{datetime.now().strftime('%d%m%Y_%H_%M_%S')}.log"
)
logging.basicConfig(filename=logs_path, level=logging.INFO)

logging.info(
    f"Iniciando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
)

# Iniciando a janela principal
root = Window(frames=[MainPage, ConfigPage, ReadFilePage])
root.mainloop()
