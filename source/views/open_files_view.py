import json
import os
import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk
from controllers.window_controller_i import WindowControllerI
from PIL import Image
from views.base_view import BaseView


class OpenFileView(BaseView):
    file_path = None

    def __init__(self, parent: ctk.CTkFrame, controller: WindowControllerI):
        BaseView.__init__(self, parent, controller)
        self.after(10, self._create_widgets)

        if __class__.file_path:
            print(__class__.file_path)
            self.load_file()

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        title = ctk.CTkLabel(
            self,
            text="Leitura de Arquivos",
            font=("Arial", 40, "bold"),
        ).grid(row=0, column=0, columnspan=3, padx=(50, 0), pady=10, sticky="nsw")

        update_img = ctk.CTkImage(
            light_image=Image.open(
                os.path.join(self.path, "static", "img", "update.png")
            ),
            size=(30, 30),
        )
        update_button = ctk.CTkButton(
            self,
            text="",
            height=40,
            width=40,
            image=update_img,
            command=self._reload_file,
            corner_radius=5,
            border_spacing=0,
        ).grid(row=0, column=3, padx=(0, 50), sticky="e")

        # Criar uma área de texto para exibir o conteúdo do arquivo
        self.text_area = ctk.CTkTextbox(self, wrap=tk.WORD)
        self.text_area.grid(
            row=1,
            column=0,
            rowspan=3,
            columnspan=4,
            padx=(40, 40),
            pady=(10, 10),
            sticky="nsew",
        )
        self.text_area.insert(
            tk.END, "Primeiro, selecione um arquivo para exibir o conteúdo."
        )
        self.text_area.configure(state=tk.DISABLED)

        # Criar um botão para abrir o arquivo

        open_button = ctk.CTkButton(
            self,
            text="ABRIR ARQUIVO",
            font=("Arial", 20, "bold"),
            width=200,
            height=70,
            command=self._open_file,
        ).grid(row=4, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="w")

        back_button = ctk.CTkButton(
            self,
            text="VOLTAR",
            command=self._back,
            font=("Arial", 20, "bold"),
            width=200,
            height=70,
        ).grid(row=4, column=2, columnspan=2, padx=50, pady=(10, 20), sticky="e")

    def _open_file(self):
        # Abrir diálogo para selecionar o arquivo
        initial_dir = os.path.join(self.path, "files")
        file_path = filedialog.askopenfilename(
            title="Selecione um arquivo:",
            initialdir=initial_dir,
            filetypes=(
                ("Todos os arquivos", "*.*"),
                ("Arquivos de Log", "*.log"),
                ("Arquivos JSON", "*.json"),
                ("Arquivos CSV", "*.csv"),
            ),
        )

        if not file_path:
            return

        __class__.file_path = file_path
        self._load_file()

    def _load_file(self):
        try:
            # Ler e exibir o conteúdo do arquivo
            with open(__class__.file_path, "r", encoding="utf-8") as file:
                if __class__.file_path.endswith(".json"):
                    content = json.dumps(json.load(file), indent=4, ensure_ascii=False)
                else:
                    content = file.read()

            self.text_area.configure(state=tk.NORMAL)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.text_area.configure(state=tk.DISABLED)

            ctk.CTkMessageBox(
                title="SUCCESS",
                text="Arquivo carregado com sucesso.",
                font=("Arial", 16),
                image_path=os.path.join(self.path, "static", "img", "success.png"),
                image_size=(50, 50),
            )

        except Exception as e:
            ctk.CTkMessageBox(
                title="ERROR",
                text="Selecione um arquivo primeiro!",
                font=("Arial", 16),
                image_path=os.path.join(self.path, "static", "img", "error.png"),
                image_size=(50, 50),
            )

    def _reload_file(self):
        self._load_file()

    def _back(self):
        self.controller.get_view("MainView")
