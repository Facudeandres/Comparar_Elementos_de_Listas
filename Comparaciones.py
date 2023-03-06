import streamlit as st
import pandas as pd
from dataclasses import dataclass

columna1_header = st.text_input("Ingrese el nombre de la columna 1")
columna1_data = st.text_area("Ingrese los datos de la columna 1")
columna2_header = st.text_input("Ingrese el nombre de la columna 2")
columna2_data = st.text_area("Ingrese los datos de la columna 2")

columna1_lista = columna1_data.split(",")
columna2_lista = columna2_data.split(",")
df = pd.DataFrame({columna1_header: columna1_lista, columna2_header: columna2_lista})

@dataclass
class Output:
    solo_col1: list
    solo_col2: list
    coincidencias: list

def comparar_columnas(columna1_lista, columna2_lista):
    output = Output([], [], [])
    for elemento in columna1_lista:
        if elemento not in columna2_lista:
            output.solo_col1.append(elemento)
    for elemento in columna2_lista:
        if elemento not in columna1_lista:
            output.solo_col2.append(elemento)
        else:
            output.coincidencias.append(elemento)
    return output

output = comparar_columnas(df[columna1_header], df[columna2_header])
st.write("Solo en " + columna1_header, output.solo_col1)
st.write("Solo en " + columna2_header, output.solo_col2)
st.write("Coincidencias", output.coincidencias)

with pd.ExcelWriter('output_comparacion.xlsx') as writer:
    pd.DataFrame({"solo en " + columna1_header: output.solo_col1}).to_excel(writer, sheet_name='output_comparacion', index=False, startcol=0)
    pd.DataFrame({"solo en " + columna2_header: output.solo_col2}).to_excel(writer, sheet_name='output_comparacion', index=False, startcol=1)
    pd.DataFrame({"Coincidencias": output.coincidencias}).to_excel(writer, sheet_name='output_comparacion', index=False, startcol=2)
