import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* Forzar fondo claro y sólido para legibilidad */
        .stApp { 
            background-color: #F1F5F9 !important; 
        }
        
        /* Hacer que las métricas y textos sean visibles (Oscuros) */
        .stMarkdown, p, h1, h2, h3, span {
            color: #1E293B !important;
        }

        /* Contenedores de tarjetas del Dashboard */
        div[data-testid="stMetric"] {
            background-color: white !important;
            padding: 15px !important;
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
        }

        /* Ajuste de la barra lateral (Sidebar) */
        [data-testid="stSidebar"] {
            background-color: #0F172A !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Eliminar espacios vacíos superiores */
        .block-container {
            padding-top: 1rem !important;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)