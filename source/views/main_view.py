import logging
import os
from datetime import datetime

import customtkinter as ctk
from controllers.window_controller_i import WindowControllerI
from PIL import Image
from services.automation_i import AutomationI
from utils.get_page_status import get_page_status
from views.base_view import BaseView


class MainView(BaseView):
    def __init__(self, parent: ctk.CTkFrame, controller: WindowControllerI):
        super().__init__(parent, controller)

        self.automation: AutomationI = None

        self._create_widgets()

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        page_name = "Receitas Portal da Transparência"
        title = ctk.CTkLabel(self, text=page_name, font=("Arial", 40, "bold")).grid(
            row=0, column=0, columnspan=3, padx=(50, 5), pady=10, sticky="nsw"
        )

        gear_img = ctk.CTkImage(
            light_image=Image.open(
                os.path.join(self.path, "static", "img", "gear.png")
            ),
            size=(30, 30),
        )

        configuration = ctk.CTkButton(
            self,
            text="",
            height=40,
            width=40,
            image=gear_img,
            command=self._configuration,
            corner_radius=5,
            border_spacing=0,
        ).grid(row=0, column=3, padx=(0, 50), sticky="e")

        graph_img = ctk.CTkImage(
            light_image=None,
            dark_image=Image.open(
                os.path.join(self.path, "static", "img", "graph.png")
            ),
            size=(250, 250),
        )

        ctk.CTkLabel(self, text="", image=graph_img).grid(
            row=1, column=0, columnspan=4, pady=10, sticky="nsew"
        )

        page_subtitle = "Esse software foi desenvolvido para baixar os dados de receitas do Portal da Transparência do Governo Federal."
        subtitle = ctk.CTkLabel(
            self,
            text=page_subtitle,
            font=("Arial", 16),
            wraplength=500,
        ).grid(row=2, column=0, columnspan=4)

        is_page_online = get_page_status("https://portaldatransparencia.gov.br/")
        status_label_text = "Online" if is_page_online else "Offline"
        page_status = ctk.CTkLabel(
            self,
            text=f"Status da Página: {status_label_text}",
            font=("Arial", 16),
        ).grid(row=3, columnspan=4, pady=0)

        start_button = ctk.CTkButton(
            self,
            text="INICIAR",
            font=("Arial", 20, "bold"),
            command=self._start,
            width=200,
            height=70,
        ).grid(row=4, column=0, columnspan=2, padx=50, pady=(10, 20), sticky="w")

        open_files = ctk.CTkButton(
            self,
            text="ARQUIVOS",
            font=("Arial", 20, "bold"),
            command=self._files,
            width=200,
            height=70,
        ).grid(row=4, column=2, columnspan=2, padx=50, pady=(10, 20), sticky="e")

        if not is_page_online:
            logging.error("A página está offline.")
            start_button["state"] = "disabled"

    def _start(self):
        self.automation.start()

        ctk.CTkMessageBox(
            title="Sucesso",
            text="Dados enviados para API com sucesso, o arquivo com a saída enviada também foi gerado e pode ser acessado no diretório 'output'.",
            font=("Arial", 12),
            image_path=os.path.join(self.path, "static", "img", "success.png"),
            image_size=(50, 50),
        )

    def _configuration(self):
        self.controller.get_view("ConfigPage")

    def _files(self):
        self.controller.get_view("ReadFilePage")

    def _exit(self):
        logging.info(
            f"Encerrando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
        )
        self.quit()
