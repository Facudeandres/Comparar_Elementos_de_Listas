import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(page_title="Comparación de columnas", page_icon=":guardsman:")

# Título de la página
st.title("Comparación de columnas")

# Texto para ingresar los títulos de las columnas
col1_title = st.text_input("Título de la columna 1", "Columna 1")
col2_title = st.text_input("Título de la columna 2", "Columna 2")

# Texto para ingresar las columnas de cadenas de caracteres
col1_input = st.text_area(f"Ingrese los valores para {col1_title}")
col2_input = st.text_area(f"Ingrese los valores para {col2_title}")

# Botón para comparar
if st.button("Comparar"):
    # Separar los valores de cada columna por líneas y convertirlos en listas
    col1_values = col1_input.split("\n")
    col2_values = col2_input.split("\n")

    # Crear un dataframe con las columnas
    df = pd.DataFrame({col1_title: col1_values, col2_title: col2_values})

    # Comparar las columnas y crear una tercera columna con los resultados
    df["Resultados"] = df.apply(lambda x: "Coincidencia" if x[col1_title] == x[col2_title] else "Solo en " + col1_title if x[col1_title] not in col2_values else "Solo en " + col2_title if x[col2_title] not in col1_values else "", axis=1)

    # Crear un archivo Excel con dos hojas: la primera con el input y la segunda con el output
    output = pd.ExcelWriter("comparacion_columnas.xlsx")
    df.to_excel(output, sheet_name="Input", index=False)
    df["Resultados"].value_counts().to_frame().to_excel(output, sheet_name="Output")
    output.save()

    # Descargar el archivo Excel
    st.download_button(
        label="Descargar resultados",
        data=output,
        file_name="comparacion_columnas.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

