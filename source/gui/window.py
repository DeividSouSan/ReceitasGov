import logging
import os
import tkinter as tk
from datetime import datetime


class Window(tk.Tk):
    def __init__(self, frames: list[tk.Frame], *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Bot - Receitas e Despesas do Governo")
        self.wm_geometry("800x600")

        container = tk.Frame(self, width=800, height=600)
        container.pack(side="top", fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        for F in frames:
            frame: tk.Frame = F(container, self)
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
