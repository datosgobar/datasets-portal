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

RULES = [
    {
        "remover_columnas": [
            {"field": "obligadodependenciaid"},
            {"field": "obligadoid"},
            {"field": "dependenciaid"},
            {"field": "dependencia_depende"},
            {"field": "dependencia_posicion"},
            {"field": "rootdependenciaid"},
            {"field": "solicitanteid"},
            {"field": "solic_personajuridica"},
            {"field": "tipointeresinvocadoid"},
            {"field": "tipocaracterid"},
            {"field": "representadoid"},
            {"field": "tipoestadoid"},
            {"field": "tipoestadonorealizadaid"},
            {"field": "obligadoasesorid"},
            {"field": "dependenciadescripcion"},

        ]
    },
    {
        "nombre_propio": [
            {"field": "obligado_cargo", "keep_original": False},
            {"field": "obligado_apellido", "keep_original": False},
            {"field": "obligado_nombre", "keep_original": False},
            {"field": "dependencia_descripcion", "keep_original": False},
            {"field": "rootdependenciadescripcion", "keep_original": False},
            {"field": "solic_apellido", "keep_original": False},
            {"field": "solic_nombre", "keep_original": False},
            {"field": "solic_cargo", "keep_original": False},
            {"field": "interes_invocado", "keep_original": False},
            {"field": "desc_caracter", "keep_original": False},
            {"field": "representado_apellido", "keep_original": False},
            {"field": "desc_estado", "keep_original": False},
            {"field": "obligadoasesorcargo", "keep_original": False},
            {"field": "asesor_apellido", "keep_original": False},
            {"field": "asesor_nombre", "keep_original": False},
            {"field": "asesor_cargo", "keep_original": False},
        ]
    },
    {
        "string": [
            {"field": "obligado_cargo", "keep_original": False},
            {"field": "obligado_apellido", "keep_original": False},
            {"field": "obligado_nombre", "keep_original": False},
            {"field": "dependencia_descripcion", "keep_original": False},
            {"field": "rootdependenciadescripcion", "keep_original": False},
            {"field": "solic_apellido", "keep_original": False},
            {"field": "solic_nombre", "keep_original": False},
            {"field": "solic_cargo", "keep_original": False},
            {"field": "interes_invocado", "keep_original": False},
            {"field": "desc_caracter", "keep_original": False},
            {"field": "representado_apellido", "keep_original": False},
            {"field": "desc_estado", "keep_original": False},
            {"field": "obligadoasesorcargo", "keep_original": False},
            {"field": "asesor_apellido", "keep_original": False},
            {"field": "asesor_nombre", "keep_original": False},
            {"field": "asesor_cargo", "keep_original": False},
        ]
    },
    {"fecha_completa": [
        {"field": "fechaaudiencia", "time_format": "YY-MM-DD HH:mm:ss"},
    ]},
    {"fecha_simple": [
        {"field": "fechasolicitud", "time_format": "YY-MM-DD HH:mm:ss"},
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
