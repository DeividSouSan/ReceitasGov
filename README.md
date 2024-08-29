# Bot Receitas do Governo

O *GovReceitasRPA* é um software de automação que captura receitas do governo, processa os dados e os envia para um API.

## Tecnologias e Bibliotecas Utilizadas
- **Python** (3.12.2)
- **Selenium:** biblioteca para automação de tarefas em navegadores.
- **Pandas:** biblioteca para manipulação e análise de dados.
- **Requests**: biblioteca para fazer requisições HTTP.
- **Tkinter**: biblioteca para criar interfaces com Python.

Outras bibliotecas que foram utilizadas encontram-se no arquivo `requirements.txt`.

## Outras Funcionalidades
### Logging
A biblioteca built-in `logging` do Python foi utilizada para fornecer algumas informações do status da execução do programa.
### Configurações
Para conseguir configurar a aplicação dinâmicamente, algumas variáveis foram adicionadas ao arquivo de configuração `config.ini`. Caso alguma alteração dentro desse arquivo seja feita durante a execução do programa, ele deve ser reiniciado.

## Screenshots
### Janela Principal
<div align="center">
  <img src="https://github.com/user-attachments/assets/aa6015d2-5236-4614-a9a9-f036901bc6a3"/>
</div>

### Janela Configurações
<div align="center">
  <img src="https://github.com/user-attachments/assets/d6129e5a-1a64-4442-bfbf-74b6591b1f43"/>
</div>

### Janela Logs
<div align="center">
  <img src="https://github.com/user-attachments/assets/7e68d36b-0694-4cc2-a9d4-4707271e2afe"/>
</div>

## Como rodar o projeto?

### Clonando

Primeiro clone o repositório. Isso pode ser feito baixando-o ou utilizando o comando:

```bash
git clone git@github.com:DeividSouSan/GovReceitasRPA.git
```

Utilizando sua IDE ou Editor de Texto, abra o projeto. Se estiver pelo terminal acesse a pasta onde baixou ou clonou o projeto e digite: 

```bash
cd GovReceitasRPA
```

### Ambiente Virtual

Dentro da pasta do projeto, inicie um ambiente virtual. É recomendado instalar as bibliotecas em um ambiente virtual para evitar conflitos de versões com os pacotes instalados globalmente. Pelo terminal, crie um ambiente virtual utilizando:

```bash
python3 -m venv <nome_do_ambiente_virtual>
```

Geralmente o nome utilizado é `.venv`, mas isso é de sua escolha.

Para ativar o ambiente virutal no linux:

```bash
source .venv/bin/activate
```

Ou

```bash
. .venv/bin/activate
```

Para desativa-lo:

```bash
deactivate
```

No windows:
```bash
.venv/Scripts/activate
```

Para desativa-lo:

```bash
.venv/Scripts/deactivate
```

### Bibliotecas
Para baixar as bibliotecas utilizadas, verifique se o ambiente virtual está ativado e digite no terminal:

```bash
pip install -r requirements.txt
```

Assim, todas as dependencias que estão dentro do arquivo `requirements.txt` serão baixadas para o ambiente virtual.

### Rodando
Para rodar a aplicação escreva entre no diretório do repositório (`GovReceitasRPA`) e digite no terminal:

```bash
python3 main.py
```
