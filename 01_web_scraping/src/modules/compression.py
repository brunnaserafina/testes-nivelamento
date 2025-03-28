import zipfile
from pathlib import Path
from typing import Dict
from modules.download import OUTPUT_DIR


def compress_attachments(attachments: Dict[str, str], output_dir: str = OUTPUT_DIR) -> bool:
    """Compacta os arquivos PDF"""
    try:
        existing_files = [
            Path(output_dir) / filename
            for filename in attachments.keys()
            if (Path(output_dir) / filename).exists()
        ]

        if not existing_files:
            raise FileNotFoundError(
                "Nenhum arquivo encontrado para compactação.")

        zip_path = Path(output_dir) / "anexos.zip"

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in existing_files:
                zipf.write(file)
                print(f"Arquivo adicionado ao ZIP: {file}")

        print(f"Arquivos compactados com sucesso em {zip_path}!")
        return True

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("Erro inesperado ao compactar os anexos: {e}")

    return False
