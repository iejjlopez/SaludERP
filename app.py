import streamlit as st
from config.settings import apply_styles
from services.auth_service import AuthService
from views.login_view import render_login_page
from views.dashboard_view import render_dashboard
from adapters.db_adapter import DBAdapter

# 1. Instanciar el adaptador
db = DBAdapter()

st.set_page_config(page_title="Salud ERP", layout="wide")
apply_styles()

if 'user' not in st.session_state:
    st.session_state.user = None

def main():
    if not st.session_state.user:
        render_login_page(AuthService())
    else:
        st.sidebar.title("🏥 Salud ERP")
        opcion = st.sidebar.selectbox("Módulos", ["Dashboard", "Configuración"])
        
        if opcion == "Dashboard":
            render_dashboard()
        elif opcion == "Configuración":
            # Implementación visual de la Marca Blanca
            st.write("## ⚙️ Configuración del Centro de Salud")
            
            # Cargar datos actuales
            config_actual = db.obtener_configuracion()
            nombre_ini = config_actual['nombre_clinica'].iloc[0] if not config_actual.empty else "Salud ERP"
            
            with st.form("form_config"):
                nombre = st.text_input("Nombre de la Clínica", value=nombre_ini)
                nit = st.text_input("NIT / Identificación Tributaria")
                dir_fisica = st.text_input("Dirección Física")
                
                if st.form_submit_button("Guardar Cambios Globales"):
                    db.guardar_configuracion(nombre, nit, dir_fisica)
                    st.success("Configuración actualizada en la base de datos")
            
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state.user = None
            st.rerun()

if __name__ == "__main__":
    main()