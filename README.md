# IMGtoWEBP

**IMPORTANTE:** Para ejecutar correctamente esta herramienta, abre **`launcher.vbs`**.  
Este archivo se encarga de iniciar la aplicación sin consola y crear, si lo deseas, un acceso directo en el escritorio.

---

## Descripción

IMGtoWEBP es una herramienta gráfica desarrollada en Python que permite convertir imágenes en formatos comunes a `.webp` de forma rápida y sencilla. Está diseñada para ser práctica, ligera y fácil de usar, todo desde una sola ventana.

---

## ¿Qué hace?

- Convierte imágenes en formato `.jpg`, `.jpeg`, `.png`, `.bmp` y `.tiff` a `.webp`
- Permite seleccionar carpetas de origen y destino
- Ofrece opción para definir la calidad de salida (de 1 a 100)
- Muestra una barra de progreso en tiempo real durante la conversión
- Abre automáticamente la carpeta de destino al finalizar

---

## Requisitos

- Python 3.8 o superior
- Librerías utilizadas:
  - `tkinter` (incluida en Python)
  - `Pillow`

Si estás usando el entorno virtual `.venv` incluido, no es necesario instalar nada adicional.

---

## Cómo usar

1. Ejecuta `launcher.vbs` (doble clic).
2. Selecciona la carpeta de origen con imágenes.
3. Selecciona la carpeta donde se guardarán las imágenes `.webp`.
4. Define la calidad de conversión (1–100).
5. Haz clic en “Convertir a WebP”.
6. Se abrirá automáticamente la carpeta de destino con las imágenes convertidas.

---

## Estructura del proyecto

IMGtoWEBP/
├── IMGtoWEBP.py # Script principal
├── IMGtoWEBP.bat # Ejecuta con entorno virtual
├── launcher.vbs # Ejecuta sin consola y crea acceso directo al escritorio
├── converter.ico # Ícono personalizado
├── .venv/ # Entorno virtual con dependencias

---

## Observaciones

- El acceso directo al escritorio se genera automáticamente la primera vez que se ejecuta `launcher.vbs`.
- Si el antivirus detecta el archivo como amenaza, se trata de un falso positivo. El código fuente está disponible para revisión.
- El entorno virtual puede ser compartido junto con el proyecto sin necesidad de instalar dependencias manualmente.

---

**Desarrollado por felizEsteban**
