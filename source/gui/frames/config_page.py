import configparser
import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk


def read_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


config = read_config(os.path.join(os.getcwd(), "source/config.ini"))


class ConfigPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        ctk.CTkFrame.__init__(self, parent, fg_color="#23272a")

        # Ler o conteúdo do arquivo .ini
        try:
            with open(os.path.join(os.getcwd(), "source/config.ini"), "r") as env_file:
                content = env_file.read()
        except FileNotFoundError:
            content = ""

        # Criar uma área de texto para editar o conteúdo do .env
        text_area = ctk.CTkTextbox(self, height=5)
        text_area.insert(tk.END, content)
        text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Criar botão "Salvar"
        save_button = ctk.CTkButton(
            self, text="Salvar", command=lambda: self.save(text_area)
        )
        save_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Criar botão "Sair"
        quit_button = ctk.CTkButton(self, text="Voltar", command=self.back)
        quit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def save(self, text_area):
        new_content = text_area.get("1.0", tk.END)

        try:
            with open(os.path.join(os.getcwd(), "source/config.ini"), "w") as env_file:
                env_file.write(new_content)
            ctk.CTkInputDialog(
                title="Sucesso", text="Configurações salvas com sucesso."
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar as configurações: {e}")

    def back(self):
        from gui.frames.main_page import MainPage

        self.controller.show_frame(MainPage)
