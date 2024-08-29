from datetime import datetime
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from data.data_processing import DataProcess
from bots.bot_receitas import RevenueBot
from api.requests.post import post_to_api
import json
import logging
import os
import configparser

# Verificando se os diretórios existem, caso contrário, criar
path = os.getcwd()

if os.path.exists("logs"):
    pass
else:
    os.mkdir("logs")

if os.path.exists("csv"):
    pass
else:
    os.mkdir("csv")
    
# Carregando os dados do arquivo de configuração
def read_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config

try:
    config = read_config(f"{path}/config/config.ini")
except Exception:
    logging.warning("Arquivo de configuração não encontrado.")
    sys.exit()

# Configurações de Log
log_filename = f"{path}/logs/logs_{datetime.now().strftime('%d%m%Y_%H_%M_%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

logging.info(f"Iniciando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}...")

# Funções para executar as ações dos botões
def run_bot():
    bot = RevenueBot(config["Download"]["WEBSITE_URL"],
                      int(config["Download"]["DOWNLOAD_TIME"]))
    bot.start()

    data_handler = DataProcess(config["Author"]["AUTHOR"])
    columns = config["Data"]["COLUMNS"].split(",")
    data_json = data_handler.handle_data(columns)
    data_handler.output_data(data_json)

    post_to_api(config["API"]["API_URL"])
    
    messagebox.showinfo("Sucesso", "Dados enviados para API com sucesso, o arquivo com a saída enviada também foi gerado e pode se acessado no diretório 'output'.")

def open_file():
    # Abrir diálogo para selecionar o arquivo
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo:",
        filetypes=[("Arquivos de Log", "*.log"), ("Arquivos JSON", "*.json")]
    )

    if not file_path:
        return  

    # Cria uma janela
    open_file_window = tk.Toplevel()
    open_file_window.title("Leitor de Logs")
    open_file_window.geometry(config["WindowSizes"]["LOGS_WINDOW_SIZE"])

    # Criar uma área de texto para exibir o conteúdo do arquivo
    text_area = tk.Text(open_file_window, wrap=tk.WORD)
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Criar um botão para abrir o arquivo
    open_button = tk.Button(
        open_file_window, text="Abrir Arquivo", command=open_file)
    open_button.pack(pady=10)

    open_button = tk.Button(open_file_window, text="Sair",
                            command=open_file_window.destroy)
    open_button.pack(pady=10)

    try:
        # Ler e exibir o conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as file:
            if file_path.endswith('.json'):
                conteudo = json.dumps(
                    json.load(file), indent=4, ensure_ascii=False)
            else:
                conteudo = file.read()

        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, conteudo)

        messagebox.showinfo("Sucesso", f"Arquivo {file_path} carregado com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")

def configs_action():

    def save():
        new_content = text_area.get("1.0", tk.END)

        try:
            with open(f"{path}/config/config.ini", 'w') as env_file:
                env_file.write(new_content)
            messagebox.showinfo(
                "Sucesso", "Configurações salvas com sucesso. Reinicie o programa para aplicar as mudanças.")
        except Exception as e:
            messagebox.showerror(
                "Erro", f"Falha ao salvar as configurações: {e}")

    # Criar a nova janela para configurações
    config_window = tk.Toplevel(root)
    config_window.title("Configurações")
    config_window.geometry(config["WindowSizes"]["CONFIG_WINDOW_SIZE"])

    # Ler o conteúdo do arquivo .ini
    try:
        with open(f"{path}/config/config.ini", 'r') as env_file:
            content = env_file.read()
    except FileNotFoundError:
        content = ""

    # Criar uma área de texto para editar o conteúdo do .env
    text_area = tk.Text(config_window, height=5)
    text_area.insert(tk.END, content)
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Criar botão "Salvar"
    salvar_button = tk.Button(
        config_window, text="Salvar", command=save)
    salvar_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Criar botão "Sair"
    quit_button = tk.Button(config_window, text="Sair",
                            command=config_window.destroy)
    quit_button.pack(side=tk.RIGHT, padx=10, pady=10)

def close():
    logging.info(f"Finalizando o programa: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}...")
    root.destroy()


# Criar a janela principal
root = tk.Tk()
root.title(config["Bot"]["BOT_NAME"])

# Definir tamanho da janela
root.geometry(config["WindowSizes"]["MAIN_WINDOW_SIZE"])

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Criar o título
title_label = tk.Label(root, text=config["Bot"]["BOT_NAME"], font=("Helvetica", 16, "bold"))
title_label.grid(row=0, columnspan=3, pady=10, sticky='nsew')

# Cria botão para abrir os logs ou saídas
logs_button = tk.Button(root, text="Logs", command=open_file)
logs_button.grid(row=0, column=3, sticky='nsew')

# Criar o subtítulo
subtitle_label = tk.Label(root, text=config["Bot"]["BOT_DESC"], font=("Helvetica", 12))
subtitle_label.grid(row=1, columnspan=3, pady=5, sticky='nsew')

# Label com o status da página
status_label = tk.Label(root, text=RevenueBot.get_status(config["Download"]["WEBSITE_URL"]), font=("Helvetica", 10))
status_label.grid(row=2, columnspan=3, pady=15, sticky='nsew')

# Criar os botões princípais
start_button = tk.Button(root, text="Start", command=run_bot)
start_button.grid(row=3, column=0, sticky='nsew')

configs_button = tk.Button(root, text="Configs", command=configs_action)
configs_button.grid(row=3, column=1, sticky='nsew')

quit_button = tk.Button(root, text="Sair", command=close)
quit_button.grid(row=3, column=2, sticky='nsew')

# Iniciar o loop da interface
root.mainloop()
