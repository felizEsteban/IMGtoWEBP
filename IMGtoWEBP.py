import os
import platform
import subprocess
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image

def abrir_carpeta(carpeta):
    sistema = platform.system()
    try:
        if sistema == "Windows":
            os.startfile(carpeta)
        elif sistema == "Darwin":
            subprocess.run(["open", carpeta])
        else:
            subprocess.run(["xdg-open", carpeta])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir la carpeta: {e}")

def seleccionar_carpeta(variable, titulo):
    carpeta = filedialog.askdirectory(title=titulo)
    if carpeta:
        variable.set(carpeta)

def convertir():
    origen = origen_var.get()
    destino = destino_var.get()
    calidad = calidad_var.get()

    if not origen or not destino:
        messagebox.showwarning("Error", "Debes seleccionar ambas carpetas.")
        return

    try:
        calidad = int(calidad)
        if calidad < 1 or calidad > 100:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Error", "Ingresa una calidad válida (1-100).")
        return

    formatos_validos = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    archivos = [f for f in os.listdir(origen) if os.path.splitext(f)[1].lower() in formatos_validos]

    if not archivos:
        messagebox.showinfo("Sin imágenes", "No se encontraron imágenes válidas en la carpeta origen.")
        return

    progress_bar["maximum"] = len(archivos)
    progress_bar["value"] = 0
    status_var.set("Convirtiendo imágenes...")

    if not os.path.exists(destino):
        os.makedirs(destino)

    contador = 0
    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, f"{nombre}.webp")

        try:
            with Image.open(ruta_origen) as img:
                img.save(ruta_destino, 'webp', quality=calidad)
                contador += 1
        except Exception as e:
            print(f"Error con {archivo}: {e}")

        progress_bar["value"] = contador
        root.update_idletasks()

    status_var.set(f"{contador} imagen(es) convertida(s).")
    abrir_carpeta(destino)

# --- UI ---

root = Tk()
root.title("Convertidor a WebP by felizEsteban")
root.geometry("500x300")
root.resizable(False, False)

origen_var = StringVar()
destino_var = StringVar()
calidad_var = StringVar(value="85")
status_var = StringVar()

Label(root, text="Carpeta de origen:").pack(pady=5)
Button(root, text="Seleccionar carpeta", command=lambda: seleccionar_carpeta(origen_var, "Selecciona carpeta de imágenes")).pack()
Entry(root, textvariable=origen_var, width=60).pack()

Label(root, text="Carpeta de destino:").pack(pady=5)
Button(root, text="Seleccionar carpeta", command=lambda: seleccionar_carpeta(destino_var, "Selecciona carpeta de destino")).pack()
Entry(root, textvariable=destino_var, width=60).pack()

Label(root, text="Calidad (1-100):").pack(pady=5)
Entry(root, textvariable=calidad_var, width=10).pack()

Button(root, text="Convertir a WebP", command=convertir).pack(pady=10)

progress_bar = Progressbar(root, length=400)
progress_bar.pack(pady=10)

Label(root, textvariable=status_var).pack(pady=5)

root.mainloop()
