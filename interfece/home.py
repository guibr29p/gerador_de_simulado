from service import PDFconverto, gerator_quetion
import pandas as pd
import streamlit as st
import os
from pathlib import Path
import json


collection_dir = os.getenv("collection_dir")


# salvar alquivo localmente
def request_save(files, file_dir_save) -> list[str]:
    list_dir: list[str] = []
    for file in files:     
        save_path = Path(file_dir_save, file.name)
        print(save_path.as_posix())
        list_dir.append(save_path.as_posix())
        with open(save_path, mode='wb') as w:
            w.write(file.getvalue())
    
        if save_path.exists():
            st.success(f'File {file.name} is successfully saved!')
    
    print(list_dir)
    return list_dir
            

# extrair texto de mutiplos arquivos 
def texto_extrect(dir_file_List: list[str]) -> str:
    contexto = ""
    for dir_file in dir_file_List:
        contexto = f"{PDFconverto.extrect_text(dir_file)} \n"

    return contexto


def save_json(json_list, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            # Usa json.dump para escrever o objeto no arquivo.
            # indent=4 deixa o arquivo JSON fácil de ler.
            json.dump(json_list, f, ensure_ascii=False, indent=4)

        print(f"\nObjeto salvo com sucesso no arquivo: {os.path.abspath(nome_arquivo)}")

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar a string JSON: {e}")
    except IOError as e:
        print(f"Erro de E/S ao salvar o arquivo: {e}")


# todo menu home
def show():
    print(collection_dir)
    list_difficulty = {
        "facil",
        "Medio",
        "dificil"
    }

    name: str = st.text_input("question name")
    
    files = st.file_uploader(
        "escolha seu arquivo",
        accept_multiple_files=True,
        type=["pdf"],
    )
    
    text_area = st.text_input("coloque seu link", placeholder="escreva um link para um site aqui")
        
    max_question = None
    
    col1, col2 = st.columns(2)
    with col1:
        max_question = st.number_input("maximo de questão", min_value=1,
                                       step=1, value=1)
    with col2:
        difficulty = st.selectbox(label="difficulty",
                                  options=list_difficulty,
                                  index=0,
                                  accept_new_options=False)
        
    # clicl do botão e gerar as quertoes e seus arquivos
    if st.button("gerar"):
        name_folde = fr"{collection_dir}/{name}"  # dir do arquirvo
        chat = gerator_quetion.chat()
        contexto = ""  # todo o texto dos arquivos aqui
        try:
            os.makedirs(name=fr"{collection_dir}/{name}" or name_folde)
            list_dir = request_save(files=files, file_dir_save=name_folde)
            print("list dir: ", list_dir)
            contexto = texto_extrect(list_dir)
            prompt = chat.format_system_prompt(difficulty, max_question)
            menssagem = chat.geration_quetion(contexto, prompt)
            print("menssagem: ", menssagem)
            json_list = json.loads(s=menssagem)  # transforma texto em json
            print(json_list)
            save_json(json_list=json_list, nome_arquivo=f"{name_folde}\\q{name}.json")

        except Exception as e:
            print(e)

        finally: 
            st.rerun()
