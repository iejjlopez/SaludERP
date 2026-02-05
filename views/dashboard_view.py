import streamlit as st
import pandas as pd

def render_dashboard():
    # Título del Tablero
    st.markdown("## 📊 Tablero de Gestión Salud ERP")
    
    # 1. Fila de Métricas Principales (KPIs)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Pacientes (Total)", value="4", delta="+1")
    with m2:
        st.metric(label="Citas (Hoy)", value="5", delta="0")
    with m3:
        st.metric(label="Atenciones (Hoy)", value="3", delta="-2")
    with m4:
        st.metric(label="Alertas Stock Bajo", value="2", delta="1", delta_color="inverse")

    st.markdown("---")

    # 2. Fila de Gráficas
    g1, g2 = st.columns(2)
    
    with g1:
        st.markdown("### 🔝 Diagnósticos CIE-10")
        # Datos simulados para la gráfica de dona
        data_cie = pd.DataFrame({
            "Diagnóstico": ["J00", "J100", "Z000"],
            "Cantidad": [33.3, 33.3, 33.3]
        })
        st.write("Distribución de diagnósticos frecuentes")
        st.divider() # Simulación visual del gráfico circular

    with g2:
        st.markdown("### 📦 Estado de Inventario")
        # Gráfica de barras
        st.write("Disponibilidad de medicamentos críticos")
        st.divider() # Simulación visual de la gráfica de stock

    st.markdown("---")

    # 3. Estado de la Aplicación (Tablas de Backend/Frontend)
    st.markdown("### 🖥️ Estado de la Aplicación")
    t1, t2 = st.columns(2)
    
    with t1:
        st.caption("BACKEND")
        df_back = pd.DataFrame([
            {"Métrica": "Conexión BD", "Valor": "🟢 Activa", "Estado": "Estable"},
            {"Métrica": "Tamaño DB", "Valor": "36.0 KB", "Estado": "Saludable"}
        ])
        st.table(df_back)

    with t2:
        st.caption("FRONTEND")
        df_front = pd.DataFrame([
            {"Métrica": "Interfaz", "Valor": "🟢 Operativo", "Estado": "Reactivo"},
            {"Métrica": "Widgets", "Valor": "🟢 Sincronizado", "Estado": "Listo"}
        ])
        st.table(df_front)