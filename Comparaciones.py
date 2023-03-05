import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(page_title="Comparacion de C/ elemento de las columnas")

st.header("Comparacion de C/ elemento de las columnas")

tabla1 = st.file_uploader("Cargar tabla 1", type=["csv", "xlsx"])
if tabla1 is not None:
    tabla1 = pd.read_csv(tabla1) if tabla1.name.endswith('.csv') else pd.read_excel(tabla1, engine='openpyxl')

tabla2 = st.file_uploader("Cargar tabla 2", type=["csv", "xlsx"])
if tabla2 is not None:
    tabla2 = pd.read_csv(tabla2) if tabla2.name.endswith('.csv') else pd.read_excel(tabla2, engine='openpyxl')

columna1 = st.selectbox("Seleccionar columna de tabla 1", tabla1.columns.tolist() if tabla1 is not None else [])
columna2 = st.selectbox("Seleccionar columna de tabla 2", tabla2.columns.tolist() if tabla2 is not None else [])

if st.button("Iniciar Comparacion") and tabla1 is not None and tabla2 is not None and columna1 and columna2:
    tabla1[columna1] = tabla1[columna1].astype(object)
    tabla2[columna2] = tabla2[columna2].astype(object)

    tabla1[columna1] = tabla1[columna1].apply(lambda x: str(x).lower())
    tabla2[columna2] = tabla2[columna2].apply(lambda x: str(x).lower())

    lista_a = tabla1[columna1].tolist()
    lista_b = tabla2[columna2].tolist()

    solo_a = [x for x in lista_a if x not in lista_b]
    solo_b = [x for x in lista_b if x not in lista_a]
    coincidencias = [x for x in lista_a if x in lista_b]

    output = pd.ExcelWriter('comparacion_columnas.xlsx', engine='openpyxl')
    tabla1.to_excel(output, sheet_name='Input Tablas', index=False)
    tabla2.to_excel
