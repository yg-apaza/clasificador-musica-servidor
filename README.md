# Clasificador de musica por género

## Requerimientos

Deben estar definidos en el PATH del sistema

- npm (Node Package Manager) 3.x
- NodeJS 5.x
- Python 2.x
- MySQL
```bash
sudo apt-get install libmysqlclient-dev
sudo apt-get install -y libfreetype6-dev libxft-dev
sudo apt-get install sox
```

## Instalacion

- Instalar dependencias globables como superusuario (administrador)
```bash
npm install -g bower
npm install -g gulp
```

- Instalar dependencias locales
```bash
npm install
bower install
```

- Instalar dependencias de Python
```bash
pip install -r requirements.txt
```

- Crear una base de datos 'clasificador' y ejecutar el script schema.sql

- Modificar el archivo settings.json (usuario y contraseña de la BD)

- Copiar las librerias a la carpeta static
```bash
gulp copy
```

## Ejecucion - Development

- Ejecutar
```bash
python -m run
```

- Abrir en un navegador localhost:5000

## Verificar

- Version de Python debe ser 2.x
```bash
python --version
```

- Pip debe ser para Python 2.x
```bash
pip --version
```
```bash
pip2 --version
```
