from tkinter import StringVar

import customtkinter as ctk
from controllers.window_controller_i import WindowControllerI
from views.base_view import BaseView


class ConfigPage(BaseView):
    def __init__(self, parent: ctk.CTkFrame, controller: WindowControllerI):
        BaseView.__init__(self, parent, controller)
        self.after(10, self._create_widgets)

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        title = ctk.CTkLabel(
            self, text="Configurações", font=("Arial", 40, "bold")
        ).grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")

        # Download seconds
        download_seconds_label = ctk.CTkLabel(
            self, text="Tempo de download (segundos):", font=("Arial", 20)
        ).grid(row=1, column=0, padx=(50, 0), sticky="w")

        download_seconds_entry = ctk.CTkEntry(
            self,
            placeholder_text="Tempo em Segundos",
        ).grid(row=1, column=1, columnspan=4, padx=(0, 50), sticky="e")

        # Default donwload folder
        default_folder_label = ctk.CTkLabel(
            self, text="Diretório Donwloads na Máquina:", font=("Arial", 20)
        ).grid(row=2, column=0, padx=(50, 0), sticky="w")

        default_folder_entry = ctk.CTkSwitch(
            self,
        ).grid(row=2, column=1, columnspan=4, padx=(0, 50), sticky="e")

        author_label = ctk.CTkLabel(
            self, text="Assinatura no Output:", font=("Arial", 20)
        ).grid(row=3, column=0, padx=(50, 0), sticky="w")

        author_entry = ctk.CTkEntry(
            self,
            placeholder_text="Assinatura do Autor",
        ).grid(row=3, column=1, columnspan=4, padx=(0, 50), sticky="e")

        save_button = ctk.CTkButton(
            self,
            text="SALVAR",
            font=("Arial", 20, "bold"),
            width=200,
            height=70,
        ).grid(row=5, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="w")

        quit_button = ctk.CTkButton(
            self,
            text="VOLTAR",
            font=("Arial", 20, "bold"),
            command=self._back,
            width=200,
            height=70,
        ).grid(row=5, column=3, columnspan=2, padx=50, pady=(10, 20), sticky="e")

    def _save(self, text_area):
        pass

    def _back(self):
        self.controller.get_view("MainPage")
