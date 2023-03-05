import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

# función para comparar elementos
def comparar_elementos(columna_a, columna_b):
    solo_en_a = []
    solo_en_b = []
    coincidencias = []
    for a in columna_a:
        if a not in columna_b:
            solo_en_a.append(a)
    for b in columna_b:
        if b not in columna_a:
            solo_en_b.append(b)
        else:
            coincidencias.append(b)
    return solo_en_a, solo_en_b, coincidencias

# interfaz de usuario
st.title("Comparación de C/ elemento de las columnas")
st.sidebar.title("Elija los nombres de las columnas")

# selección de los nombres de las columnas
nombre_columna_a = st.sidebar.text_input("Nombre de la columna A", "A")
nombre_columna_b = st.sidebar.text_input("Nombre de la columna B", "B")

# entrada de datos
texto_a = st.text_area("Introduzca elementos para la columna A, uno por línea")
texto_b = st.text_area("Introduzca elementos para la columna B, uno por línea")
separador = st.sidebar.text_input("Separador", ",")

if st.button("Iniciar comparación"):
    # procesamiento de datos
    lista_a = [float(x) if '.' in x else int(x) if x.isdigit() else x for x in texto_a.split('\n')]
    lista_b = [float(x) if '.' in x else int(x) if x.isdigit() else x for x in texto_b.split('\n')]
    solo_en_a, solo_en_b, coincidencias = comparar_elementos(lista_a, lista_b)

    # salida de datos
    output = pd.ExcelWriter('comparacion_columnas.xlsx')
    df_input = pd.DataFrame({nombre_columna_a: lista_a, nombre_columna_b: lista_b})
    df_input.to_excel(output, sheet_name='Input', index=False)
    df_output = pd.DataFrame({f"Solo en {nombre_columna_a}": solo_en_a, f"Solo en {nombre_columna_b}": solo_en_b, "Coincidencias": coincidencias})
    df_output.to_excel(output, sheet_name='Output', index=False)
    output.save()

    # descarga de archivo
    with open('comparacion_columnas.xlsx', 'rb') as f:
        bytes_data = f.read()
    b64 = base64.b64encode(bytes_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="comparacion_columnas.xlsx">Descargar archivo Excel</a>'
    st.markdown(href, unsafe_allow_html=True)
