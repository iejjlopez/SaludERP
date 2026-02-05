import streamlit as st
from config.settings import apply_styles
from services.auth_service import AuthService
from views.login_view import render_login_page
from views.dashboard_view import render_dashboard
from views.doc_view import render_doc_page

def main():
    st.set_page_config(page_title="Salud ERP", page_icon="🏥", layout="wide")
    apply_styles()

    # Inicializar el estado de autenticación si no existe
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    # LÓGICA DE LOGIN
    if not st.session_state.authenticated:
        # Llamamos al login y capturamos el resultado
        auth = AuthService()
        user_data = render_login_page(auth)
        
        if user_data:
            st.session_state.authenticated = True
            st.session_state.user = user_data
            st.rerun()  # Forzar recarga para mostrar el Dashboard
    
    # LÓGICA DE DASHBOARD (Solo si ya está autenticado)
    else:
        with st.sidebar:
            st.title("🏥 Salud ERP")
            st.write(f"**{st.session_state.user.username}**")
            
            menu_option = st.selectbox("Menú", ["Dashboard", "Documentación"])
            st.divider()
            
            if st.button("Cerrar Sesión"):
                st.session_state.authenticated = False
                st.session_state.user = None
                st.rerun()

        if menu_option == "Dashboard":
            render_dashboard()
        else:
            render_doc_page()

if __name__ == "__main__":
    main()