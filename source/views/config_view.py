import customtkinter as ctk
from controllers.window_controller_i import WindowControllerI
from views.base_view import BaseView


class ConfigPage(BaseView):
    def __init__(self, parent: ctk.CTkFrame, controller: WindowControllerI):
        BaseView.__init__(self, parent, controller)
        self.after(10, self._create_widgets)

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        title = ctk.CTkLabel(
            self, text="Configurações", font=("Arial", 40, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

        save_button = ctk.CTkButton(
            self,
            text="Salvar",
        ).grid(row=2, column=0, padx=10, pady=10, sticky="nw")

        quit_button = ctk.CTkButton(self, text="Voltar", command=self._back).grid(
            row=2, column=2, padx=10, pady=10, sticky="ne"
        )

    def _save(self, text_area):
        pass

    def _back(self):
        self.controller.get_view("MainPage")
