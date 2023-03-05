import streamlit as st
import pandas as pd
import openpyxl as px

# Configuración de la página de Streamlit
st.set_page_config(page_title="Comparación de elementos de listas", page_icon=":mag:", layout="wide")

# Título de la página
st.title("Comparación de elementos de listas")

# Ingreso de datos
st.header("Ingreso de datos")
st.write("Ingrese los títulos de las columnas y los elementos de las dos listas a comparar.")

titulo_col1 = st.text_input("Título columna 1")
titulo_col2 = st.text_input("Título columna 2")
columna1 = st.text_area("Columna 1 (separe los elementos con salto de línea)", height=250)
columna2 = st.text_area("Columna 2 (separe los elementos con salto de línea)", height=250)

# Conversión de las listas ingresadas a DataFrames de Pandas
df1 = pd.DataFrame(columna1.split("\n"), columns=[titulo_col1])
df2 = pd.DataFrame(columna2.split("\n"), columns=[titulo_col2])

# Comparación de los elementos de las listas
coincidencias = []
for index1, row1 in df1.iterrows():
    for index2, row2 in df2.iterrows():
        if row1[titulo_col1] == row2[titulo_col2]:
            coincidencias.append(row1[titulo_col1])

# Creación del DataFrame de resultado
df_resultado = pd.DataFrame({
    f"Solo en {titulo_col1}": df1.loc[~df1[titulo_col1].isin(df2[titulo_col2]), titulo_col1],
    f"Solo en {titulo_col2}": df2.loc[~df2[titulo_col2].isin(df1[titulo_col1]), titulo_col2],
    "Coincidencias": coincidencias
})

# Exportación del resultado a Excel
output_excel = px.Workbook()
hoja_input = output_excel.create_sheet("Input", 0)
hoja_output = output_excel.create_sheet("Output", 1)

for row_index, row_value in pd.concat([df1, df2], axis=1).iterrows():
    hoja_input.append([row_value[col] for col in [titulo_col1, titulo_col2]])

hoja_output.append([f"Solo en {titulo_col1}", f"Solo en {titulo_col2}", "Coincidencias"])
for row_index, row_value in df_resultado.iterrows():
    hoja_output.append([row_value[col] for col in df_resultado.columns])

# Descarga del archivo generado
def download_excel_file(df, filename):
    with open(filename, 'wb') as f:
        f.write(df)
    return f

excel_file = download_excel_file(px.writer.excel.save_virtual_workbook(output_excel), f"{titulo_col1}_{titulo_col2}.xlsx")
st.download_button(label="Descargar resultado", data=excel_file.getvalue(), file_name=f"{titulo_col1}_{titulo_col2}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
