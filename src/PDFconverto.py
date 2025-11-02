from PyPDF2 import PdfReader
from typing import IO


def extrect_text(file: IO[bytes]) -> str:
    reader = PdfReader(file)
    text: str = ""
    for pages in reader.pages:
        text += pages.extract_text() or ""

    return text

