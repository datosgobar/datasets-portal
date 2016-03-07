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
#input_path = "contratos_vigentes_2015.csv"
#DEFAULT_OUTPUT_PATH = "clear_contratos_vigentes_2015.csv"

DEFAULT_INPUT_PATH  = "contratos-hasta-2015-raw.csv"
DEFAULT_OUTPUT_PATH = "contratos-hasta-2015-clean.csv"

RULES =[

    {
        "nombre_propio": [
            {"field": "titulo"},
            {"field": "financiacion"},
            {"field": "nombre_organismo"},
            {"field": "apellido"},
            {"field": "nombre"},
            {"field": "denominacion_del_organismo"},
            {"field": "tipo_organismo"},
            {"field": "jurisdiccion"},
            {"field": "FH_Desactivado"},

        ]
    },
    {
        "fecha_simple": [
            {"field": "desde", "time_format": "YYYY/MM/DD"},
            {"field": "hasta", "time_format": "YYYY/MM/DD"},
            {"field": "alta_fecha", "time_format": "YYYY/MM/DD"},
            {"field": "mod_fecha", "time_format": "YYYY/MM/DD"},
            {"field": "fecha_ultimo_envio", "time_format": "YYYY/MM/DD"},


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
        {"field": "id_unico_borrar"},
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
    dc.save(output_path)
    print("Limpieza finalizada exitosamente!")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        clean_file(DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH)
    elif len(sys.argv) == 2:
        clean_file(sys.argv[1], DEFAULT_OUTPUT_PATH)
    elif len(sys.argv) == 3:
        clean_file(sys.argv[1], sys.argv[2])
    else:
        print("{} no es una cantidad de argumentos aceptada.".format(
            len(sys.argv) - 1
        ))
