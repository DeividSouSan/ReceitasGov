import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog
from dotenv import load_dotenv
from data.data_processing import DataProcess
from bots.receipts_bot import ReceiptsBot
from api_requests.send_post_req import send_post_request
import json

load_dotenv()

BOT_NAME = os.getenv('BOT_NAME')
BOT_DESC = os.getenv('BOT_DESC')
CONFIG_WINDOW_SIZE = os.getenv('CONFIG_WINDOW_SIZE')
MAIN_WINDOW_SIZE = os.getenv('MAIN_WINDOW_SIZE')
LOGS_WINDOW_SIZE = os.getenv('LOGS_WINDOW_SIZE')
AUTHOR = os.getenv('AUTHOR')
WEBSITE_URL = os.getenv('WEBSITE_URL')
DOWNLOAD_PATH = os.getenv('DOWNLOAD_FOLDER_PATH') # Deixe vazio para baixar na pasta Downloads
DOWNLOAD_TIME = int(os.getenv('DOWNLOAD_TIME'))
OUTPUT_PATH = os.getenv('OUTPUT_PATH')
API_URL = os.getenv('API_URL')


def start_action():
    bot = ReceiptsBot(WEBSITE_URL, DOWNLOAD_PATH, DOWNLOAD_TIME)
    bot.start()
    
    data = DataProcess(AUTHOR, DOWNLOAD_PATH)
    data_json = data.get_json(log=True)
    data.process(data_json, log=True)
    
    send_post_request(API_URL, OUTPUT_PATH)

def abrir_arquivo():
    # Abrir diálogo para selecionar o arquivo
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Arquivos JSON", "*.json"), ("Arquivos de Texto", "*.txt")]
    )
    
    if not file_path:
        return  # Se o usuário cancelar, a função retorna
    
    # Cria uma janela
    open_file_window = tk.Toplevel()
    open_file_window.title("Leitor de Logs")
    open_file_window.geometry("600x500")

    # Criar uma área de texto para exibir o conteúdo do arquivo
    text_area = tk.Text(open_file_window, wrap=tk.WORD)
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Criar um botão para abrir o arquivo
    open_button = tk.Button(open_file_window, text="Abrir Arquivo", command=abrir_arquivo)
    open_button.pack(pady=10)
    
    open_button = tk.Button(open_file_window, text="Sair", command=open_file_window.destroy)
    open_button.pack(pady=10)
    
    try:
        # Ler e exibir o conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as file:
            if file_path.endswith('.json'):
                conteudo = json.dumps(json.load(file), indent=4, ensure_ascii=False)
            else:
                conteudo = file.read()
        
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, conteudo)
        
        messagebox.showinfo("Sucesso", f"Arquivo {file_path} carregado com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")

def configs_action():
    
    def salvar_config():
        novo_conteudo = text_area.get("1.0", tk.END)
        
        try:
            with open('.env', 'w') as env_file:
                env_file.write(novo_conteudo)
            messagebox.showinfo("Sucesso", "Configurações salvas com sucesso. Reinicie o programa para aplicar as mudanças.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar as configurações: {e}")

    # Criar a nova janela para configurações
    config_window = tk.Toplevel(root)
    config_window.title("Configurações")
    config_window.geometry(CONFIG_WINDOW_SIZE)

    # Ler o conteúdo do arquivo .env
    try:
        with open('.env', 'r') as env_file:
            conteudo = env_file.read()
    except FileNotFoundError:
        conteudo = ""

    # Criar uma área de texto para editar o conteúdo do .env
    text_area = tk.Text(config_window, height=5)
    text_area.insert(tk.END, conteudo)
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Criar botão "Salvar"
    salvar_button = tk.Button(config_window, text="Salvar", command=salvar_config)
    salvar_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Criar botão "Sair"
    sair_button = tk.Button(config_window, text="Sair", command=config_window.destroy)
    sair_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Criar a janela principal
root = tk.Tk()
root.title(BOT_NAME)

# Definir tamanho da janela
root.geometry(MAIN_WINDOW_SIZE)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Criar o título
title_label = tk.Label(root, text=BOT_NAME, font=("Helvetica", 16, "bold"))
title_label.grid(row=0, columnspan=3, pady=10, sticky='nsew')

logs_button = tk.Button(root, text="Logs", command=abrir_arquivo)
logs_button.grid(row=0, column=3, sticky='nsew')

# Criar o subtítulo
subtitle_label = tk.Label(root, text=BOT_DESC, font=("Helvetica", 12))
subtitle_label.grid(row=1, columnspan=3, pady=5, sticky='nsew')

status_label = tk.Label(root, text=ReceiptsBot.get_status(WEBSITE_URL), font=("Helvetica", 10))
status_label.grid(row=2, columnspan=3, pady=15, sticky='nsew')

# Criar os botões
start_button = tk.Button(root, text="Start", command=start_action)
start_button.grid(row=3, column=0, sticky='nsew')

configs_button = tk.Button(root, text="Configs", command=configs_action)
configs_button.grid(row=3, column=1, sticky='nsew')

sair_button = tk.Button(root, text="Sair", command=root.destroy())
sair_button.grid(row=3, column=2, sticky='nsew')

# Iniciar o loop da interface
root.mainloop()
