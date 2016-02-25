# coding: utf-8

from data_cleaner import DataCleaner
import pandas as pd

#input_path = "contratos_vigentes_2015.csv"
#output_path = "clear_contratos_vigentes_2015.csv"

input_path = "contratos_hasta_2015.csv"
output_path = "clear_contratos_hasta_2015.csv"

df = pd.read_csv(input_path, encoding="utf8")

df


rules = [
    
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


dc = DataCleaner(input_path)

dc.clean_file(rules, output_path)
