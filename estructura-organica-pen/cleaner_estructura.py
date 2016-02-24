from data_cleaner import DataCleaner

input_path = "./estructuraPrueba.csv"
output_path = "./clean_estructuraPrueba.csv"

rules = [
    {
        "renombrar_columnas":
            [
                {"field": "aut_cargo", "new_field": "autoridad_cargo"},
                {"field": "aut_tratamiento", "new_field": "autoridad_tratamiento"},
                {"field": "aut_apellido", "new_field": "autoridad_apellido"},
                {"field": "aut_nombre", "new_field": "autoridad_nombre"},
                {"field": "aut_norma_designacion", "new_field": "autoridad_norma_designacion"},
            ]
    },
    {
        "nombre_propio": [
                      {"field": "jurisdiccion"},
                      {"field": "unidad"},
                      {"field": "reporta_a"},
                      {"field": "autoridad_cargo"},
                      {"field": "autoridad_tratamiento"},
                      {"field": "autoridad_apellido"},
                      {"field": "autoridad_nombre"},
                      {"field": "domicilio"},
                      {"field": "localidad"},
                      {"field": "provincia"},
                      ]
    },
    {
        "string": [{"field": "jurisdiccion"},
                   {"field": "unidad"},
                   {"field": "reporta_a"},
                   {"field": "unidad_tipo"},
                   {"field": "autoridad_cargo"},
                   {"field": "autoridad_tratamiento"},
                   {"field": "autoridad_apellido"},
                   {"field": "autoridad_nombre"},
                   {"field": "domicilio"},
                   {"field": "localidad"},
                   {"field": "provincia"},
                   ]
    },
    {
        "string_regex_substitute":
            [
                {"field": "norma_competenciasobjetivos", "regex_str_match": ";", "regex_str_sub": ","},
                {"field": "unidad", "regex_str_match": "\(.*\)", "regex_str_sub": ""},
                {"field": "provincia", "regex_str_match": "Bs\. As\.", "regex_str_sub": "Buenos Aires"},
                {"field": "autoridad_tratamiento", "regex_str_match": "\s+$", "regex_str_sub": ""},
                {"field": "autoridad_tratamiento", "regex_str_match": "(.+{^\.})$", "regex_str_sub": "\g<1>."},
                {"field": "autoridad_norma_designacion", "regex_str_match": "Dto\D*", "regex_str_sub": "Decreto "},
                {"field": "web", "regex_str_match": "^.+www\.", "regex_str_sub": "http://www."},
            ]
    },
]


dc = DataCleaner(input_path)
# separar mails: 
dc.df['mail'] = dc.df['mail'].str.lower()
dc.df['mail'] = dc.df.mail.str.findall('[a-z_0-9\.]+@[a-z_0-9\.]+').str.join(",")
dc.clean(rules)
