import streamlit as st
import pandas as pd

def render_dashboard():
    st.header("📊 Tablero de Gestión Salud ERP")
    
    # Métricas superiores
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Pacientes (Total)", "4", "+1")
    col2.metric("Citas (Hoy)", "5", "0")
    col3.metric("Atenciones (Hoy)", "3", "-2")
    col4.metric("Alertas Stock Bajo", "2", "↑ 1")

    st.divider()

    # Sección de Gráficos y Tablas
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("🔝 Diagnósticos CIE-10")
        data = {"Diagnóstico": ["Diabetes", "Hipertensión", "Gastritis"], "Casos": [10, 15, 7]}
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index("Diagnóstico"))

    with c2:
        st.subheader("📦 Estado de Inventario")
        inv_data = {"Insumo": ["Gasa", "Alcohol", "Jeringas"], "Stock": [50, 12, 5]}
        st.table(pd.DataFrame(inv_data))