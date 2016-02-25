# -*- coding: utf-8 -*-

from data_cleaner import DataCleaner

data_path = '/home/mec/Downloads/'
input_path = data_path + "arg-servsociales-mds-red144-nacional.csv"
output_path = data_path +  "clean_red-114-del-consejo-nacional-de-las-mujeres.csv"

rules = [
    {
        "nombre_propio": [
            {"field": "institucion"},
            {"field": "localidad"},
            {"field": "provincia"},
            {"field": "direccion"},
        ]
    },
    {
        "string": [
            {"field": "localidad"},
            {"field": "provincia"},
            {"field": "direccion"},
            {"field": u"Tipo de API (Centro/Institución)"},
        ]
    },
    {"renombrar_columnas": [
        {"field": "recurso", "new_field": "coordenadas"},
    ]}
    # NO FUNCIONA BIEN DEJO EL CAMPO COMO ESTA
#     {"reemplazar": [
#     {
#      "field": "horario_de_atencion",
#      "replacements": {"LUN": ["lunes", "lun"], 
#                       "MAR": ["martes", "mar"],
#                       "MIE": ["miercoles", "mie", u"miércoles"],
#                       "JUE": ["jueves", "jue"],
#                       "VIE": ["viernes", "vie"],
#                       "SAB": ["sabado", "sab", "sábado","sáb"],
#                       "DOM": ["domingo", "dom"],
#                       "-": [" a "],
#                       "_": [" y ", ","],
#                       "": ["hs", "hs."],
#                       "00:00-23:59": ["24"]
#                      },
#      "keep_original": True
#     }
#    ]}

]

dc = DataCleaner(input_path)
# No implementados aun van derecho con Pandas
dc.df['coordenadas_latitud'] = dc.df.recurso.str.split("\s+", 1, expand=True)[0]
dc.df['coordenadas_longitud'] = dc.df.recurso.str.split("\s+", 1, expand=True)[1]
dc.df['mail'] = dc.df['mail'].str.lower()
dc.df['sitio_web'] = dc.df.mail.str.findall('www[^ \s]+').str.join(",")
dc.df['mail'] = dc.df.mail.str.findall('[a-z_0-9\.]+@[a-z_0-9\.]+').str.join(",")
dc.clean_file(rules, output_path)
