#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script de limpieza para los datos de audiencias

Utiliza el paquete `data-cleaner` para limpiar datos de audiencias aplicando
reglas de limpieza.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import sys

from data_cleaner import DataCleaner

DEFAULT_INPUT_PATH = "audiencias-raw.csv"
DEFAULT_OUTPUT_PATH = "audiencias-clean.csv"

RULES = [
    {
        "nombre_propio": [
            {"field": "dependencia", "keep_original": False}
        ]
    },
    {
        "string": [
            {"field": "lugar", "keep_original": False},
            {"field": "sintesis", "keep_original": False},
            {"field": "objeto", "keep_original": False},
            {"field": "dependencia", "keep_original": False},
            {"field": "interes_invocado", "keep_original": False},
            {"field": "datos_representado", "keep_original": False}
        ]
    },
    {
        "fecha_separada": [
            {"fields": [["fecha_audiencia", "DD-MM-YYYY"],
                        ["hora_audiencia", "HH:mm"]],
             "new_field_name": "audiencia",
             "keep_original": True}
        ]
    },
    {
        "fecha_simple": [
            {"field": "fecha_solicitud",
             "time_format": "DD-MM-YYYY",
             "keep_original": False}
        ]
    },
    {
        "string_simple_split": [
            {"field": "sujeto_obligado",
             "separators": [", Cargo:", "Cargo:"],
             "new_field_names": ["nombre", "cargo"],
             "keep_original": True}
        ]
    },
    {
        "nombre_propio": [
            {"field": "sujeto_obligado_nombre", "keep_original": False},
            {"field": "sujeto_obligado_cargo", "keep_original": False}
        ]
    },
    {
        "string": [
            {"field": "sujeto_obligado_nombre", "keep_original": False},
            {"field": "sujeto_obligado_cargo", "keep_original": False}
        ]
    },
    {
        "string_peg_split": [
            {"field": "datos_solicitante",
             "grammar": """
            allowed_char = anything:x ?(x not in '1234567890() ')
            nombre = ~('DNI') <allowed_char+>:n ws -> n.strip()
            number = <digit+>:num -> int(num)

            nom_comp = <nombre+>:nc -> nc.strip()
            cargo = '(' <nombre+>:c ')' -> c.strip()
            dni = ','? ws 'DNI' ws number:num -> num

            values = nom_comp:n ws cargo?:c ws dni?:d ws anything* -> [n, c, d]
             """,
             "new_field_names": ["nombre", "cargo", "dni"],
             "keep_original": True}
        ]
    },
    {
        "nombre_propio": [
            {"field": "datos_solicitante_nombre", "keep_original": False}
        ]
    },
    {
        "string": [
            {"field": "datos_solicitante_nombre", "keep_original": False}
        ]
    },
]


def clean_file(input_path, output_path):
    """Limpia los datos del input creando un nuevo archivo limpio."""
    print("Comenzando limpieza...")
    dc = DataCleaner(input_path)
    dc.clean_file(RULES, output_path)
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
