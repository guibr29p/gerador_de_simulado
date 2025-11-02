import PDFconverto
import tkinter
from pathlib import Path

print("coloque o link do arquivo")
caminho_pdf = input("Coloque o link do arquivo: ").strip().strip('"')
print(PDFconverto.extrect_text(caminho_pdf))




