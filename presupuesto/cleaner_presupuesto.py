#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import int8, int16, int32, int64, uint16, uint32, uint64, float16, float32, float64

import data_cleaner


input_path = "./Gastos_Listado_General-2.csv"
output_path = "./clean_Gastos_Listado_General-2.csv"

rules = [
    {
        "renombrar_columnas":
            [
                {'field': u'\uefbb\xbfCarácter', 'new_field': u'caracter', "inplace":True},
                {'field': u'Cod. Jurisdicción', 'new_field': u'cod_jurisdiccion', "inplace":True},
                {'field': u'Desc. Jurisdicción', 'new_field': u'desc_jurisdiccion', "inplace":True},
                {'field': u'Cod. Subjurisdicción', 'new_field': u'cod_subjurisdiccion', "inplace":True},
                {'field': u'Desc. Subjurisdicción',
                'new_field': u'desc_subjurisdiccion', "inplace":True},
                {'field': u'Cod. Entidad', 'new_field': u'cod_entidad', "inplace":True},
                {'field': u'Desc. Entidad', 'new_field': u'desc_entidad', "inplace":True},
                {'field': u'Cod. Servicio', 'new_field': u'cod_servicio', "inplace":True},
                {'field': u'Desc. Servicio', 'new_field': u'desc_servicio', "inplace":True},
                {'field': u'Cod. Programa', 'new_field': u'cod_programa', "inplace":True},
                {'field': u'Desc. Programa', 'new_field': u'desc_programa', "inplace":True},
                {'field': u'Cod. Finalidad', 'new_field': u'cod_finalidad', "inplace":True},
                {'field': u'Desc. Finalidad', 'new_field': u'desc_finalidad', "inplace":True},
                {'field': u'Cod. Función', 'new_field': u'cod_funcion', "inplace":True},
                {'field': u'Desc. Función', 'new_field': u'desc_funcion', "inplace":True},
                {'field': u'Cod. Inciso', 'new_field': u'cod_inciso', "inplace":True},
                {'field': u'Desc. Inciso', 'new_field': u'desc_inciso', "inplace":True},
                {'field': u'Cod. Principal', 'new_field': u'cod_principal', "inplace":True},
                {'field': u'Desc. Principal', 'new_field': u'desc_principal', "inplace":True},
                {'field': u'Cod. Clasificador Económico 2 D\xc3\xadgitos',
                'new_field': u'cod_clasificador_economico_2_digitos', "inplace":True},
                {'field': u'Desc. Clasificador Económico 2 D\xc3\xadgitos',
                'new_field': u'desc_clasificador_economico_2_digitos', "inplace":True},
                {'field': u'Cod. Clasificador Económico 3 D\xc3\xadgitos',
                'new_field': u'cod_clasificador_economico_3_digitos', "inplace":True},
                {'field': u'Desc. Clasificador Económico 3 D\xc3\xadgitos',
                'new_field': u'desc_clasificador_economico_3_digitos', "inplace":True},
                {'field': u'Cod. Fuente Financiamiento',
                'new_field': u'cod_fuente_financiamiento', "inplace":True},
                {'field': u'Desc. Fuente Financiamiento',
                'new_field': u'desc_fuente_financiamiento', "inplace":True},
                {'field': u'Presupuestado', 'new_field': u'monto_presupuestado', "inplace":True},
                {'field': u'Comprometido', 'new_field': u'monto_comprometido', "inplace":True},
                {'field': u'Devengado', 'new_field': u'monto_devengado', "inplace":True},
                {'field': u'Pagado', 'new_field': u'monto_pagado', "inplace":True},
                {'field': u'Leyenda_Fecha_Act', 'new_field': u'leyenda_fecha_act', "inplace":True},
                {'field': u'Ejercicio-Actual', 'new_field': u'ejercicio_actual', "inplace":True},
            ]
    },
    {
        "string_replace":
            [
                {"field": u"monto_presupuestado", "old": ",", "new": ".", "inplace":True, "keep_original":False},
                {"field": u"monto_comprometido", "old": ",", "new": ".", "inplace":True, "keep_original":False},
                {"field": u"monto_devengado", "old": ",", "new": ".", "inplace":True, "keep_original":False},
                {"field": u"monto_pagado", "old": ",", "new": ".", "inplace":True, "keep_original":False},
            ]
    },
    {
        "change_type":
            [
                {"field": u"monto_presupuestado", "new_type": "float64", "inplace":True, "keep_original":False},
                {"field": u"monto_comprometido", "new_type": "float64", "inplace":True, "keep_original":False},
                {"field": u"monto_devengado", "new_type": "float64", "inplace":True, "keep_original":False},
                {"field": u"monto_pagado", "new_type": "float64", "inplace":True, "keep_original":False},
                
                {'field': u'caracter', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_jurisdiccion', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_jurisdiccion', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_subjurisdiccion', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_subjurisdiccion', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_entidad', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_entidad', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_servicio', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_servicio', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_programa', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_programa', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_finalidad', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_finalidad', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_funcion', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_funcion', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_inciso', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_inciso', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_principal', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_principal', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_clasificador_economico_2_digitos', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_clasificador_economico_2_digitos', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_clasificador_economico_3_digitos', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_clasificador_economico_3_digitos', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'cod_fuente_financiamiento', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'desc_fuente_financiamiento', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'leyenda_fecha_act', 'new_type': 'unicode', "inplace":True, "keep_original":False},
                {'field': u'ejercicio_actual', 'new_type': 'unicode', "inplace":True, "keep_original":False},
            ]
    },
]


class MyDataCleaner(data_cleaner.DataCleaner):
    def string_replace(self, field, old,
                                new, sufix="clean",
                                keep_original=True, inplace=False):
        """Regla para reeplazar substrings.
        Args:
            field (str): Campo a limpiar
            old (str): String  a buscar
            new (str): String para el reemplazo
        Returns:
            pandas.Series: Serie de strings alterados
        """
        
        field = self._normalize_field(field)
        series = self.df[field]
        replaced = series.str.replace(old, new)
        encoded_series = replaced.str.encode(self.OUTPUT_ENCODING)

        if inplace:
            self._update_series(field=field, sufix=sufix,
                                keep_original=keep_original,
                                new_series=encoded_series)

        return encoded_series


    def change_type(self, field, new_type, sufix="clean",
                                keep_original=True, inplace=False):
        """Regla para cambiar el tipo del campo.
        Args:
            field (str): Campo a limpiar
            new_type (str): Nuevo tipo de dato
        Returns:
            pandas.Series: Serie con el campo alterado
        """
        
        new_type = {
            "int" : int,
            "float" : float,
            "str" : str,
            "unicode" : unicode,
            "int8" : int8,
            "int16" : int16,
            "int32" : int32,
            "int64" : int64,
            "uint16" : uint16,
            "uint32" : uint32,
            "uint64" : uint64,
            "float16" : float16,
            "float32" : float32,
            "float64" : float64
        }[new_type]
        field = self._normalize_field(field)
        series = self.df[field]
        replaced = series.astype(new_type)
        encoded_series = replaced

        if inplace:
            self._update_series(field=field, sufix=sufix,
                                keep_original=keep_original,
                                new_series=encoded_series)

        return encoded_series

dc = MyDataCleaner(input_path)
dc.clean(rules)

import csv
import pandas as pd
data_cleaner.data_cleaner.pd.set_option('display.float_format', lambda x: '%.3f' % x)
dc.save(output_path, quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8', index=False)

