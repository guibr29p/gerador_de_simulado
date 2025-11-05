import streamlit as st
import pandas as pd
import os
from typing import cast
from dotenv import load_dotenv

load_dotenv()
collection_dir = os.getenv("collection_dir")


def get_key(question_itens, r):
    for i in range(1, len(question_itens)+1):
        print(f"verificao valor: {question_itens[f"resposta{i}"]["texto"]} bool: {r == question_itens[f"resposta{i}"]["texto"]}\n")
        if r == question_itens[f"resposta{i}"]["texto"]:
            print(f"key function: {f"resposta{i}"}")
            return f"resposta{i}"


def show(file):
    print(f"{collection_dir}/{file}/q{file}.json")
    dt = pd.read_json(f"{collection_dir}/{file}/q{file}.json", orient="records")

    for index, question_iten in dt.iterrows():
        print(index)
        if "file" not in st.session_state:
            st.session_state.file = {
                file: {
                    index: ""
                }
            }
        elif file not in st.session_state.file.keys():
            st.session_state.file[file] = {
                index: ""
            }
        else: 
            st.session_state.file[file][index] = ""

        st.write(question_iten["enunciado"])
        r = st.radio("resposta ", [
            question_iten["resposta1"]["texto"],
            question_iten["resposta2"]["texto"],
            question_iten["resposta3"]["texto"],
            question_iten["resposta4"]["texto"]
        ])
    
        st.session_state.file[file][index] = get_key(question_itens=question_iten, r=r) or ""
        key = st.session_state.file[file][index] 
        
        print(question_iten[key]["correta"])
        if question_iten[key]["correta"] is True:
            st.write(f":green[resposta: {r}]")
        elif question_iten[key]["correta"] is False:
            st.write(f":red[resposta: {r}]")
        else:
            st.write(f"resposta: {r}")
        
    if st.button("enviar"):
        st.rerun()