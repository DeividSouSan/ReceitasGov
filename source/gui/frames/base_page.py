import customtkinter as ctk


class BasePage(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame):
        ctk.CTkFrame.__init__(self, parent, fg_color="#23272a")
