#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script de limpieza para los datos de audiencias
Utiliza el paquete `data-cleaner` para limpiar datos de
establecimientos-de-salud aplicando reglas de limpieza.

Versión data-cleaner=0.1.11
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import sys

from data_cleaner import DataCleaner

DEFAULT_INPUT_PATH = "establecimientos-de-salud-raw.csv"
DEFAULT_OUTPUT_PATH = "establecimientos-de-salud-clean.csv"

RULES = [
    {
        "string": [
            {"field": "financiamiento", "keep_original": False},
            {"field": "provincia", "keep_original": False},
            {"field": "localidad", "keep_original": False},
        ]
    }
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
