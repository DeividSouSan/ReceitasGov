import configparser
import logging
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

import customtkinter as ctk
from gui.frames.config_page import ConfigPage
from gui.frames.read_files_page import ReadFilePage
from PIL import Image
from services.automation_service import AutomationService
from utils.get_page_status import get_page_status

current_dir = os.getcwd()
path = os.path.join(current_dir, "source")


def read_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


config = read_config(os.path.join(path, "config.ini"))


class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        # Window relates
        self.controller = controller
        self.parent = parent

        # Automation Service
        self.automation_service = AutomationService()

        # Config Variables

        self.page_name = config["MainPage"]["TITLE"]
        self.page_subtitle = config["MainPage"]["BOT_DESC"]
        self.target_url = config["Download"]["WEBSITE_URL"]

        # Widgets
        ctk.CTkFrame.__init__(self, self.parent, fg_color="#23272a")

        title_label = ctk.CTkLabel(
            self, text=self.page_name, text_color="#ffffff", font=("Arial", 40, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

        # Criar o subtítulo
        subtitle_label = ctk.CTkLabel(
            self,
            text=self.page_subtitle,
            text_color="#ffffff",
            font=("Arial", 16),
            fg_color=None,
            wraplength=500,
        )
        subtitle_label.grid(row=2, column=0, columnspan=4, pady=5, sticky="nsew")

        # Label com o status da página
        is_page_online = get_page_status(self.target_url)
        status_label_text = "Online" if is_page_online else "Offline"
        status_label = ctk.CTkLabel(
            self,
            text=f"A página está: {status_label_text}",
            font=("Arial", 16),
            fg_color=None,
        )
        if is_page_online:
            status_label._text_color = "green"
        else:
            status_label._text_color = "#red"

        status_label.grid(row=3, columnspan=4, pady=15, sticky="nsew")

        # Imagem

        img = ctk.CTkImage(
            light_image=Image.open(os.path.join(path, "gui", "img", "dollar_3.png")),
            dark_image=Image.open(os.path.join(path, "gui", "img", "dollar_3.png")),
            size=(300, 300),
        )

        img_label = ctk.CTkLabel(self, text="", image=img)
        img_label.grid(row=1, column=0, columnspan=4, pady=10, sticky="nsew")

        # Cria botão para abrir os logs ou saídas
        configuration = ctk.CTkButton(
            self,
            text="CONFIGS",
            height=20,
            command=self.configuration,
            fg_color="#99aab5",
        )
        configuration.grid(row=0, column=3)

        start_button = ctk.CTkButton(
            self,
            text="INICIAR",
            command=self.start,
            fg_color="#7289da",
            width=200,
            height=70,
        )
        start_button.grid(row=3, column=0, columnspan=2)

        open_files = ctk.CTkButton(
            self,
            text="ARQUIVOS",
            command=self.files,
            fg_color="#7289da",
            width=200,
            height=70,
        )
        open_files.grid(row=3, column=2, columnspan=2)

        if not is_page_online:
            logging.error("A página está offline.")
            start_button["state"] = "disabled"

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
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
