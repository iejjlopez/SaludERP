import streamlit as st
from config.settings import apply_styles
from services.auth_service import AuthService
from views.login_view import render_login_page
from views.dashboard_view import render_dashboard
from views.doc_view import render_doc_page

def main():
    # Configuración de página de Streamlit
    st.set_page_config(
        page_title="Salud ERP - Gestión Clínica",
        page_icon="🏥",
        layout="wide"
    )

    # Aplicar estilos CSS personalizados
    apply_styles()

    # Manejo de estado de sesión para autenticación
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user = None

    # Lógica de navegación
    if not st.session_state.authenticated:
        # Renderizar login si no está autenticado
        user_data = render_login_page(AuthService())
        if user_data:
            st.session_state.authenticated = True
            st.session_state.user = user_data
            st.rerun()
    else:
        # Sidebar para navegación una vez logueado
        with st.sidebar:
            st.title("🏥 Salud ERP")
            st.write(f"Usuario: **{st.session_state.user.username}**")
            st.write(f"Rol: {st.session_state.user.role}")
            
            st.divider()
            
            # Selector de módulos
            menu_option = st.selectbox(
                "Módulos",
                ["Dashboard", "Documentación"]
            )
            
            st.divider()
            
            if st.button("Cerrar Sesión"):
                st.session_state.authenticated = False
                st.session_state.user = None
                st.rerun()

        # Renderizar la vista seleccionada
        if menu_option == "Dashboard":
            render_dashboard()
        elif menu_option == "Documentación":
            render_doc_page()

if __name__ == "__main__":
    main()