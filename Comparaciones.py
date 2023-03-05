import streamlit as st
import pandas as pd
import openpyxl as px

# Título de la página
st.title("Comparar elementos de dos columnas")

# Ingreso de los títulos de las columnas
titulo_columna_1 = st.text_input("Ingrese el título de la columna 1:")
titulo_columna_2 = st.text_input("Ingrese el título de la columna 2:")

# Ingreso de las columnas de datos
columna_1 = st.text_area("Ingrese la columna 1 (separe los elementos con salto de línea):")
columna_2 = st.text_area("Ingrese la columna 2 (separe los elementos con salto de línea):")

# Dividir las cadenas de entrada en listas
lista_1 = [x.strip() for x in columna_1.split('\n') if x.strip()]
lista_2 = [x.strip() for x in columna_2.split('\n') if x.strip()]

# Comparación de las listas
solo_en_a = sorted(set(lista_1) - set(lista_2))
solo_en_b = sorted(set(lista_2) - set(lista_1))
coincidencias = sorted(set(lista_1) & set(lista_2))

# Visualización de los resultados
st.write("Resultado:")
df_resultado = pd.DataFrame({
    f"Solo en {titulo_columna_1}": solo_en_a,
    f"Solo en {titulo_columna_2}": solo_en_b,
    "Coincidencias": coincidencias
})
st.write(df_resultado)

# Descargar en excel
output = pd.ExcelWriter('comparacion_columnas.xlsx')
df_input = pd.DataFrame({
    titulo_columna_1: lista_1,
    titulo_columna_2: lista_2
})
df_input.to_excel(output, sheet_name='Input', index=False)
df_resultado.to_excel(output, sheet_name='Output', index=False)
output.save()
button = '<a href="comparacion_columnas.xlsx" download="comparacion_columnas.xlsx">Descargar resultado en Excel</a>'
st.markdown(button, unsafe_allow_html=True)

