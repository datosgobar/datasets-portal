# Solicitudes de Acceso a la Información Pública

En este cuerpo de datos se detallan los pedidos de acceso a la información que se realizan en el marco del Decreto 1172/2003. Entre otras cosas, se detallan la fecha del pedido, el estado del trámite y una síntesis del objeto de la solicitud. 

## Características

* **Fecha de Publicación:** 26/02/2016

* **Recursos:** Pedidos de acceso a la información

* **Tags o Etiquetas:** Solicitudes, Acceso a la Información, Pedidos, Información Pública, Trámites de Acceso a la Información, Estado de Trámites,

* **Organización:** Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia

* **Autor:** Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia.

* **Responsable:** Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia.

* **Grupo:**  Administración Pública y Normativa

* **Frecuencia de Actualización:** Anual

## Recursos

### Pedidos de acceso a la información 2016

* **Nombre:** pedidos-de-acceso-a-la-informacion-2016

* **Descripción:** Detalles de los pedidos de información realizados al estado en el año 2016

* **Formato:** CSV

* **Rango temporal:** 01/01/2016 al 31/12/2016

* **Fecha de Actualización:** 06/04/2017

#### Campos del recurso

* **sips (int):** Nro. de pedido (antes: *pedidos*)

* **casos (int):** Nro. de caso. Puede haber varios casos por pedido.

* **estado (string):** Abierto: la solicitud se encuentra en procesamiento, dentro de los 20 días de plazo / Pendiente: Pasados los 20 días, no se ha respondido el pedido. / Cerrado en plazo: Solicitud respondida dentro del plazo legal. / Cerrado con mora: Solicitud respondida pero pasados los 20 días de plazo.

* **id_general (string):** Sigla-número/año * 

* **organismo (string):** Organismo informante (antes: *organismo_informante*).

* **nro_de_expediente_interno (string):** Nro. de expediente.

* **forma_del_pedido (string):** Nota / Formulario Voluntario de Solicitud de Información

* **punto_de_ingreso (string):** Mesa de entrada por la que ingresó el pedido.

