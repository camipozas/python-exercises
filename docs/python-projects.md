# Proyectos en Python

## 1. Activar entornos virtuales
### ¿Qué son los entornos virtuales?
Los ambientes conocidos como `venv` son una herramienta usada para crear un entorno Python aislado. Este entorno tiene sus propios directorios de instalación que no comparten bibliotecas con otros entornos virtualenv o las bibliotecas instaladas globalmente en el servidor.

> Cabe destacar que `venv` es un paquete que viene con Python 3. Python 2 no contiene venv.
> También existe [Virtualenv](https://virtualenv.pypa.io/en/stable/) es una biblioteca que ofrece más funcionalidades que venv. 
### ¿Cómo activarlos?
1. Correr:
  ```bash
  python3 -m venv [Virtual Environment Name]
  ```
2. En caso de Linux o Windows
 ```bash
source [Virtual Environment Name]/bin/activate
```
3. En caso de Windows:
 ```bash
.\[Virtual Environment Folder Name]\Scripts\activate
 ```

### ¿Cómo desactivarlos?
```bash
deactivate
```

### Eliminar ambiente virtual
```bash
rm -rf [Virtual Environment Folder Name]
```

## 2. Usar requirements
Requirements vendría siendo el uso de librerías o bibliotecas que necesita el programa para funcionar. Por tanto, una vez activado el entorno virtual allí podemos todo lo que necesitamos.

1. Para instalar las librerías necesarias
```bash
pip install [librería]
```

2. Una vez instaladas las librerías necesarias debemos correr el siguiente comando, lo que hará es _congelar_ lo que se instaló con su respectiva versión en un archivo.
 ```bash
 pip freeze > requirements.txt
 ```
 3. En el caso de que estés abriendo un repositorio de otra persona o equipo y haya que instalar las librerías. Primero debes activar el entorno virtual y posteriormente correr:
```bash
pip install -r requirements.txt
```
4. En caso de haber realizado el paso 2 y querer instalar más librerías. Repetir el paso 1 y posteriormente 2. 

## 3. Docker
Algunas veces por temas de compatibilidad o proyectos complicados con herramientas nativas. Es mejor trabajarlo con imágenes de Docker dado que no hay que preocuparse del entorno en el que se va a ejecturar el programa.

### ¿Cómo realizar un Dockerfile?
Este archivo está compuesto por una serie de comandos que te indicaré a continuación, y que son los responsables de la construcción de la imagen.

1. `ADD` copia un archivo del host al contenedor.
2. `CMD` el agumento que pasas por defecto.
3. `ENTRYPOINT` el comando que se ejecuta por defecto al arrancar el contenedor.
4. `ENV` permite declarar una variable de entorno en el contenedor.
5. `EXPOSE` abre un puerto del contenedor.
6. `FROM` indica la imagen base que utilizarás para construir tu imagen personalizada. Esta opción es obligatoria, y además debe ser la primera instrucción del Dockerfile.
7. `MAINTAINER` es una valor opcional que te permite indicar quien es el que se encarga de mantener el Dockerfile.
8. `ONBUILD` te permite indicar un comando que se ejecutará cuando tu imagen sea utilizada para crear otra imagen.
9. `RUN` ejecuta un comando y guarda el resultado como una nueva capa.
10. `USER` define el usuario por defecto del contenedor.
11. `VOLUME` crea un volumen que es compartido por los diferentes contenedores o con el host
12. `WORKDIR` define el directorio de trabajo para el contenedor.

> Fuente: [Crea tus propias imágenes en Docker](https://atareao.es/tutorial/docker/crear-tus-propias-imagenes-docker/)
### Documentación
- [Crear imágenes en Docker](https://docs.docker.com/language/python/build-images/)