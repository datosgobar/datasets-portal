# Registro Único de Audiencias de Gestión de Intereses

Información correspondiente a las solicitudes de audiencias a funcionarios públicos. La misma surge del [Registro Único de Audiencias de Gestión de Intereses del Poder Ejecutivo Nacional](http://audiencias.jgm.gob.ar/registrodeaudiencias/searchjgm.php), establecido por el Decreto 1172/2003. Contiene, entre otros, datos sobre las fechas de solicitud y realización de la audiencia, sus participantes y una síntesis de los temas discutidos. Para una descripción más detallada de los datos disponibles ver la sección [Recursos](#heading=h.kh8t24rymv7n).

# Características

* **Recursos:**  audiencias.csv

* **Tags o Etiquetas:**  Audiencias, Reuniones, Funcionarios, Solicitudes de Audiencia, Agenda Pública

* **Organización:**  MINISTERIO DEL INTERIOR, OBRAS PÚBLICAS Y VIVIENDA. Secretaría de Asuntos Políticos y Fortalecimiento Institucional.

* **Autor:**  Ministerio del Interior, Obras Públicas y Vivienda. Secretaría de Asuntos Políticos y Fortalecimiento Institucional. Subsecretaría de Reforma Institucional y Fortalecimiento de la Democracia.

* **Responsable:**  MINISTERIO DEL INTERIOR, OBRAS PÚBLICAS Y VIVIENDA. Secretaría de Asuntos Políticos y Fortalecimiento Institucional.

* **Grupo:**  Administración Pública y Normativa

* **Frecuencia de Actualización:**  Eventual

# Recursos

## Audiencias

* **Nombre:**  audiencias.csv

* **Descripción:**  Datos sobre las fechas de solicitud y realización de la audiencia con Funcionarios Públicos, sus participantes y una síntesis de los temas discutidos.

* **Formato:**  CSV

* **Rango temporal:**  20-01-2004 / 31-12-2015

* **Fecha de Actualización:**  17/02/2016

### Campos del recurso

* **audiencia_id (int):** ID de la audiencia

* **obligado_cargo (string):** Cargo del sujeto obligado.

* **obligado_apellido (string):** Apellido del sujeto obligado.

* **obligado_nombre (string):** Nombre del sujeto obligado.

* **dependencia_descripcion (string):** Nombre de la Dependencia Estatal en la que se solicitó una Audiencia.

* **root_dependencia_descripcion (string):** 

* **fecha_solicitud (date):** Fecha en que fue solicitada la audiencia.

* **solic_apellido (string):** Apellido de la persona que solicita la audiencia.

* **solic_nombre (string):** Nombre de la persona que solicita la audiencia.

* **solic_cargo (string):** Cargo de la persona que solicita la audiencia.

* **interes_invocado (string):** Puede ser Propio, Colectivo o Difuso invocado por un Particular Interesado, un Organismo Estatal, un Representante de Persona Física o un Representante de Persona Jurídica.

* **desc_caracter (string):** Caracter de la reunión. 

* **representado_cargo (string):** Cargo del Representado

* **representado_persona_juridica (boolean):**  ¿Es persona jurídica el representado?

* **representado_nombre (string):** Nombre del Representado

* **representado_apellido (string):** Apellido del Representado

* **fecha_audiencia (datetime):** Fecha y hora en que se realizó la audiencia.

* **lugar (string): ** Lugar de la Audiencia.

* **objeto (string):** Finalidad de la Audiencia.

* **participante (string):** Nombre de los participantes de la audiencia.

* **comentario (string):** Comentarios sobre la audiencia. 

* **desc_estado (string):** Estado de la audiencia (ej. realizada, pospuesta, suspendida)

* **desc_estado_no_realizado (string):**  Razón por la cual no fue realizada.

* **sintesis (string):** Resúmen de los temas tratados.

* **obligado_asesor_cargo (string):** Cargo del asesor del sujeto obligado.

* **asesor_apellido (string):** Cargo del asesor del sujeto obligado.

* **asesor_nombre (string):** Cargo del asesor del sujeto obligado. 

* **asesor_cargo (string):** Cargo del asesor del sujeto obligado.

# Notas

El decreto que regula el acceso a la información de Audiencias de Funcionarios Públicos se puede encontrar en [este sitio](http://infoleg.gov.ar/infolegInternet/anexos/90000-94999/90763/norma.htm). 

# Preprocesamiento

Este dataset fue preprocesado siguiendo los [estándares de limpieza de datos](https://github.com/gobabiertoAR/documentacion-estandares/tree/master/datos/limpieza) que incluyen una normalización básica de strings, de fechas y separación de campos a partir de strings concatenados.

