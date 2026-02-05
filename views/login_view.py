import streamlit as st

def render_login_page(auth_service):
    st.title("Gestión inteligente para tu clínica")
    
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("Ingresar al Sistema"):
        # Llamada al servicio con el nombre correcto validate_user
        user_data = auth_service.validate_user(user_input, pass_input)
        
        if user_data:
            st.success(f"Bienvenido {user_data.username}")
            return user_data  # CRÍTICO: Sin esto app.py no avanza
        else:
            st.error("Credenciales inválidas")
            return None
    return None