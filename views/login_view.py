import streamlit as st

def render_login_page(auth_service):
    # Barra superior de idioma
    st.markdown('<div style="text-align: right; padding: 0 50px; color: #64748B;">🌐 Idioma: <b>Español</b> ▾</div>', unsafe_allow_html=True)

    # Layout de columnas para centrar la tarjeta
    _, center_col, _ = st.columns([0.1, 0.8, 0.1])

    with center_col:
        # Contenedor dividido tipo Oculis
        col_hero, col_form = st.columns([1, 1], gap="medium")

        with col_hero:
            st.markdown(f"""
                <div style="background-color: #0F172A; padding: 60px; border-radius: 30px 0 0 30px; color: white; min-height: 550px;">
                    <div style="font-size: 24px; font-weight: 800; margin-bottom: 40px;">💙 Salud ERP</div>
                    <h1 style="color: white; font-size: 40px;">Gestión inteligente para tu clínica.</h1>
                    <p style="color: #94A3B8; font-size: 16px;">Control total de pacientes e inventarios con IA.</p>
                    <div style="margin-top: 100px; font-size: 12px; color: #475569;">Confían en nosotros +500 centros en Latam</div>
                </div>
            """, unsafe_allow_html=True)

        with col_form:
            st.markdown("""
                <div style="background: white; padding: 40px; border-radius: 0 30px 30px 0; border: 1px solid #E2E8F0; min-height: 550px;">
            """, unsafe_allow_html=True)
            
            # Selector de Perfil
            perfil = st.radio("PERFIL", ["Administración", "Pacientes"], horizontal=True, label_visibility="collapsed")
            st.markdown("<br>", unsafe_allow_html=True)

            # Inputs de texto con etiquetas claras para evitar errores
            user_input = st.text_input("EMAIL / USUARIO", placeholder="ej. ADMINGENERAL")
            pass_input = st.text_input("CONTRASEÑA", type="password", placeholder="••••••••")
            
            st.markdown('<div style="text-align: right; font-size: 12px; color: #3B82F6;">¿Olvidaste tu contraseña?</div>', unsafe_allow_html=True)
            
            if st.button("Ingresar al Sistema →"):
                # Llamada al servicio de lógica
                user_data = auth_service.validate_user(user_input, pass_input)
                if user_data:
                    st.session_state.user = user_data
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")

            # Footer de tarjetas Demo/Gratis
            st.markdown("""
                    <div style="display: flex; gap: 10px; margin-top: 40px;">
                        <div style="flex:1; padding: 10px; border: 1px solid #E2E8F0; border-radius: 12px; text-align: center; font-size: 12px;"><b>Ver Demo</b></div>
                        <div style="flex:1; padding: 10px; border: 1px solid #E2E8F0; border-radius: 12px; text-align: center; font-size: 12px; border-left: 4px solid #10B981;"><b>Cuenta Gratis</b></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)