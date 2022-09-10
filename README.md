# Proyecto final de Python de Coder House

_El proyecto se pensó como una página donde se puede compartir opiniones de literatura, música y cine.
Para esto los usuarios que deseen subir contenido deberan loguearse. Para ver el contenido no hace falta crearse un
usario.

### Explicacion funcionamiento 📋

La pagina se puede utilizar de 3 maneras:
Como "Admin":
Este usuario puede crear, modificar y eliminar cualquier dato de usuarios, literatura, musica o cine creado.
Al loguearse con este usuario se mostraran opciones que a los otros usuarios no.
Al cliclear sobre su nombre de usuario que se encuentra arriba a la derecha, puede modificar sus datos y agregar un
avatar.

Como "Usuario":
Una persona se puede crear un usuario por medio del "Create user".
Una vez creado el usuario, este puede logearse y comenzar a crear contenido de acuerdo a lo que desee, literatura,
musica o cine.
Tambien puede modificar o eliminar los datos que ha ingresado, ya que con esas opciones solo le apareceran lo que él
haya creado.
Tambien puede ver lo creado por otros usuarios, pero solo como visor, sin poder modificar nada.
Al cliclear sobre su nombre de usuario que se encuentra arriba a la derecha, puede modificar sus datos y agregar un
avatar.

Como "Invitado":
Este tipo de usuarios, solo puede ver lo creado por otros usuarios, pero solo como visor, sin poder modificar nada.

### Pre-requisitos 📋

_Esta version se creó con:

-Python 3.10.6

-Django 4.1

-PyCharm 2022.2 (Community Edition)
Build #PC-222.3345.131, built on July 27, 2022
Runtime version: 17.0.3+7-b469.32 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: G1 Young Generation, G1 Old Generation
Memory: 2034M
Cores: 4

- Importar "import ctypes" en las vistas para mostrar avisos pop ups
- Instalar python -m pip install Pillow
- Se instalo pip install django-richtextfield
- pip install django-ckeditor 

Para mas detalle se puede ver el archivo "requirements.txt"

### Componentes 🔧

Página principal: http://127.0.0.1:8000/TPFinal/

Página para crear un nuevo usuario: http://127.0.0.1:8000/TPFinal/Logon/

Página donde un usuario se loguea:
http://127.0.0.1:8000/TPFinal/Login/

Página para crear un nuevo dato de literatura: http://127.0.0.1:8000/TPFinal/Literatura/Crear/

Pagina para administrar la literatura creada por cada usuario: http://127.0.0.1:8000/TPFinal/Literatura/Buscar/

Pagina para ver toda la literatura cargada por todos los usuarios: http://127.0.0.1:8000/TPFinal/Literatura/BuscarVer/

Pagina paramodificar datos de literatura seleccionada: http://127.0.0.1:8000/TPFinal/Literatura/Modificar/"ID de
literatura"

Pagina que muestra una literatura especifica seleccionada: http://127.0.0.1:8000/TPFinal/Literatura/Ver/"ID de
literatura"

Página para crear un nuevo dato de musica: http://127.0.0.1:8000/TPFinal/Musica/Crear/

Pagina para administrar la musica creada por cada usuario: http://127.0.0.1:8000/TPFinal/Musica/Buscar/

Pagina para ver toda la musica cargada por todos los usuarios: http://127.0.0.1:8000/TPFinal/Musica/BuscarVer/

Pagina paramodificar datos de musica seleccionada: http://127.0.0.1:8000/TPFinal/Musica/Modificar/"ID de musica"

Pagina que muestra una musica especifica seleccionada: http://127.0.0.1:8000/TPFinal/Musica/Ver/"ID de musica"

Página para crear un nuevo dato de cine: http://127.0.0.1:8000/TPFinal/Cine/Crear/

Pagina para administrar las peliculas creadas por cada usuario: http://127.0.0.1:8000/TPFinal/Cine/Buscar/

Pagina para ver toda las peliculas cargadas por todos los usuarios: http://127.0.0.1:8000/TPFinal/Cine/BuscarVer/

Pagina paramodificar datos de pelicula seleccionada: http://127.0.0.1:8000/TPFinal/Cine/Modificar/"ID de pelicula"

Pagina que muestra una pelicula especifica seleccionada: http://127.0.0.1:8000/TPFinal/Cine/Ver/"ID de pelicula"

Solo puede acceder el usuario admin
Pagina para crear usuarios: http://127.0.0.1:8000/TPFinal/Usuario/Crear/

Pagina para listar todos los uaurios existentes: http://127.0.0.1:8000/TPFinal/Usuario/Buscar/

Pagina para modificar datos de los usuarios: http://127.0.0.1:8000/TPFinal/Usuario/Modificar/"nombre de usuario"

## Ejecutando las pruebas ⚙️

Las pruebas realizadas fueron:

- Se creó un usuario desde el formulario que solicita los datos.
- Se creó un dato de literatura desde el formulario que solicita los datos.
- Se creó un dato de musica desde el formulario que solicita los datos.
- Se creó un dato de cine desde el formulario que solicita los datos.
- Se buscaron datos de literaturas ya cargadas desde el formulario que solicita los datos,
  donde realiza la búsqueda con al menos un dato ingresado coincidente.
- Se buscaron datos de musica ya cargadas desde el formulario que solicita los datos,
  donde realiza la búsqueda con al menos un dato ingresado coincidente.
- Se buscaron datos de cine ya cargadas desde el formulario que solicita los datos,
  donde realiza la búsqueda con al menos un dato ingresado coincidente.

Todos los datos cargados se pueden validar ingresando a http://127.0.0.1:8000/admin/

## Construido con 🛠️

* [Python](https://www.python.org/)
* [Pycharm](https://www.jetbrains.com/pycharm/promo/?source=google&medium=cpc&campaign=14127625370&term=pycharm)
* [Django](https://www.djangoproject.com/)

## Wiki 📖

N/A

## Versionado 📌

Primera version

## Autores ✒️

* **Fernando Otero** - *Trabajo Inicial* - [Fernando Otero](https://github.com/fotero80)

## Licencia 📄

Este proyecto no está bajo Licencia.

## Expresiones de Gratitud 🎁

* Gracias a los profesores y tutores de Coder House

---
⌨️Por [Fernando Otero](https://github.com/fotero80) 😊

