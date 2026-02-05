import sqlite3
import pandas as pd

class DBAdapter:
    def __init__(self, db_path="salud_erp.db"):
        self.db_path = db_path
        self._create_tables()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_tables(self):
        """Crea las tablas necesarias si no existen"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Tabla para Marca Blanca
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS configuracion (
                    id INTEGER PRIMARY KEY,
                    nombre_clinica TEXT,
                    nit TEXT,
                    direccion TEXT
                )
            """)
            # Tabla para métricas del Dashboard (Simulada)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS metricas (
                    clave TEXT PRIMARY KEY,
                    valor TEXT
                )
            """)
            conn.commit()

    def obtener_configuracion(self):
        """Recupera los datos de Marca Blanca"""
        query = "SELECT * FROM configuracion WHERE id = 1"
        with self._get_connection() as conn:
            return pd.read_sql_query(query, conn)

    def guardar_configuracion(self, nombre, nit, direccion):
        """Guarda o actualiza la identidad corporativa"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO configuracion (id, nombre_clinica, nit, direccion)
                VALUES (1, ?, ?, ?)
            """, (nombre, nit, direccion))
            conn.commit()