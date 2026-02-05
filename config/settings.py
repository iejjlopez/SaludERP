import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* 1. Fondo de la App: Forzamos un tono gris azulado muy suave para reducir el brillo */
        .stApp { 
            background-color: #F1F5F9 !important; 
        }
        
        /* 2. Forzar texto oscuro: Evita que los números y etiquetas se pierdan en el fondo */
        .stMarkdown, p, h1, h2, h3, span, label, .stMetric {
            color: #1E293B !important;
        }

        /* 3. Tarjetas de Métricas: Fondo blanco puro con bordes definidos para que resalten */
        div[data-testid="stMetric"] {
            background-color: #FFFFFF !important;
            padding: 20px !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
            border: 1px solid #CBD5E1 !important;
        }

        /* 4. Inputs del Login: Les damos un borde oscuro para que no desaparezcan en el blanco */
        .stTextInput > div > div > input {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            border: 2px solid #94A3B8 !important;
        }

        /* 5. Sidebar: Mantenerlo oscuro para un contraste total con el área de trabajo */
        [data-testid="stSidebar"] {
            background-color: #0F172A !important;
        }
        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }

        /* 6. Eliminar espacios superiores innecesarios */
        .block-container {
            padding-top: 1rem !important;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)