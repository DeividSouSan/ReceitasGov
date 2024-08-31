import configparser
import os
import tkinter as tk
from tkinter import messagebox

path = os.getcwd()


def read_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


config = read_config(os.path.join(path, "config/config.ini"))


class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)

        # Ler o conteúdo do arquivo .ini
        try:
            with open(f"{path}/config/config.ini", "r") as env_file:
                content = env_file.read()
        except FileNotFoundError:
            content = ""

        # Criar uma área de texto para editar o conteúdo do .env
        text_area = tk.Text(self, height=5)
        text_area.insert(tk.END, content)
        text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Criar botão "Salvar"
        save_button = tk.Button(
            self, text="Salvar", command=lambda: self.save(text_area)
        )
        save_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Criar botão "Sair"
        quit_button = tk.Button(self, text="Voltar", command=self.back)
        quit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def save(self, text_area):
        new_content = text_area.get("1.0", tk.END)

        try:
            with open(f"{path}/config/config.ini", "w") as env_file:
                env_file.write(new_content)
            messagebox.showinfo(
                "Sucesso",
                "Configurações salvas com sucesso. Reinicie o programa para aplicar as mudanças.",
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar as configurações: {e}")

    def back(self):
        from gui.frames.main_page import MainPage

        self.controller.show_frame(MainPage)
