import logging
import os
import tkinter as tk
from datetime import datetime
from typing import Type

import customtkinter as ctk
from controllers.window_controller_i import WindowControllerI
from views.base_view import BaseView


class Window(ctk.CTk, WindowControllerI):
    def __init__(self):
        ctk.CTk.__init__(self)

        self.views: dict[str, BaseView] = dict()

        self.create_window()

    def create_window(self):
        logging.info(
            f"Iniciando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
        )

        # Define a aparência da janela e o tema padrão
        self.switch_theme("dark")

        # Configura a janela principal
        self.wm_title("Receitas Públicas - Portal da Transparência")
        self.wm_geometry("800x600")
        self.wm_resizable(False, False)
        self.iconphoto(
            False,
            tk.PhotoImage(
                file=os.path.join(
                    os.getcwd(), "source", "static", "icon", "billing.png"
                )
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
            path = os.path.join(os.getcwd(), "source", "themes", "light_theme.json")
            ctk.set_default_color_theme(path)
        elif theme == "dark":
            path = os.path.join(os.getcwd(), "source", "themes", "dark_theme.json")
            ctk.set_default_color_theme(path)

        logging.info(f"Tema alterado para {theme}.")

    def set_views(self, views: list[Type[BaseView]]) -> None:
        view_class: Type[BaseView]

        for view_class in views:
            view_object: BaseView = view_class(parent=self.container, controller=self)
            self.views[view_class.__name__] = view_object
            view_object.grid(row=0, column=0, sticky="nsew")

        self.get_view("MainView")

    def get_view(self, view_name: str) -> None:
        selected_view: BaseView = self.views[view_name]
        view_name = str(selected_view).replace("frame", "").replace(".!", "")
        selected_view.tkraise()

        logging.info(f"Frame {view_name} carregado.")
