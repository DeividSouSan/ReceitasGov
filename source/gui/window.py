import logging
import tkinter as tk

from gui.frames.config_page import ConfigPage
from gui.frames.main_page import MainPage
from gui.frames.read_files_page import ReadFilePage


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Bot - Receitas e Despesas do Governo")
        self.wm_geometry("800x600")

        container = tk.Frame(self, width=800, height=600)
        container.pack(side="top", fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        for F in [MainPage, ConfigPage, ReadFilePage]:
            frame: tk.Frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

        logging.info("Janela principal carregada com sucesso.")

    def show_frame(self, cont):
        selected_frame = self.frames[cont]
        frame_name = str(selected_frame).replace("frame", "").replace(".!", "")
        logging.info(f"Frame {frame_name} selecionado.")
        selected_frame.tkraise()
