import configparser
import logging
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from gui.frames.config_page import ConfigPage
from gui.frames.read_files_page import ReadFilePage
from services.automation_service import AutomationService
from utils.get_page_status import get_page_status

current_dir = os.getcwd()
path = os.path.join(current_dir, "source")


def read_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


config = read_config(os.path.join(path, "config.ini"))


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.automation_service = AutomationService()

        tk.Frame.__init__(self, self.parent)

        title_label = tk.Label(
            self, text=config["Bot"]["BOT_NAME"], font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, columnspan=3, pady=10, sticky="nsew")

        # Cria botão para abrir os logs ou saídas
        open_file_btn = tk.Button(self, text="Open Files", command=self.files)
        open_file_btn.grid(row=0, column=3, sticky="nsew")

        # Criar o subtítulo
        subtitle_label = tk.Label(
            self, text=config["Bot"]["BOT_DESC"], font=("Helvetica", 12)
        )
        subtitle_label.grid(row=1, columnspan=3, pady=5, sticky="nsew")

        # Label com o status da página
        is_page_online = get_page_status(config["Download"]["WEBSITE_URL"])
        status_label_text = "Online" if is_page_online else "Offline"
        status_label = tk.Label(
            self, text=f"A página está: {status_label_text}", font=("Helvetica", 10)
        )
        status_label.grid(row=2, columnspan=3, pady=15, sticky="nsew")

        # Criar os botões princípais
        start_button = tk.Button(self, text="Iniciar", command=self.start)
        start_button.grid(row=3, column=0, sticky="nsew")

        if not is_page_online:
            logging.error("A página está offline.")
            start_button["state"] = "disabled"

        configs_button = tk.Button(
            self, text="Configuration", command=self.configuration
        )
        configs_button.grid(row=3, column=1, sticky="nsew")

        quit_button = tk.Button(self, text="Sair", command=self.exit)
        quit_button.grid(row=3, column=2, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

    def start(self):
        self.automation_service.start(config)

        messagebox.showinfo(
            "Sucesso",
            "Dados enviados para API com sucesso, o arquivo com a saída enviada também foi gerado e pode ser acessado no diretório 'output'.",
        )

    def configuration(self):
        self.controller.show_frame(ConfigPage)

    def files(self):
        self.controller.show_frame(ReadFilePage)

    def exit(self):
        logging.info(
            f"Encerrando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
        )
        self.quit()
