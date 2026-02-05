import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. Fondo de la App: Gris azulado claro para evitar deslumbramiento */
        .stApp { 
            background-color: #F1F5F9 !important; 
        }
        
        /* 2. Forzar color de texto oscuro en toda la app */
        .stMarkdown, p, h1, h2, h3, span, label {
            color: #1E293B !important;
        }

        /* 3. Tarjetas de Métricas: Fondo blanco sólido con texto azul oscuro */
        div[data-testid="stMetric"] {
            background-color: #FFFFFF !important;
            padding: 20px !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
            border: 1px solid #E2E8F0 !important;
        }
        /* Forzar visibilidad de los números de las métricas */
        div[data-testid="stMetricValue"] > div {
            color: #0F172A !important;
            font-weight: 800 !important;
        }

        /* 4. Inputs del Login: Bordes definidos y fondo blanco */
        .stTextInput input {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            border: 2px solid #CBD5E1 !important;
        }

        /* 5. Sidebar: Color oscuro para contraste total */
        [data-testid="stSidebar"] {
            background-color: #0F172A !important;
        }
        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        /* 6. Eliminar el espacio blanco superior */
        .block-container {
            padding-top: 1.5rem !important;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)