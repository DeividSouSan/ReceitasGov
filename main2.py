import logging
import os
from datetime import datetime

from gui.window import Window

# Capturando o diretório atual
path = os.getcwd()

# Configurando o log
log_filename = f"{path}/logs/logs_{datetime.now().strftime('%d%m%Y_%H_%M_%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

logging.info(
    f"Iniciando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
)

# Iniciando a janela principal
root = Window()
root.mainloop()
