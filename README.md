# Integration Developer Challenge

El siguiente proyecto esta diseñado para:
* Leer un archivo CSV
* FIltrar los datos
* Almacenar los datos filtrados en una base de datos MySQL

## Instalación:
Los siguientes pasos fueron comprobados en un sistema operativo linux(Ubuntu 18.04 LTS) usando Python 3.6.9.

1. Instalación de MySQL:
```
sudo apt-get install mysql-server
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev
```

Puede ser necesario el crear un nuevo ususario para MySQL, para información sobre como crear y configurar los permisos visitar:

```
https://www.digitalocean.com/community/tutorials/crear-un-nuevo-usuario-y-otorgarle-permisos-en-mysql-es
```

2. Instalar librerías:
```
pip3 install -r requirements.txt
```

3. Configuración de usuario y clave
El último paso antes de ejecutar el script es cambiar el usuario y la clave de mysql en el archivo 'SQL_utils.py' en la linea 11 y 12 respectivamente.

## Funcionamiento
Para ejecutar el filtrado y la carga de los datos se deje ejecutar el siguiente comando despues de haber instalado las librerías
```
python3 ETL_movies.py <Nombre de la DB> <Nombre de la tabla>
```
