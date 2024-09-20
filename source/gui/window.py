import logging
import os
import tkinter as tk
from datetime import datetime

import customtkinter as ctk


class Window(ctk.CTk):
    def __init__(self, *args, **kwargs):

        # Define a aparência da janela e o tema padrão
        ctk.set_appearance_mode("dark-blue")
        ctk.set_default_color_theme("dark-blue")
        ctk.CTk.__init__(self, *args, **kwargs)

        # Configura a janela principal
        self.wm_title("Receitas Públicas - Portal da Transparência")
        self.wm_geometry("800x600")
        self.wm_resizable(False, False)
        self.iconphoto(
            False,
            tk.PhotoImage(
                file=os.path.join(os.getcwd(), "source", "gui", "icon", "billing.png")
            ),
        )

        # Configura o container principal
        self.container = ctk.CTkFrame(
            self, width=800, height=600, bg_color="black", corner_radius=0
        )
        self.container.pack(side="top", fill="both", expand=True)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

    def load_frames(self, frames: list[tk.Frame]):
        self.frames = dict()

        for F in frames:
            frame: ctk.CTkFrame = F(self.container, self)
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
