import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from gui.frames.base_page import BasePage


class ConfigPage(BasePage):
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

        path = os.path.join(os.getcwd(), "source", "gui", "themes", "light_theme.json")
        ctk.set_default_color_theme(path)

        # Criando o label
        title = ctk.CTkLabel(
            self, text="Configurações", font=("Arial", 40, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

        self.switch_theme = ctk.CTkOptionMenu(
            self, values=["Escuro", "Claro"], command=self.switch_theme
        ).grid(row=1, column=0, padx=10, pady=10)

        # Criando botões
        save_button = ctk.CTkButton(
            self,
            text="Salvar",
        ).grid(row=2, column=0, padx=10, pady=10, sticky="nw")

        quit_button = ctk.CTkButton(self, text="Voltar", command=self.back).grid(
            row=2, column=2, padx=10, pady=10, sticky="ne"
        )

    def switch_theme(self, theme: str):
        if theme == "Escuro":
            self.controller.switch_theme("dark")
        elif theme == "Claro":
            self.controller.switch_theme("light")
        else:
            messagebox.showerror("Erro", "Tema não encontrado.")

    def save(self, text_area):
        pass

    def back(self):
        self.controller.show_page("MainPage")
