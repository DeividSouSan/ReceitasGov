def get_page_status(url) -> bool:
    """
    Função que verifica se a página está online ou offline.

    Args:
        url (str): URL da página a ser verificada.

    Returns:
        bool: True se a página estiver online, False se estiver offline.
    """
    import requests

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False
