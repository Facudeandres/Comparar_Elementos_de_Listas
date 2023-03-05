import streamlit as st
import pandas as pd

def comparar_columnas(col_a, col_b, title_a, title_b):
    lista_a = col_a.strip().split('\n')
    lista_b = col_b.strip().split('\n')
    
    solo_a = []
    solo_b = []
    coincidencias = []
    for elemento in lista_a:
        if elemento not in lista_b:
            solo_a.append(elemento)
        else:
            coincidencias.append(elemento)
    for elemento in lista_b:
        if elemento not in lista_a:
            solo_b.append(elemento)
    
    df_solo_a = pd.DataFrame({'Solo en A': solo_a})
    df_solo_b = pd.DataFrame({'Solo en B': solo_b})
    df_coincidencias = pd.DataFrame({
        title_a: coincidencias,
        title_b: coincidencias
    })
    
    return df_solo_a, df_solo_b, df_coincidencias

st.title('Comparación de Columnas')
st.write('Ingrese los datos de las columnas')

# Columna 1
st.subheader('Columna 1')
title_a = st.text_input('Ingrese el título de la columna 1', 'Columna 1')
col_a = st.text_area('Ingrese los valores de la columna 1')

# Columna 2
st.subheader('Columna 2')
title_b = st.text_input('Ingrese el título de la columna 2', 'Columna 2')
col_b = st.text_area('Ingrese los valores de la columna 2')

# Botón para iniciar la comparación
if st.button('Iniciar Comparación'):
    df_solo_a, df_solo_b, df_coincidencias = comparar_columnas(col_a, col_b, title_a, title_b)
    
    # Descarga de archivo en formato Excel
    output = pd.ExcelWriter('comparacion_columnas.xlsx')
    df_solo_a.to_excel(output, sheet_name='Solo en A', index=False)
    df_solo_b.to_excel(output, sheet_name='Solo en B', index=False)
    df_coincidencias.to_excel(output, sheet_name='Coincidencias', index=False)
    output.save()
    
    st.write('Comparación realizada con éxito.')
    
    # Botón para descargar archivo
    if st.button('Descargar archivo Excel'):
        with open('comparacion_columnas.xlsx', 'rb') as f:
            bytes_data = f.read()
        st.download_button(
            label='Descargar archivo',
            data=bytes_data,
            file_name='comparacion_columnas.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
