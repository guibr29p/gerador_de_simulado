import streamlit as st
from dotenv import load_dotenv
import pandas as pd
from interfece import home, quetion
import os

load_dotenv()

collection_dir = os.getenv("collection_dir")
print(collection_dir)
collection: list[str] = None


def chage_session(session):
    st.session_state.collection = session


with st.sidebar:
    if st.button("novas quertoes"):
        chage_session(session="home")
        st.rerun()

    st.divider()
    st.subheader("All Collections")
     
    if os.path.exists(collection_dir):
        collection = [d for d in os.listdir(collection_dir) if os.path.isdir
                      (os.path.join(collection_dir, d))]
        
        for collectionFile in collection:

            if st.button(collectionFile):
                st.session_state.collection = collectionFile
                st.rerun()
            
            
if "collection" not in st.session_state:
    chage_session("home")

print(st.session_state.collection, collection)

if st.session_state.collection == "home":
    home.show()
elif st.session_state.collection in collection:
    quetion.show(st.session_state.collection)