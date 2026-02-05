import streamlit as st

def render_doc_page():
    st.title("📖 Centro de Recursos Médicos")
    
    tab1, tab2, tab3 = st.tabs(["Manual de Uso", "Buscador CIE-10", "Vademécum"])
    
    with tab1:
        st.header("Manual del Sistema")
        st.markdown("""
        - **Dashboard**: Monitoreo de indicadores clave.
        - **Login**: Acceso seguro con credenciales `ADMINGENERAL`.
        """)

    with tab2:
        st.header("Buscador de Diagnósticos (CIE-10)")
        busqueda = st.text_input("Ingrese código o nombre del diagnóstico")
        # Diccionario simulado para la demo
        cie10 = {
            "E11": "Diabetes mellitus tipo 2",
            "I10": "Hipertensión esencial (primaria)",
            "J00": "Rinofaringitis aguda (resfriado común)",
            "K29": "Gastritis y duodenitis"
        }
        if busqueda:
            resultados = {k: v for k, v in cie10.items() if busqueda.upper() in k or busqueda.lower() in v.lower()}
            st.write(resultados if resultados else "No se encontraron coincidencias.")

    with tab3:
        st.header("Diccionario de Medicamentos")
        meds = {
            "Paracetamol": "500mg - Analgésico y antipirético.",
            "Metformina": "850mg - Antidiabético oral.",
            "Loratadina": "10mg - Antihistamínico.",
            "Omeprazol": "20mg - Protector gástrico."
        }
        selected_med = st.selectbox("Seleccione un medicamento", list(meds.keys()))
        st.info(f"**Indicación**: {meds[selected_med]}")