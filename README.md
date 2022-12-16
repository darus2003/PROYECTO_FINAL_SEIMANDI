# PROYECTO_FINAL_SEIMANDI

Trabajo Realizado en Visual Studio Code y respaldado en github. 

Se trabaja sobre la apps creada con el nombre "trabajo", creando modelos para llevar registro de los familiares. 

Para su ejecucion trabajar con la carpeta PROYECTO>PROYECTO_FINAL_SEIMANDI.

Detalle de los modelos creados: 

a-Pronvicias: este modelo fue creado con el propocito de ser vinculado con el siguiente modelos (ciudades), el mismo fue integramente importado, utilizando la funcion migrations, debido a que las mismas no van a ser cambiadas. 

b-Ciudad: tiene relacion con los modelos de provincia, donde obtiene el id de la misma, y vinculo con el alta de familia. Posee un formulario propio para ingresar previamente al alta de familia.  

c-Familia: Tiene relacion con el modelo ciudad, vinculada con su id. Tiene su propio formulario, para altas. Se crea para agilizar la carga un choices.py con los sexos. 


ingresando en python manage.py runserver ---> http://127.0.0.1:8000/, tenemos las siguientes urls creadas:

1.admin/ ----> sin definir.
2.saludar/ -----> se crearon diferentes link para poder acceder a las sguientes urls.
3.mi-familia/----> Lista todo los familiares en la base de datos: En desarrollo, solo muestra Nombre, Apellido paterno y Apelllido Materno. 
3.mi-familia/buscar ---> realiza un filtro por nombre de famliar. 
4.mi-familia/alta---> acceso al formulario que permite incorporar nuevos familiares a la base de datos 
5.alta-ciudad/---> acceso al formulario que permite incorporar nuevas ciudades a la base de datos. 










