import random
import time
import os

while True:
    number = random.randint(1, 100)
    filename = f"{time.strftime('%d%m%Y%H%M%S')}.txt"
    with open(os.path.join("/sync_files/public", filename), 'w') as f:
        f.write(str(number))
        print("Archivo generado")
    time.sleep(1800)  # Esperar 30 minutos
