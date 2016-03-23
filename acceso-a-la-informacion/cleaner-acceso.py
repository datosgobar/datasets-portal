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
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import sys
import pandas as pd
from data_cleaner import DataCleaner

DEFAULT_INPUT_PATH = "acceso-informacion-publica-raw.csv"
DEFAULT_OUTPUT_PATH = "acceso-informacion-publica-clean.csv"


RULES = [
    {
        "string_regex_substitute": [
            {"field": "forma_del_pedido",
             "regex_str_match": "nota",
             "regex_str_sub": "Nota",
             "keep_original": False
             },
            {"field": "sector_al_que_se_dirige_la_solicitud",
             "regex_str_match": "^\.+",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": "^\.+",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": u"\u2026",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": u"Complete aquí",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": "NO COMPLETAR",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "plazo_en_el_que_se_contesto_la_solicitud",
             "regex_str_match": u"Complete aquí",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "plazo_en_el_que_se_contesto_la_solicitud",
             "regex_str_match": "NO COMPLETAR",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "forma_de_aviso_de_uso_de_la_prorroga_al_solicitante",
             "regex_str_match": u"Complete aquí",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "forma_de_aviso_de_uso_de_la_prorroga_al_solicitante",
             "regex_str_match": "NO COMPLETAR",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "cargo_del_funcionario_que_firma_la_entrega_de_la_informacion",
             "regex_str_match": "^\.+",
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "cargo_del_funcionario_que_firma_la_entrega_de_la_informacion",
             "regex_str_match": u"\u2026", # sacar caracter de puntos suspensivos
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "cargo_del_funcionario_que_firma_la_entrega_de_la_informacion",
             "regex_str_match": u"Complete aquí", # sacar caracter de puntos suspensivos
             "regex_str_sub": "",
             "keep_original": False
             },
            {"field": "cargo_del_funcionario_que_firma_la_entrega_de_la_informacion",
             "regex_str_match": u"NO COMPLETAR", # sacar caracter de puntos suspensivos
             "regex_str_sub": "",
             "keep_original": False
             },
             {"field": "fecha_de_la_respuesta",
              "regex_str_match": u"Complete aquí",
              "regex_str_sub": "",
              "keep_original": False
              },
             {"field": "fecha_de_la_respuesta",
              "regex_str_match": "NO COMPLETAR",
              "regex_str_sub": "",
              "keep_original": False
              },
              {"field": "fecha_de_la_respuesta",
              "regex_str_match": u"2010",
              "regex_str_sub": "2015",
              "keep_original": False
              },
             {"field": "fecha_de_la_respuesta",
              "regex_str_match": "2017",
              "regex_str_sub": "2015",
              "keep_original": False
              },
        ]
    },
    {"nombre_propio": [
        {"field": "sector_al_que_se_dirige_la_solicitud", "keep_original": False},
        {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo", "keep_original": False},
    ]},

    {"fecha_completa": [
        {"field": "fecha_de_recepcion_de_la_solicitud_por_el_organismo", "time_format": "M/D/YYYY", "keep_original": True},
        {"field": "fecha_de_recepcion_de_la_solicitud_por_el_enlace", "time_format": "M/D/YYYY","keep_original": True},
        {"field": "fecha_de_la_respuesta", "time_format": "DD/MM/YYYY","keep_original": True}
     ]},
      {
        "string_regex_substitute": [
            {"field": "sector_al_que_se_dirige_la_solicitud",
             "regex_str_match": "Dniece",
             "regex_str_sub": "DNIECE",
             "keep_original": False
             },
             {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": "Enre",
             "regex_str_sub": "ENRE",
             "keep_original": False
             },
             {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": "Telam",
             "regex_str_sub": "TELAM",
             "keep_original": False
             },
             {"field": "sector_al_que_derivo_el_enlace_dentro_del_organismo",
             "regex_str_match": "Renaper",
             "regex_str_sub": "ReNaPer",
             "keep_original": False
             },
        ]
    },

]

def custom_cleaning_before_rules(dc):
    """Script de limpieza custom para aplicar al objeto antes de las reglas.

    Args:
        dc (DataCleaner): Objeto data cleaner con datos cargados.
    """
    dc.df['pedidos'] = dc.df['pedidos'].fillna(method='ffill') #  Completar los pedidos en blanco con el ultimo valido
    dc.df['pedidos']= dc.df['pedidos'].astype('int32')
    dc.df['casos']= dc.df['casos'].astype('int32')
    dc.df['perfil_del_solicitante'] = dc.df['perfil_del_solicitante'].fillna("")
    dc.df['sector_al_que_se_dirige_la_solicitud'] = dc.df['sector_al_que_se_dirige_la_solicitud'].fillna("")
    dc.df['rubro_de_solicitud_de_informacion'] = dc.df['rubro_de_solicitud_de_informacion'].fillna("")
    dc.df['sector_al_que_derivo_el_enlace_dentro_del_organismo'] = dc.df['sector_al_que_derivo_el_enlace_dentro_del_organismo'].fillna("")
    dc.df['cargo_del_funcionario_que_firma_la_entrega_de_la_informacion'] = dc.df['cargo_del_funcionario_que_firma_la_entrega_de_la_informacion'].fillna("")
    dc.df['plazo_en_el_que_se_contesto_la_solicitud'] = dc.df['plazo_en_el_que_se_contesto_la_solicitud'].fillna("")
    dc.df['forma_de_aviso_de_uso_de_la_prorroga_al_solicitante'] = dc.df['forma_de_aviso_de_uso_de_la_prorroga_al_solicitante'].fillna("")



def custom_cleaning_after_rules(dc):
    """Script de limpieza custom para aplicar al objeto después de las reglas.

    Args:
        dc (DataCleaner): Objeto data cleaner con datos cargados.
    """
    #  Saco datos que no peretencen al rango de fechas
    #gi_resp = pd.to_datetime(dc.df['isodatetime_fecha_de_la_respuesta']).dt.year > 2010
    #gi_solicitud = pd.to_datetime(dc.df['isodatetime_fecha_de_recepcion_de_la_solicitud_por_el_organismo']).dt.year > 2010
    #gi_enlace = pd.to_datetime(dc.df['isodatetime_fecha_de_recepcion_de_la_solicitud_por_el_enlace']).dt.year > 2010
    #ge = pd.to_datetime(dc.df['isodatetime_fecha_de_la_respuesta']).isnull()
    #gu = pd.to_datetime(dc.df['isodatetime_fecha_de_la_respuesta']).dt.year < 2016
    #gi = gi_resp & gi_solicitud & gi_enlace & gu
    #dc.df = dc.df[gi | ge]


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
