import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Fondo Oculis y tipografía legible */
        .stApp { background-color: #F8FAFC !important; }
        
        /* Corregir inputs para que no desaparezcan */
        .stTextInput input {
            background-color: white !important;
            color: #1E293B !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 8px !important;
        }
        
        /* Estilo del botón de Salud ERP */
        .stButton>button {
            background-color: #0F172A !important;
            color: white !important;
            border-radius: 8px;
            font-weight: 700;
            width: 100%;
        }
        
        /* Ocultar elementos nativos que rompen el diseño */
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)