### Inconvenientes

##### Al instalar el modulo de MySQL-python hay que tener en cuenta:
 1. Se requiere pip
 1. Se requiere tener instalado mysql
 1. Se produce un error con el comando MySQL-python 
   * mysql.c(42) : fatal error C1083: Cannot open include file: 'config-win.h':
No such file or directory

##### Posibles soluciones
 1. Se soluciona instalando el conector de mysql mysql-connector-c-6.0.2-win32
   * [Se encuentra aqui] (https://dev.mysql.com/downloads/connector/c/6.0.html#downloads)
