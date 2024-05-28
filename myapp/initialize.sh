#!/bin/bash

# Obtener el ID del contenedor
CONTAINER_ID=$(hostname)

# Crear la carpeta en /sync_files/private con el ID del contenedor
mkdir -p /sync_files/private/$CONTAINER_ID

# Ejecutar la aplicación principal
exec python3 ./app.py & python3 ./generador.py