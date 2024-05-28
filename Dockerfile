# imagen base
FROM python:3
# establece el directorio de trabajo
WORKDIR /usr/src/app
# Copiar la carpeta myapp a /usr/src/app
COPY ./myapp/ .
# instalacion de requerimientos y dependencias
RUN pip3 install -r requirements.txt
# Crear las carpetas sync_files, public y private
RUN mkdir -p /sync_files/public /sync_files/private
# Copiar el script Python al contenedor
COPY myapp/generador.py /sync_files/private/generador.py
# Copiar el contenido del repositorio al contenedor
COPY . .
# Aperturo el puerto 5000 del contenedor
EXPOSE 5000

# Establecer el entrypoint
ENTRYPOINT ["/usr/src/app/initialize.sh"]
