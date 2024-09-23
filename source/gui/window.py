import logging
import os
import tkinter as tk
from datetime import datetime
from typing import Type

import customtkinter as ctk
from gui.frames.main_page import BasePage


class Window(ctk.CTk):
    def __init__(self):
        logging.info(
            f"Iniciando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
        )

        # Define a aparência da janela e o tema padrão
        self.switch_theme("light")
        ctk.CTk.__init__(self)

        # Configura a janela principal
        self.wm_title("Receitas Públicas - Portal da Transparência")
        self.wm_geometry("800x600")
        self.wm_resizable(False, False)
        self.iconphoto(
            False,
            tk.PhotoImage(
                file=os.path.join(os.getcwd(), "source", "gui", "icon", "billing.png")
            ),
        )

        # Configura o container principal
        self.container = ctk.CTkFrame(self, width=800, height=600)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        logging.info("Janela principal carregada com sucesso.")

    def switch_theme(self, theme: str) -> None:
        """_summary_

        Args:
            theme (str): "light" ou "dark"
        """
        if theme == "light":
            path = os.path.join(
                os.getcwd(), "source", "gui", "themes", "light_theme.json"
            )
            ctk.set_default_color_theme(path)
        elif theme == "dark":
            path = os.path.join(
                os.getcwd(), "source", "gui", "themes", "dark_theme.json"
            )
            ctk.set_default_color_theme(path)

        logging.info(f"Tema alterado para {theme}.")

    def load_pages(self, pages: list[Type[BasePage]]) -> None:
        self.pages: dict[Type[BasePage], BasePage] = dict()

        page_class: Type[BasePage]

        for page_class in pages:
            page_object: BasePage = page_class(parent=self.container, controller=self)
            self.pages[page_class] = page_object
            page_object.grid(row=0, column=0, sticky="nsew")

        main_page = next(iter(self.pages.keys()))
        self.show_page(main_page)

    def show_page(self, page: Type[BasePage]) -> None:
        selected_page: BasePage = self.pages[page]
        page_name = str(selected_page).replace("frame", "").replace(".!", "")
        selected_page.tkraise()

        logging.info(f"Frame {page_name} carregado.")
