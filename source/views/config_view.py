import configparser
import os
from tkinter import IntVar, StringVar

import customtkinter as ctk
from controllers.window_controller_i import WindowControllerI
from views.base_view import BaseView


class ConfigView(BaseView):
    def __init__(self, parent: ctk.CTkFrame, controller: WindowControllerI):
        BaseView.__init__(self, parent, controller)
        self.after(10, self._create_widgets)

        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(self.path, "config.ini"))

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        title = ctk.CTkLabel(
            self, text="Configurações", font=("Arial", 40, "bold")
        ).grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")

        # Download seconds

        download_wait_time_label = ctk.CTkLabel(
            self, text="Tempo de download (segundos):", font=("Arial", 20)
        ).grid(row=1, column=0, padx=(50, 0), sticky="w")

        self.download_wait_time = StringVar()
        self.download_wait_time.set(self.config["DOWNLOAD"]["WAIT_TIME"])

        download_wait_time_entry = ctk.CTkEntry(
            self,
            textvariable=self.download_wait_time,
        ).grid(row=1, column=1, columnspan=4, padx=(0, 50), sticky="e")

        # Default donwload folder
        default_folder_label = ctk.CTkLabel(
            self, text="Baixar em /Downloads:", font=("Arial", 20)
        ).grid(row=2, column=0, padx=(50, 0), sticky="w")

        state: bool = self.config["DOWNLOAD"].getboolean("DEVICE_DOWNLOAD_FOLDER")

        self.default_folder_switch = ctk.CTkSwitch(self)

        if state == True:
            self.default_folder_switch.select()
        else:
            self.default_folder_switch.deselect()

        self.default_folder_switch.grid(
            row=2, column=1, columnspan=4, padx=(0, 50), sticky="e"
        )

        author_label = ctk.CTkLabel(
            self, text="Assinatura no Output:", font=("Arial", 20)
        ).grid(row=3, column=0, padx=(50, 0), sticky="w")

        self.author = StringVar()
        self.author.set(self.config["OUTPUT"]["AUTHOR"])

        author_entry = ctk.CTkEntry(
            self,
            textvariable=self.author,
        ).grid(row=3, column=1, columnspan=4, padx=(0, 50), sticky="e")

        save_button = ctk.CTkButton(
            self,
            text="SALVAR",
            font=("Arial", 20, "bold"),
            width=200,
            height=70,
            command=self._save,
        ).grid(row=5, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="w")

        quit_button = ctk.CTkButton(
            self,
            text="VOLTAR",
            font=("Arial", 20, "bold"),
            command=self._back,
            width=200,
            height=70,
        ).grid(row=5, column=3, columnspan=2, padx=50, pady=(10, 20), sticky="e")

    def _save(self):
        if not self.download_wait_time.get().isnumeric():
            ctk.CTkMessageBox(
                title="ERROR",
                text="Valor inválido para o tempo de download.",
                font=("Arial", 16),
                image_path=os.path.join(self.path, "static", "img", "error.png"),
                image_size=(50, 50),
            )
            return
        else:

            self.config["DOWNLOAD"]["WAIT_TIME"] = self.download_wait_time.get()

            default_folder_switch = self.default_folder_switch.get()
            self.config["DOWNLOAD"]["DEVICE_DOWNLOAD_FOLDER"] = (
                "true" if default_folder_switch == 1 else "false"
            )

            self.config["OUTPUT"]["AUTHOR"] = self.author.get()

            with open(os.path.join(self.path, "config.ini"), "w") as file:
                self.config.write(file)

            ctk.CTkMessageBox(
                title="CONFIGURATION SAVED",
                text="Todas as configurações foram salvas com sucesso.",
                font=("Arial", 16),
                image_path=os.path.join(self.path, "static", "img", "success.png"),
                image_size=(50, 50),
            )

    def _back(self):
        self.controller.get_view("MainView")
