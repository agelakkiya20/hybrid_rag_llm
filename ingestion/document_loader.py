
from pathlib import Path
from pypdf import PdfReader


def load_document(file_path):
    """
    Load text from PDF or TXT documents.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    extension = file_path.suffix.lower()

    if extension == ".txt":
        text = file_path.read_text(encoding="utf-8")

    elif extension == ".pdf":
        reader = PdfReader(str(file_path))

        pages = []

        for page in reader.pages:
            page_text = page.extract_text() or ""
            pages.append(page_text)

        text = "\n".join(pages)

    else:
        raise ValueError(
            "Unsupported file format. Use PDF or TXT."
        )

    return {
        "text": text,
        "metadata": {
            "source": file_path.name,
            "file_type": extension
        }
    }
