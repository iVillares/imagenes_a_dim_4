from PIL import Image, ImageOps
import os
import math

# 📌 CONFIGURACIÓN
input_folder = "imagenes"  # Carpeta con las fotos
output_folder = "salida"   # Carpeta de salida
img_size = (850, 850)  # 7 cm x 7 cm en píxeles (300 DPI)
a4_size = (2480, 3508)  # Tamaño A4 en píxeles (300 DPI)
cols, rows = 2, 3  # Máximo de imágenes por página (3x3 = 9 fotos por hoja)
margin = 60  # Margen en píxeles

# Crear carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 📌 Cargar imágenes
files = [f for f in os.listdir(input_folder) if f.lower().endswith(("jpeg", "png"))]

# 📌 Calcular cuántas páginas A4 necesitamos
fotos_por_pagina = cols * rows
paginas = math.ceil(len(files) / fotos_por_pagina)

print(f"Total de imágenes: {len(files)}")
print(f"Se generarán {paginas} páginas A4.")

# 📌 Procesar cada grupo de 9 fotos
for page in range(paginas):
    # Crear lienzo A4 en blanco
    a4_img = Image.new("RGB", a4_size, "white")

    # Seleccionar las fotos para esta página
    fotos_pagina = files[page * fotos_por_pagina : (page + 1) * fotos_por_pagina]

    for idx, file in enumerate(fotos_pagina):
        #img = Image.open(os.path.join(input_folder, file)).resize(img_size)
        # Ajustar la imagen manteniendo la proporción
        img = Image.open(os.path.join(input_folder, file))
        img = ImageOps.pad(img, img_size, method=Image.Resampling.LANCZOS, color="white")
        
        # Calcular posición en la cuadrícula
        x = margin + (idx % cols) * (img_size[0] + margin)
        y = margin + (idx // cols) * (img_size[1] + margin)+30

        # Pegar imagen en la hoja
        a4_img.paste(img, (x, y))

    # 📌 Guardar la página A4
    output_path = os.path.join(output_folder, f"pagina_{page+1}.jpg")
    a4_img.save(output_path, quality=95)
    print(f"Página {page+1} guardada en: {output_path}")

print("✅ Proceso terminado. ¡Listo para imprimir!")

