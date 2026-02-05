import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. Fondo Global Uniforme (Gris Azulado Profesional) */
        .stApp { 
            background-color: #F1F5F9 !important; 
        }
        
        /* 2. Tipografía y Textos (Color Pizarra Oscuro para contraste total) */
        .stMarkdown, p, h1, h2, h3, span, label, .stMetric {
            color: #1E293B !important;
        }

        /* 3. Tarjetas de Métricas y Contenedores Blancos */
        div[data-testid="stMetric"], .stTable, .stDataFrame {
            background-color: #FFFFFF !important;
            padding: 20px !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
            border: 1px solid #E2E8F0 !important;
        }

        /* 4. Inputs (Login y Buscadores): Bordes visibles y definidos */
        .stTextInput > div > div > input {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            border: 1px solid #94A3B8 !important;
            border-radius: 8px !important;
            height: 45px !important;
        }

        /* 5. Botones de Acción (Color Azul Marino ERP) */
        .stButton>button {
            background-color: #0F172A !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            font-weight: 600 !important;
            width: 100% !important;
            padding: 0.5rem 1rem !important;
        }
        
        .stButton>button:hover {
            background-color: #1E293B !important;
            border: none !important;
        }

        /* 6. Sidebar Oscuro (Contraste con el área de trabajo) */
        [data-testid="stSidebar"] {
            background-color: #0F172A !important;
        }
        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }

        /* 7. Limpieza de Header y Espacios */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 2rem !important;
        }
        </style>
    """, unsafe_allow_html=True)