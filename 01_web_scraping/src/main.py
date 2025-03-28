from modules.scraping import get_attachment_links
from modules.download import download_attachments, verify_downloads
from modules.compression import compress_attachments


def main() -> None:
    attachments = get_attachment_links()
    if attachments:
        download_attachments(attachments)
        if verify_downloads(attachments):
            compress_attachments(attachments)
        else:
            print("Erro na verificação dos downloads. A compactação foi cancelada.")
    else:
        print("Nenhum anexo encontrado.")


if __name__ == "__main__":
    main()
