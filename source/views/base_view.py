from typing import TYPE_CHECKING

import customtkinter as ctk

if TYPE_CHECKING:
    from controllers.window_controller_i import WindowControllerI


class BaseView(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: "WindowControllerI"):
        self._create_view(parent)

        self.controller = controller

    def _create_view(self, parent: ctk.CTkFrame):
        ctk.CTkFrame.__init__(self, parent)
