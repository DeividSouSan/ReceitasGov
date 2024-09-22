import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk


class ReadFilePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent

        ctk.CTkFrame.__init__(self, parent, fg_color="#23272a")

        title = ctk.CTkLabel(
            self,
            text="Leitura de Arquivos",
            font=("Arial", 40, "bold"),
            text_color="#ffffff",
        )
        title.pack(pady=10)

        # Criar uma área de texto para exibir o conteúdo do arquivo
        global text_area
        text_area = ctk.CTkTextbox(self, wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH, padx=50, pady=10)
        text_area.insert(
            tk.END, "Primeiro, selecione um arquivo para exibir o conteúdo."
        )

        # Criar um botão para abrir o arquivo
        open_button = ctk.CTkButton(self, text="Abrir Arquivo", command=self.open_file)
        open_button.pack(pady=10)

        open_button = ctk.CTkButton(self, text="Sair", command=self.back)
        open_button.pack(pady=10)

    def open_file(self):
        # Abrir diálogo para selecionar o arquivo
        initial_dir = os.path.join(os.getcwd(), "source/logs")
        file_path = filedialog.askopenfilename(
            title="Selecione um arquivo:",
            initialdir=initial_dir,
            filetypes=[("Arquivos de Log", "*.log"), ("Arquivos JSON", "*.json")],
        )

        if not file_path:
            return

        try:
            # Ler e exibir o conteúdo do arquivo
            with open(file_path, "r", encoding="utf-8") as file:
                if file_path.endswith(".json"):
                    content = json.dumps(json.load(file), indent=4, ensure_ascii=False)
                else:
                    content = file.read()

            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

            messagebox.showinfo(
                "Sucesso", f"Arquivo {file_path} carregado com sucesso."
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo.")

    def back(self):
        from gui.frames.main_page import MainPage

        self.controller.show_frame(MainPage)
