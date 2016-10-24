# Formulario de Dataset

**Título del DataSet:**  Contratos de Alquiler del Estado Nacional como Locador

**Descripción:** 	Información de los contratos donde el Estado Nacional arrienda, como locador, inmuebles de su propiedad. Esta información se actualizará conforme los contratos sean digitalizados y cargados por la Agencia de Administración de Bienes del Estado.

**Fuente:** Registro de Contratos de la Agencia de Administración de Bienes del Estado

**Autor:** Jefatura de Gabinete de Ministros. Agencia de Administración de Bienes del Estado. Dirección Nacional del Registro de Bienes Inmuebles. 

**E-mail del Autor:** info_renabe@bienesdelestado.gob.ar

**Responsable:** Agencia de Administración de Bienes del Estado. Dirección Nacional del Registro de Bienes Inmuebles.

**E-mail del Responsable:** info_renabe@bienesdelestado.gob.ar

**Grupo: **Administración Pública; Infraestructura y Obra Pública

**Tags o Etiquetas:**  Inmuebles, Alquileres, Contratos, Locador, Bienes Inmuebles

**Frecuencia de Actualización:**  Eventual

## Formulario del Recurso

**Nombre:** Contratos de alquiler ENA

**Descripción:** 	Información de los contratos donde el Estado Nacional arrienda, como locador, inmuebles de su propiedad. Esta información se actualizará conforme los contratos sean digitalizados y cargados por la Agencia de Administración de Bienes del Estado.

**Formato:**  csv

**Campos:** 

* cce (String): Sigla de Código de Contrato del Estado. Es el código de registro del contrato que le asigna la Agencia de Administración de Bienes del Estado al Contrato.

* cie (String): Sigla de Código de Inmueble del Estado. Es el código de registro del contrato que le asigna la Agencia de Administración de Bienes del Estado al Inmueble.

* tipo_contraparte (String): Clasificación entre persona física o jurídica.

* razon_social (String): Denominación de la contraparte del Estado en el contrato.

* objeto(String): Descripción del Objeto del Contrato

* isodatetime_fecha_inicio(Date): Estandarización del campo fecha_inicio

* fecha_inicio(Date): Fecha de Inicio del Contrato

* isodatetime_fecha_finalizacion(Date): Estandarización del campo fecha_finalizacion	

* fecha_finalizacion(Date): Fecha de Finalización del Contrato

* canon_total(Numeric): Monto Total del contrato

* organización(String): Organización que firmó el contrato.

* jurisdiccion(String): Organismo del cual depende la organización.

* provincia(String): Provincia de la ubicación del inmueble

* departamento(String): Departamento de la ubicación del inmueble

* localidad(String): Localidad de la ubicación del inmueble

* direccion(String): Dirección de la ubicación del inmueble 

* destino_uso (String): Descripción del destino de uso que se le dará al inmueble según el contrato.

* contrato_url (string): URL link hacia el archivo pdf del contrato

