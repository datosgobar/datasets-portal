#GENERAL

Los CSVs raw no tienen delimitados los campos por “ ” y algunos campos contienen comas en sus valores entonces no se parsea correctamente. ARREGLARLO!

##CAMPOS

* Normalizar los campos al formato de nuestro estandar>  minusculas_y_guiones_bajos
* Separar la columna mail en mail / sitio_web 
* Separar el campo RECURSO que contiene coordenadas en latitud y longitud

##VALORES
* mail:  
1. hay varios mails, separarlos con ‘,’ 
1. pasar los mails a minusculas
1. Extraer los sitios web que haya y mandarlos a la columna nueva sito_web
* horario_de_atencion llevarlo al standard en un nuevo campo standard_horario_de_atencion pero conservando version legible por humanos 
