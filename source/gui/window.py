import logging
import os
import tkinter as tk
from datetime import datetime

import customtkinter as ctk


class Window(ctk.CTk):
    def __init__(self, frames: list[tk.Frame], *args, **kwargs):

        ctk.set_appearance_mode("dark-blue")
        ctk.set_default_color_theme("dark-blue")
        ctk.CTk.__init__(self, *args, **kwargs)

        self.wm_title("Receitas Públicas - Portal da Transparência")
        self.wm_geometry("800x600")
        self.wm_resizable(False, False)
        self.iconphoto(
            False,
            tk.PhotoImage(
                file=os.path.join(os.getcwd(), "source", "gui", "icon", "billing.png")
            ),
        )

        container = ctk.CTkFrame(
            self, width=800, height=600, bg_color="black", corner_radius=0
        )
        container.pack(side="top", fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        for F in frames:
            frame: ctk.CTkFrame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        main_frame = next(iter(self.frames.keys()))
        self.show_frame(main_frame)

        logging.info(
            f"Iniciando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}..."
        )
        logging.info("Janela principal carregada com sucesso.")

    def show_frame(self, cont):
        selected_frame = self.frames[cont]
        frame_name = str(selected_frame).replace("frame", "").replace(".!", "")
        selected_frame.tkraise()

        logging.info(f"Frame {frame_name} carregado.")
