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

DEFAULT_INPUT_PATH = "contratos-raw.csv"
DEFAULT_OUTPUT_PATH_VIGENTE = "contratos-2015-clean.csv"
DEFAULT_OUTPUT_PATH1_HISTORICO = "contratos-historico-clean.csv"

RULES = [

    {
        "nombre_propio": [
            {"field": "financiacion"},
            {"field": "nombre_organismo"},
            {"field": "apellido"},
            {"field": "nombre"},
        ]
    },
    {
        "fecha_simple": [
            {"field": "alta_fecha", "time_format": "YYYY/MM/DD"},
            {"field": "mod_fecha", "time_format": "YYYY/MM/DD"},
        ]
    },

    {
        "reemplazar": [
            {"field": "locacion",
             "replacements": {"Servicios": ["Serv"],

                              }
             }
        ]
    },
    {
        "reemplazar": [
            {"field": "financiacion",
             "replacements": {"Dec. 1421/2002 - Convenio Dec.1133/09": ["Dec. 1133/2009"],
                              "Dec. 1421/2002 - Convenio Conae": ["Convenio Conae"],
                              "Dec. 1421/2002 - Convenio Docifa": ["Convenio Docifa"],
                              "Dec. 1421/2002 - Convenio Pecifa": ["Convenio Pecifa"],
                              "Dec. 1421/2002 - Convenio Senasa": ["Convenio Senasa"],
                              "Dec. 1421/2002 - Convenio Sigen": ["Convenio Sigen"],
                              "Dec. 2345/2008 - Fin. Int. B I D": ["Fin. Int. B I D"],
                              "Dec. 2345/2008 - Fin. Int. B I R F": ["Fin. Int. B I R F"],
                              "Dec. 2345/2008 - Fin. Int. B M": ["Fin. Int. B M"],
                              "Dec. 2345/2008 - Fin. Int. Fonplata": ["Fin. Int. Fonplata"],
                              "Dec. 2345/2008 - Fin. Int. P N U D": ["Fin. Int. P N U D"],
                              "Dec. 2345/2008 - Fin. Int. U E": ["Fin. Int. U E"],
                              "Dec. 1421/2002 (arts. 93/99 LCT)": [u"Ley Nº 20744"],
                              }
             }
        ]
    },

    {"renombrar_columnas": [
        {"field": "alta_fecha", "new_field": "fecha_alta_registro_rcpc"},
        {"field": "mod_fecha", "new_field": "fecha_modificacion_registro_rcpc"},
        {"field": "id_unico", "new_field": "id_organismo"},
    ]},

    {"remover_columnas": [
        {"field": "estudios"},
        {"field": "titulo"},
        {"field": "nivel_grado"},
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
    dc = DataCleaner(input_path, encoding='latin1')
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
    df1 = dc.df[givig].copy()
    print("La cantida de registros 2015 es: ")
    print(givig.sum())
    gin2016 = dc.df.desde.dt.year == 2016
    df2 = dc.df[~gin2016].copy()
    print("La cantida de registros historicos es: ")
    print((~gin2016).sum())
    df1.to_csv(
        DEFAULT_OUTPUT_PATH_VIGENTE, encoding=dc.OUTPUT_ENCODING,
        separator=dc.OUTPUT_SEPARATOR,
        quotechar=dc.OUTPUT_QUOTECHAR, index=False)
    df2.to_csv(
        DEFAULT_OUTPUT_PATH1_HISTORICO, encoding=dc.OUTPUT_ENCODING,
        separator=dc.OUTPUT_SEPARATOR,
        quotechar=dc.OUTPUT_QUOTECHAR, index=False)

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
