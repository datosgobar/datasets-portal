# coding: utf-8

"""
Script de limpieza para los datos de contratos
Utiliza el paquete `data-cleaner` para limpiar datos de audiencias aplicando
reglas de limpieza.

Version: 0.1.10

"""
from data_cleaner import DataCleaner
import pandas as pd
import sys
# input_path = "contratos_vigentes_2015.csv"
# DEFAULT_OUTPUT_PATH = "clear_contratos_vigentes_2015.csv"

DEFAULT_INPUT_PATH = "contratos-hasta-2015-raw.csv"
DEFAULT_OUTPUT_PATH_VIGENTE = "contratos-2015-clean.csv"
DEFAULT_OUTPUT_PATH1_HISTORICO = "contratos-historico-clean.csv"

RULES = [

    {
        "nombre_propio": [
            {"field": "titulo"},
            {"field": "financiacion"},
            {"field": "nombre_organismo"},
            {"field": "apellido"},
            {"field": "nombre"},
        ]
    },
    {
        "fecha_simple": [
            {"field": "desde", "time_format": "YYYY/MM/DD"},
            {"field": "hasta", "time_format": "YYYY/MM/DD"},
            {"field": "alta_fecha", "time_format": "YYYY/MM/DD"},
            {"field": "mod_fecha", "time_format": "YYYY/MM/DD"},
        ]
    },

        {"reemplazar": [
            {
            "field": "locacion",
            "replacements": {"Servicios": ["Serv"]}
            }
        ]
    },

     {"renombrar_columnas": [
        {"field": "alta_fecha", "new_field": "fecha_alta_registro_rcpc"},
        {"field": "mod_fecha", "new_field": "fecha_modificacion_registro_rcpc"}
    ]},

    {"remover_columnas": [
        {"field": "estudios"},
        {"field": "titulo"},
        {"field": "nivel_grado"},
        {"field": "id_unico"},
        {"field": "nacimiento"}
    ]}
]




def custom_cleaning_before_rules(dc):
    """Script de limpieza custom para aplicar al objeto antes de las reglas.
    Args:
        dc (DataCleaner): Objeto data cleaner con datos cargados.
    """
    pass


def custom_cleaning_after_rules(dc):
    """Script de limpieza custom para aplicar al objeto después de las reglas.
    Args:
        dc (DataCleaner): Objeto data cleaner con datos cargados.
    """
    pass


def clean_file(input_path, output_path):
    """Limpia los datos del input creando un nuevo archivo limpio."""
    print("Comenzando limpieza...")
    dc = DataCleaner(input_path, encoding='Latin 1')
    custom_cleaning_before_rules(dc)
    dc.clean(RULES)
    custom_cleaning_after_rules(dc)
    y = 2015
    dc.df.hasta = pd.to_datetime(dc.df.hasta, yearfirst=True)
    dc.df.desde = pd.to_datetime(dc.df.desde, yearfirst=True)
    gii = dc.df.desde.dt.year == y
    gif = dc.df.hasta.dt.year == y
    gis = (dc.df.desde.dt.year < y) & (dc.df.hasta.dt.year > y)
    givig = gii | gif | gis
    df1 = dc.df[givig]
    gin2016 = dc.df.desde.dt.year == 2016
    df2 = dc.df[~gin2016]
    df1.set_index(df1.columns[0]).to_csv(
        DEFAULT_OUTPUT_PATH_VIGENTE, encoding=dc.OUTPUT_ENCODING,
        separator=dc.OUTPUT_SEPARATOR,
        quotechar=dc.OUTPUT_QUOTECHAR)
    df2.set_index(df2.columns[0]).to_csv(
        DEFAULT_OUTPUT_PATH1_HISTORICO, encoding=dc.OUTPUT_ENCODING,
        separator=dc.OUTPUT_SEPARATOR,
        quotechar=dc.OUTPUT_QUOTECHAR)

    print("Limpieza finalizada exitosamente!")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        clean_file(DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH_VIGENTE)
    elif len(sys.argv) == 2:
        clean_file(sys.argv[1], DEFAULT_OUTPUT_PATH_VIGENTE)
    elif len(sys.argv) == 3:
        clean_file(sys.argv[1], sys.argv[2])
    else:
        print("{} no es una cantidad de argumentos aceptada.".format(
            len(sys.argv) - 1
        ))
