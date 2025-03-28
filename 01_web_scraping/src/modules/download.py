import requests
from pathlib import Path
from typing import Dict

OUTPUT_DIR = "01_web_scraping/downloads"


def download_attachments(attachments: Dict[str, str], output_dir: str = OUTPUT_DIR) -> None:
    """Baixa os anexos a partir das URLs encontradas."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    session = requests.Session()

    for filename, url in attachments.items():
        try:
            file_path = Path(output_dir) / filename
            print(f"Baixando o arquivo {filename}...")

            response = session.get(url, stream=True, timeout=10)
            response.raise_for_status()

            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Download concluído com sucesso: {file_path}")
        except Exception as e:
            print(f"Erro ao baixar {filename}: {e}")


def verify_downloads(attachments: Dict[str, str], output_dir: str = OUTPUT_DIR) -> bool:
    """Verifica se os arquivos baixados existem e não estão corrompidos."""
    all_files_ok = True

    for filename in attachments.keys():
        file_path = Path(output_dir) / filename
        if not file_path.exists():
            print(f"Erro: Arquivo não encontrado - {file_path}")
            all_files_ok = False
        elif file_path.stat().st_size == 0:
            print(f"Erro: Arquivo vazio - {file_path}")
            all_files_ok = False

    if all_files_ok:
        print("Todos os arquivos foram baixados corretamente!")
    else:
        print("Alguns arquivos apresentaram problemas!")

    return all_files_ok
