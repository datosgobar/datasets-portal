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

DEFAULT_INPUT_PATH = "anses-direccion-oficinas-raw.csv"
DEFAULT_OUTPUT_PATH = "anses-direccion-oficinas-clean.csv"

RULES = [
    {
        "nombre_propio": [
            {"field": "descripcion", "keep_original": False},
            {"field": "domicilio", "keep_original": False},
            {"field": "provincia", "keep_original": False}
        ]
    },
    {
        "string": [
            {"field": "provincia", "keep_original": False},
        ]
    },
    {
        "string_regex_substitute": [
            {"field": "descripcion",
             "regex_str_match": "Udai",
             "regex_str_sub": "UDAI",
             "keep_original": False,
             }
        ]
    }
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
    dc = DataCleaner(input_path)
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
