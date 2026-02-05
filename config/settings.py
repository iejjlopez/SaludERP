import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* Fondo General y tipografía legible */
        .stApp { 
            background-color: #F8FAFC !important; 
        }
        
        /* Eliminar espacio superior del header oculto */
        .block-container {
            padding-top: 0rem !important;
            margin-top: -2rem;
        }

        /* Corregir inputs para que no desaparezcan visualmente */
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
            border: none;
            padding: 0.6rem;
        }
        
        /* Ocultar elementos nativos de Streamlit */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)