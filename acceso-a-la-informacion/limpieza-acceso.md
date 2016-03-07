#GENERAL:

Quitar la primera fila, Borrar últimas dos columnas que tienen solo un texto aclaratorio para una única fila.

Poner la columna de fecha de la respuesta en formato de celda fecha DD/MM/YYYY antes de guardar como csv

##CAMPOS:

Llevar los nombres a formato estándar.

##VALORES:

**forma_del_pedido:** reemplazar ‘nota’ por ‘Nota’

**fecha_de_recepcion_de_la_solicitud_por_el_organismo:**  llevar a iso date

 **sector_al_que_se_dirige_la_solicitud:** Quitar puntos iniciales y Capitalizar

**fecha_de_recepcion_de_la_solicitud_por_el_enlace:**  llevar a iso date

**sector_al_que_derivo_el_enlace_dentro_del_organismo:** Quitar puntos iniciales y Capitalizar

**plazo_en_el_que_se_contesto_la_solicitud:** Quitar valores *[ 'Complete aqu\xed', 'NO COMPLETAR' ]*

**forma_de_aviso_de_uso_de_la_prorroga_al_solicitante:** Quitar valores [ 'Complete aqu\xed', 'NO COMPLETAR' ]

**fecha_de_la_respuesta:** llevar a iso date
Aca hay un problema grave con las fechas algunas tienen mes primer otras dia primero y otra estan en algun formato int  NO ESTÁ CLARO COMO SABER CUAL ES CUAL SIEMPRE
RESUELTO: hay que 
Poner la columna de fecha de la respuesta en formato de celda fecha DD/MM/YYYY antes de guardar como csv

**cargo_del_funcionario_que_firma_la_entrega_de_la_informacion:** Quitar puntos iniciales

