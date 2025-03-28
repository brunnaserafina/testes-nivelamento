import requests
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
ATTACHMENTS = {"Anexo I": "anexoI.pdf", "Anexo II": "anexoII.pdf"}


def get_attachment_links() -> dict[str, str] | None:
    """Busca os links para download dos anexos I e II na página da ANS."""
    try:
        print(f"Conectando ao site: {URL}")

        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        found_links = {}

        for attachment_name, filename in ATTACHMENTS.items():
            link = soup.find(
                "a", string=lambda text: text and attachment_name in text)

            if link and "href" in link.attrs:
                found_links[filename] = link["href"]
                print(
                    f"Encontrado link para {attachment_name}: {link['href']}")
            else:
                print(
                    f"Aviso: Não foi encontrado o link para: {attachment_name}")

        return found_links if found_links else None

    except requests.exceptions.RequestException as error:
        print(f"Erro ao acessar a página: {error}")
        return None
    except Exception as error:
        print(f"Ocorreu um erro inesperado: {error}")
        return None
