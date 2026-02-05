import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* Fondo sólido y limpio */
        .stApp { 
            background-color: #F8FAFC !important; 
        }
        
        /* Títulos en azul oscuro para resaltar */
        h1, h2, h3 {
            color: #1E293B !important;
            font-weight: 700 !important;
        }

        /* Tarjetas de métricas con borde suave */
        div[data-testid="stMetric"] {
            background-color: white !important;
            padding: 20px !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
            border: 1px solid #E2E8F0 !important;
        }

        /* Mejorar legibilidad de las tablas (DataFrames) */
        .stDataFrame td, .stDataFrame th {
            color: #334155 !important;
            font-size: 14px !important;
        }

        /* Sidebar elegante */
        [data-testid="stSidebar"] {
            background-color: #1E293B !important;
        }
        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }

        /* Botón de Cerrar Sesión */
        .stButton>button {
            border-radius: 6px !important;
            transition: 0.3s;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)