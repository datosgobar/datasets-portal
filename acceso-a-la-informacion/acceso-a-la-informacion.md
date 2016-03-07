# Solicitudes de Acceso a la Información Pública

En este cuerpo de datos se detallan los pedidos de acceso a la información que se realizan en el marco del Decreto 1172/2003. Entre otras cosas, se detallan la fecha del pedido, el estado del trámite y una síntesis del objeto de la solicitud. 

# Características

* **Fecha de Publicación:** 26/02/2016

* **Recursos:** Pedidos de acceso a la información

* **Tags o Etiquetas:** Solicitudes, Acceso a la Información, Pedidos, Información Pública, Trámites de Acceso a la Información, Estado de Trámites,

* **Organización:** Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia

* **Autor:** Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia.

* **Responsable:** Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia.

* **Grupo:**  Administración Pública y Normativa

* **Frecuencia de Actualización:** Anual

## Recursos

### Pedidos de acceso a la información

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

* **razon_social_del_solicitante (string):** Razón social del solicitante si la tuviera.

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

# Notas

El acceso a la Información Pública esta regulado por el [decreto 1172/2003]: (http://infoleg.gov.ar/infolegInternet/anexos/90000-94999/90763/norma.htm) 

# Preprocesamiento

Este dataset fue preprocesado siguiendo los[ estándares de limpieza de datos](https://github.com/gobabiertoAR/documentacion-estandares/tree/master/datos/limpieza) que incluyen una normalización básica de strings, de fechas y separación de campos a partir de strings concatenados.

