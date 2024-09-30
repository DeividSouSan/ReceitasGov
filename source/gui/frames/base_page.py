import customtkinter as ctk


class BasePage(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk):
        ctk.CTkFrame.__init__(self, parent)

        self.controller = controller
