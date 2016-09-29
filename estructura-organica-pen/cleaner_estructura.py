#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script de limpieza para los datos de audiencias

Utiliza el paquete `data-cleaner` para limpiar datos de audiencias aplicando
reglas de limpieza disponibles en el paquete, reglas extendidas sobre el objeto
MyDataCleaner y cualquier script de limpieza custom que deba aplicarse antes o
después de las reglas.

Típicamente, el usuario puede tener que aplicar filtros, recortes o tareas muy
específicas para ese dataset antes de aplicar reglas de limpieza. Estas tareas
no buscarían implementar una nueva regla de limpieza en la clase extensible
MyDataCleaner sino que se escribirían en los métodos provistos que actúan antes
o después de la aplicación de reglas.

Versión del data-cleaner: 0.1.15
"""


from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import sys

from data_cleaner import DataCleaner

DEFAULT_INPUT_PATH = "estructura-organica-raw.csv"
DEFAULT_OUTPUT_PATH = "estructura-organica-clean.csv"

RULES = [
    {
        "renombrar_columnas": [
            {"field": "aut_dni", "new_field": "autoridad_dni"},
            {"field": "aut_cuit_cuil", "new_field": "autoridad_cuil_cuit"},
            {"field": "aut_cargo", "new_field": "autoridad_cargo"},
            {"field": "aut_tratamiento", "new_field": "autoridad_tratamiento"},
            {"field": "aut_apellido", "new_field": "autoridad_apellido"},
            {"field": "aut_nombre", "new_field": "autoridad_nombre"},
            {"field": "aut_norma_designacion",
                "new_field": "autoridad_norma_designacion"},
            {"field": "norma_competenciasobjetivos",
                "new_field": "norma_competencias_objetivos"},
            {"field": "cordigo_postal", "new_field": "codigo_postal"}
        ]
    },
    {
        "string": [
            {"field": "jurisdiccion", "keep_original": False},
            {"field": "unidad", "keep_original": False},
            {"field": "reporta_a", "keep_original": False},
            {"field": "unidad_tipo", "keep_original": False},
            {"field": "autoridad_cargo", "keep_original": False},
            {"field": "autoridad_tratamiento", "keep_original": False},
            {"field": "autoridad_apellido", "keep_original": False},
            {"field": "autoridad_nombre", "keep_original": False},
            {"field": "piso_oficina", "keep_original": False},
            {"field": "codigo_postal", "keep_original": False},
            {"field": "domicilio", "keep_original": False},
            {"field": "localidad", "keep_original": False},
            {"field": "provincia", "keep_original": False},
        ]
    },
    {
        "string_regex_substitute": [
            {"field": "norma_competencias_objetivos", "regex_str_match": ";", "regex_str_sub": ",",
             "keep_original": False},
            {"field": "unidad", "regex_str_match": "\(.*\)", "regex_str_sub": "",
             "keep_original": False},
            {"field": "provincia", "regex_str_match": "Bs\. As\.", "regex_str_sub": "Buenos Aires",
             "keep_original": False},
            {"field": "autoridad_tratamiento", "regex_str_match": "\s+$", "regex_str_sub": "",
             "keep_original": False},
            {"field": "autoridad_tratamiento", "regex_str_match": "(.+{^\.})$", "regex_str_sub": "\g<1>.",
             "keep_original": False},
            {"field": "autoridad_norma_designacion", "regex_str_match": "Dto\D*", "regex_str_sub": "Decreto ",
             "keep_original": False},
            {"field": "web", "regex_str_match": "^.+www\.", "regex_str_sub": "http://www.",
             "keep_original": False},
        ]
    },
    {
        "mail_format": [
            {"field": "mail"}
        ]
    },
    {
        "reemplazar_string": [
            {"field": "piso_oficina", "replacements": {
                "Oficina": ["Of.icina"]}},
            {"field": "piso_oficina", "replacements": {"Piso": ["Planta"]}}
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


class MyDataCleaner(DataCleaner):
    """Extensión del DataCleaner que permite agregar nuevas reglas.

    El método clean_file() utiliza esta clase extendible del DataCleaner para
    permitir el agregado de nuevos métodos de limpieza que sean necesarios, en
    un formato que haga sencilla su posterior portación al paquete original."""

    def nueva_regla(self, field, sufix=None, keep_original=False,
                    inplace=False):
        """One liner sobre lo que hace la regla.

        Descripción extendida (si correponde) sobre lo que hace la regla.

        Args:
            field (str): Campo a limpiar.
            sufix (str): Sufijo del nuevo campo creado después de limpiar.
            keep_original (bool): True si se mantiene el campo original y el
                nuevo se agrega con un sufijo. False para reemplazar el campo
                original.
            inplace (bool): True si los cambios deben impactar en el estado del
                objeto. False si sólo se quiere retornar una serie limpia sin
                impactar en el estado del objeto.

        Returns:
            pandas.Series: Serie de strings limpios
        """
        # debe normalizarse el nombre del campo primero
        field = self._normalize_field(field)

        # toma la serie a limpiar del DataFrame
        series = self.df[field]

        # ________________________________________________________
        # en este espacio se aplica el nuevo algoritmo de limpieza
        # y se guarda la serie limpia en una nueva variable

        clean_series = series
        # ________________________________________________________

        # guarda los cambios en el objeto, si inplace=True
        if inplace:
            self._update_series(field=field, sufix=sufix,
                                keep_original=keep_original,
                                new_series=clean_series)

        return clean_series


def clean_file(input_path, output_path):
    """Limpia los datos del input creando un nuevo archivo limpio."""

    print("Comenzando limpieza...")
    # crea una instancia de la versión extendible del DataCleaner
    dc = MyDataCleaner(input_path)

    # aplica reglas de limpieza disponibles y customizadas
    custom_cleaning_before_rules(dc)
    dc.clean(RULES)
    custom_cleaning_after_rules(dc)

    # guarda la data limpia en el csv output
    dc.save(output_path)
    print("Limpieza finalizada exitosamente!")


if __name__ == '__main__':
    # toma argumentos optativos de la línea de comandos
    if len(sys.argv) == 1:
        # el usuario no pasó argumentos, se usan los default en input y output
        clean_file(DEFAULT_INPUT_PATH, DEFAULT_OUTPUT_PATH)
    elif len(sys.argv) == 2:
        # el usuario pasó input, se usa el default para output
        clean_file(sys.argv[1], DEFAULT_OUTPUT_PATH)
    elif len(sys.argv) == 3:
        # el usuario pasó input y output, no se usan defaults
        clean_file(sys.argv[1], sys.argv[2])
    else:
        # el usuario pasó más de 2 argumentos!
        print("{} no es una cantidad de argumentos aceptada.".format(
            len(sys.argv) - 1
        ))
