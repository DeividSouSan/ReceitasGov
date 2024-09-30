import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk
from gui.frames.base_page import BasePage
from PIL import Image


class ReadFilePage(BasePage):
    file_path = None

    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

        if __class__.file_path:
            print(__class__.file_path)
            self.load_file()

        title = ctk.CTkLabel(
            self,
            text="Leitura de Arquivos",
            font=("Arial", 40, "bold"),
        ).grid(row=0, column=0, columnspan=3)

        # Criar uma área de texto para exibir o conteúdo do arquivo
        global text_area
        text_area = ctk.CTkTextbox(self, wrap=tk.WORD)
        text_area.grid(
            row=1,
            column=0,
            rowspan=3,
            columnspan=4,
            padx=(40, 40),
            pady=(10, 10),
            sticky="nsew",
        )
        text_area.insert(
            tk.END, "Primeiro, selecione um arquivo para exibir o conteúdo."
        )
        text_area.configure(state=tk.DISABLED)

        # Criar um botão para abrir o arquivo
        current_dir = os.getcwd()
        self._path = os.path.join(current_dir, "source")

        update_img = ctk.CTkImage(
            light_image=Image.open(
                os.path.join(self._path, "gui", "img", "update.png")
            ),
            size=(30, 30),
        )

        update_button = ctk.CTkButton(
            self,
            text="",
            height=40,
            width=40,
            image=update_img,
            command=self.reload_file,
            fg_color="#588157",
            corner_radius=200,
            border_spacing=0,
        ).grid(row=0, column=3)

        open_button = ctk.CTkButton(
            self,
            text="ABRIR ARQUIVO",
            font=("Arial", 20, "bold"),
            width=200,
            height=70,
            command=self.open_file,
        ).grid(row=4, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="nsw")

        back_button = ctk.CTkButton(
            self,
            text="VOLTAR",
            command=self.back,
            font=("Arial", 20, "bold"),
            width=200,
            height=70,
        ).grid(row=4, column=2, columnspan=2, padx=50, pady=(10, 20), sticky="nse")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

    def open_file(self):
        # Abrir diálogo para selecionar o arquivo
        initial_dir = os.path.join(os.getcwd(), "source/logs")
        file_path = filedialog.askopenfilename(
            title="Selecione um arquivo:",
            initialdir=initial_dir,
            filetypes=[("Arquivos de Log", "*.log"), ("Arquivos JSON", "*.json")],
        )

        if not file_path:
            return

        __class__.file_path = file_path
        self.load_file()

    def load_file(self):
        try:
            # Ler e exibir o conteúdo do arquivo
            with open(__class__.file_path, "r", encoding="utf-8") as file:
                if __class__.file_path.endswith(".json"):
                    content = json.dumps(json.load(file), indent=4, ensure_ascii=False)
                else:
                    content = file.read()

            text_area.configure(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
            text_area.configure(state=tk.DISABLED)

            ctk.CTkMessageBox(
                title="SUCCESS",
                text="Arquivo carregado com sucesso.",
                font=("Arial", 16),
                image_path=os.path.join(self._path, "gui", "img", "success.png"),
                image_size=(50, 50),
            )

        except Exception as e:
            ctk.CTkMessageBox(
                title="ERROR",
                text="Selecione um arquivo primeiro!",
                font=("Arial", 16),
                image_path=os.path.join(self._path, "gui", "img", "error.png"),
                image_size=(50, 50),
            )

    def reload_file(self):
        self.load_file()

    def back(self):
        self.controller.show_page("MainPage")
