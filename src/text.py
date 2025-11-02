from pathlib import Path

# pedir o caminho da pasta
caminho_pasta = input("Digite o caminho da pasta: ").strip().strip('"')
pasta = Path(caminho_pasta)

if pasta.exists() and pasta.is_dir():
    # listar todos os arquivos da pasta
    arquivos = list(pasta.iterdir())
    print(f"Arquivos encontrados na pasta '{pasta}':")
    for arquivo in arquivos:
        if arquivo.is_file():
            print(arquivo.name)
else:
    print("A pasta não existe.")