* **isodatetime_fecha_de_recepcion_de_la_solicitud_por_el_organismo (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_recepcion_de_la_solicitud_por_el_organismo (string):** Fecha en que fue recibida la solicitud por parte del organismo comprometido.

* **isodatetime_fecha_de_recepcion_de_la_solicitud_por_el_enlace (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_recepcion_de_la_solicitud_por_el_enlace (string):** Fecha en que fue recibida la solicitud por parte del Enlace.

* **perfil_del_solicitante (string):** Perfil del solicitante. (Ej. ONG, Sindicato, Particular)

* **ciudad (string):** Ciudad en que fue realizada la solicitud

* **provincia (string):** Provincia en que fue realizada la solicitud

* **pais (string):** País en que fue realizada la solicitud

* **sintesis_del_pedido_de_informacion (string):** Resúmen del objeto sobre el cual se realiza el pedido de acceso a información (antes: *sintesis_de_la_solicitud*) . 

* **tipo_de_informacion_solicitada (string):** Rubro sobre el cual se realiza el pedido de acceso a información (antes: *rubro_de_solicitud_de_informacion*). 

* **derivacion_de_la_sip_otro_organismo_ente_descentralizado_empresa (string):** Sector definitivo responsable de responder (antes *sector_al_que_derivo_el_enlace_dentro_del_organismo*)

* **derivacion_de_la_sip_area_dentro_del_organismo (string):** Oficina o área que recibió el Pedido de Información (antes: *sector_al_que_se_dirige_la_solicitud*)

* **isodatetime_fecha_de_la_remision (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_la_remision (string):** Fecha en la que la solicitud es remitida al organismo encargado de responder.

* **prorroga (string):** Medio por el cual se notificó de la prorroga al solicitante. (antes *forma_de_aviso_de_uso_de_la_prorroga_al_solicitante*)

* **isodatetime_fecha_de_la_respuesta (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_la_respuesta (string):** Fecha en que fue respondido el pedido.

* **sintesis_de_la_respuesta (string):** Síntesis de la respuesta brindada.

* **apellido_nombre_y_cargo_de_quien_firma_la_respuesta (string):** Apellido, nombre y cargo del funcionario que firma la entrega de la información.


### Pedidos de acceso a la información 2015

* **Nombre:** pedidos-de-acceso-a-la-informacion-2015

* **Descripción:** Detalles de los pedidos de información realizados al estado en el año 2015

* **Formato:** CSV

* **Rango temporal:** 01/01/2015 al 31/12/2015

* **Fecha de Actualización:** 31/12/2015

#### Campos del recurso

* **pedidos (int):** Nro. de pedido.

* **casos (int):** Nro. de caso. Puede haber varios casos por pedido.

* **id_general (string):** Sigla-número/año * 

* **estado (string):** Abierto: la solicitud se encuentra en procesamiento, dentro de los 20 días de plazo / Pendiente: Pasados los 20 días, no se ha respondido el pedido. / Cerrado en plazo: Solicitud respondida dentro del plazo legal. / Cerrado con mora: Solicitud respondida pero pasados los 20 días de plazo.

* **organismo_informante (string):** Organismo informante.

* **nro_de_expediente_interno (string):** Nro. de expediente.

* **forma_del_pedido (string):** Nota / Formulario Voluntario de Solicitud de Información

* **punto_de_ingreso (string):** Mesa de entrada por la que ingresó el pedido.

* **sector_al_que_se_dirige_la_solicitud (string):** Oficina o área que recibió el Pedido de Información

* **isodatetime_fecha_de_recepcion_de_la_solicitud_por_el_organismo (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_recepcion_de_la_solicitud_por_el_organismo (string):** Fecha en que fue recibida la solicitud por parte del organismo comprometido.

* **isodatetime_fecha_de_recepcion_de_la_solicitud_por_el_enlace (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_recepcion_de_la_solicitud_por_el_enlace (string):** Fecha en que fue recibida la solicitud por parte del Enlace.

* **perfil_del_solicitante (string):** Perfil del solicitante. (Ej. ONG, Sindicato, Particular)

* **sintesis_de_la_solicitud (string):** Resúmen del objeto sobre el cual se realiza el pedido de acceso a información. 

* **rubro_de_solicitud_de_informacion (string):** Rubro sobre el cual se realiza el pedido de acceso a información. 

* **sector_al_que_derivo_el_enlace_dentro_del_organismo (string):** Sector definitivo responsable de responder.

* **plazo_en_el_que_se_contesto_la_solicitud (string):** Plazo en el que fue contestada la solicitud. 

* **forma_de_aviso_de_uso_de_la_prorroga_al_solicitante (string):** Medio por el cual se notificó de la prorroga al solicitante.

* **condicion_de_respuesta (string):** Tipo de respuesta recibida. (Ej: Brindó la información, No se entregó por inexistencia de información (art 5), Devuelta por no corresponder al organismo, Pendiente, Derivada a otro organismo, etc.)

* **isodatetime_fecha_de_la_respuesta (date):** Mismos datos del campo siguiente con formato estándar. 

* **fecha_de_la_respuesta (string):** Fecha en que fue respondido el pedido.

* **cargo_del_funcionario_que_firma_la_entrega_de_la_informacion (string):** Cargo del funcionario que firma la entrega de la información.


------------------------------------------------------------------------------------------------------------------

*Ejemplo: MS-01/2009

Siglas:

* SGM: Jefatura de Gabinete

* MCTI: Ministerio de Ciencia, Tecnología e Innovación Productiva

* MD: Ministerio de Defensa

* MDS: Ministerio de Desarrollo Social

* MEC: Ministerio de Economía y Finanzas Públicas

* MED: Ministerio de Educación

* JUS: Ministerio de Justicia, Seguridad y DDHH

* MPL: Ministerio de Planificación

* MPR: Ministerio de Producción

* MRE: Ministerio de Relaciones Exteriores y Comercio

* MS: Ministerio de Salud

* MT: Ministerio de Trabajo

* MI: Ministerio del Interior

* CULT: Secretaría de Cultura

* SIDE: Secretaría de Inteligencia

* SGP: Secretaría General de la Presidencia

* SLyT: Secretaría Legal y Técnica

* SED: SEDRONAR

* SIGE: SIGEN

* PAMI: PAMI.

## Notas

El acceso a la Información Pública esta regulado por el decreto 1172/2003:[http://infoleg.gov.ar/infolegInternet/anexos/90000-94999/90763/norma.htm](http://infoleg.gov.ar/infolegInternet/anexos/90000-94999/90763/norma.htm) 

