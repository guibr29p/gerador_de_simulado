import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
collection_dir = os.getenv("collection_dir")


def show(file):
    print(f"{collection_dir}/{file}/q{file}.json")
    dt = pd.read_json(f"{collection_dir}/{file}/q{file}.json", orient="records")

    print(dt.head)
    for _, question_iten in dt.iterrows():
        
        st.write(question_iten["enunciado"])
        st.radio("resposta ", [
            question_iten["resposta1"]["texto"],
            question_iten["resposta1"]["texto"],
            question_iten["resposta1"]["texto"],
            question_iten["resposta1"]["texto"],
            question_iten["resposta1"]["texto"]
        ])