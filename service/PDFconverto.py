from PyPDF2 import PdfReader
from typing import IO
from pathlib import Path


def opeFile(caminho) -> IO[bytes]:
    with open(caminho, "fb") as file:
        return file


def extrect_text(caminho):
    text: str = ""
    file = Path(caminho)

    try:
        if file.is_file():
            reader = PdfReader(file)
            
            for pages in reader.pages:
                text += pages.extract_text() or ""
        
        else:
            if file.exists() and file.is_dir():

                for File in list(file.iterdir()):
                    reader = PdfReader(File)
                    for pages in reader.pages:
                        text += pages.extract_text() or ""
                                           
    except FileExistsError:
        print("arquibo não encotrado")
    except Exception as e: 
        print(f"Erro de leitura de arquivo: {e.args}") 

    return text or ""