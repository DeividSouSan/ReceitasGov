# ReceitasGov 🧾

O *ReceitasGov* é um software de automação que captura receitas do governo, processa os dados e os envia para um API.

## Tecnologias e Bibliotecas Utilizadas 📝
- **Python** (3.12.2)
- **Selenium:** biblioteca para automação de tarefas em navegadores.
- **Pandas:** biblioteca para manipulação e análise de dados.
- **Requests**: biblioteca para fazer requisições HTTP.
- **Custom Tkinter**: biblioteca para criar interfaces com Python.

Outras bibliotecas que foram utilizadas encontram-se no arquivo `requirements.txt`.

## Outras Funcionalidades ➕
### Logging
A biblioteca built-in `logging` do Python foi utilizada para fornecer algumas informações do status da execução do programa.

## Arquitetura 🏗
O sistema foi desenvolvido tentando seguir boas práticas de programação e arquitetura limpa. A maneira final como as classes do sistemas estão organizadas e estão relacionadas é a seguinte:

<div align="center">
  <img src="https://github.com/user-attachments/assets/4a15ab22-e56f-4b3f-ac28-f52adb104687"/>
</div>

## Desafios 🥊
### Importação Circular
Durante o desenvolvimento das interfaces do projeto, foi necessário lidar com *importações circulares*. A interface `WindowControllerI` e a classe `BaseView` se importavam de maneira paradoxal. Para solucionar isso utilizei o `TYPE_CHECKING` da biblioteca `typing` como condição para fazer as importações. Dessa maneira, somente durante a checagem de tipos é que ambas bibliotecas seriam importadas, evitando, assim, problemas durante a execução do código. As soluções podem ser verificadas dentro dos arquivos `window_controller_i.py` e `base_view.py`.

## Screenshots 📷
### Janela Principal
<div align="center">
  <img src="https://github.com/user-attachments/assets/cc873038-afeb-4a02-a151-e918750b4242"/>
</div>

### Janela Configurações
<div align="center">
  <img src="https://github.com/user-attachments/assets/f1aaacaa-0282-4d06-b616-c4d23bf944c9"/>
</div>

### Janela Logs
<div align="center">
  <img src="https://github.com/user-attachments/assets/807617f5-4219-4fdd-9c27-c4b7225a3a72"/>
</div>

## Como rodar o projeto?

### Clonando

Primeiro clone o repositório. Isso pode ser feito baixando-o ou utilizando o comando:

```bash
git clone git@github.com:DeividSouSan/ReceitasGov.git
```

Utilizando sua IDE ou Editor de Texto, abra o projeto. Se estiver pelo terminal acesse a pasta onde baixou ou clonou o projeto e digite:

```bash
cd ReceitasGov
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
Para rodar a aplicação entre no diretório do repositório (`ReceitasGov`) e digite no terminal:

```bash
python3 source/main.py
```
