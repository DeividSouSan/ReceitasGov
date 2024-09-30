import configparser
import logging
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

import customtkinter as ctk
from gui.frames.base_page import BasePage
from PIL import Image
from services.automation_service import AutomationService
from utils.get_page_status import get_page_status

current_dir = os.getcwd()
path = os.path.join(current_dir, "source")


class MainPage(BasePage):
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

        # Page Text Variables
        page_name = "Receitas Portal da Transparência"
        page_subtitle = "Esse software foi desenvolvido para baixar os dados de receitas do Portal da Transparência do Governo Federal."

        # Widgets
        title = ctk.CTkLabel(self, text=page_name, font=("Arial", 40, "bold")).grid(
            row=0, column=0, columnspan=3, pady=10
        )

        # Criar o subtítulo
        subtitle = ctk.CTkLabel(
            self,
            text=page_subtitle,
            font=("Arial", 16),
            wraplength=500,
        ).grid(row=2, column=0, columnspan=4)

        # Label com o status da página
        is_page_online = get_page_status("https://portaldatransparencia.gov.br/")
        status_label_text = "Online" if is_page_online else "Offline"

        page_status = ctk.CTkLabel(
            self,
            text=f"Status da Página: {status_label_text}",
            font=("Arial", 16),
        ).grid(row=3, columnspan=4, pady=0)

        # Imagem

        graph_img = ctk.CTkImage(
            light_image=None,
            dark_image=Image.open(os.path.join(path, "gui", "img", "graph.png")),
            size=(250, 250),
        )

        ctk.CTkLabel(self, text="", image=graph_img).grid(
            row=1, column=0, columnspan=4, pady=10, sticky="nsew"
        )

        # Cria botão para abrir os logs ou saídas
        gear_img = ctk.CTkImage(
            light_image=Image.open(os.path.join(path, "gui", "img", "gear.png")),
            size=(30, 30),
        )

        configuration = ctk.CTkButton(
            self,
            text="",
            height=40,
            width=40,
            image=gear_img,
            command=self.configuration,
            corner_radius=200,
            border_spacing=0,
        ).grid(row=0, column=3)

        start_button = ctk.CTkButton(
            self,
            text="INICIAR",
            font=("Arial", 20, "bold"),
            command=self.start,
            width=200,
            height=70,
        ).grid(row=4, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="nsw")

        open_files = ctk.CTkButton(
            self,
            text="ARQUIVOS",
            font=("Arial", 20, "bold"),
            command=self.files,
            width=200,
            height=70,
        ).grid(row=4, column=2, columnspan=2, padx=50, pady=(10, 20), sticky="nse")

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
        AutomationService().start()

        messagebox.showinfo(
            "Sucesso",
            "Dados enviados para API com sucesso, o arquivo com a saída enviada também foi gerado e pode ser acessado no diretório 'output'.",
        )

    def configuration(self):
        self.controller.show_page("ConfigPage")

    def files(self):
        self.controller.show_page("ReadFilePage")

    def exit(self):
        logging.info(
            f"Encerrando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
        )
        self.quit()
