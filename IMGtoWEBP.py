import os
import platform
import subprocess
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox
from tkinter.ttk import Progressbar, Style
from PIL import Image


# Paleta de colores modo oscuro
PRIMARY_COLOR = "#7C4DFF"
PRIMARY_DARK = "#5E35B1"
PRIMARY_LIGHT = "#B39DDB"
SECONDARY_COLOR = "#FFAB40"
BACKGROUND_DARK = "#121212"
SURFACE_DARK = "#1E1E1E"
TEXT_COLOR = "#F5F5F5"

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

def seleccionar_archivo():
    return filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.tiff")])

def convertir_imagen_unica():
    archivo = seleccionar_archivo()
    if not archivo:
        return

    try:
        calidad = int(calidad_var.get())
        if calidad < 1 or calidad > 100:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Error", "Calidad inválida. Usa un número entre 1 y 100.")
        return

    destino = filedialog.askdirectory(title="Selecciona carpeta de destino")
    if not destino:
        return

    nombre = os.path.splitext(os.path.basename(archivo))[0]
    ruta_destino = os.path.join(destino, f"{nombre}.webp")

    try:
        with Image.open(archivo) as img:
            img.save(ruta_destino, 'webp', quality=calidad)
        messagebox.showinfo("Éxito", f"Imagen convertida a:\n{ruta_destino}")
        abrir_carpeta(destino)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo convertir la imagen:\n{e}")

def convertir_carpeta():
    origen = origen_var.get()
    destino = destino_var.get()

    if not origen or not destino:
        messagebox.showwarning("Error", "Debes seleccionar ambas carpetas.")
        return

    try:
        calidad = int(calidad_var.get())
        if calidad < 1 or calidad > 100:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Error", "Calidad inválida. Usa un número entre 1 y 100.")
        return

    formatos_validos = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    archivos = [f for f in os.listdir(origen) if os.path.splitext(f)[1].lower() in formatos_validos]

    if not archivos:
        messagebox.showinfo("Sin imágenes", "No se encontraron imágenes válidas en la carpeta.")
        return

    progress_bar["maximum"] = len(archivos)
    progress_bar["value"] = 0
    status_var.set("Convirtiendo imágenes...")

    if not os.path.exists(destino):
        os.makedirs(destino)

    contador = 0
    for archivo in archivos:
        nombre, ext = os.path.splitext(archivo)
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
root.title(" IMGtoWEBP - by felizEsteban")
root.geometry("540x400")
root.iconbitmap('converter.ico')
root.configure(bg=BACKGROUND_DARK)

# Estilos
style = Style()
style.theme_use("clam")
style.configure("TButton",
                background=PRIMARY_COLOR,
                foreground=TEXT_COLOR,
                font=('Segoe UI', 10, 'bold'),
                padding=8)
style.map("TButton",
        background=[("active", PRIMARY_DARK)],
        foreground=[("disabled", "#999")])

style.configure("TProgressbar",
                troughcolor=SURFACE_DARK,
                background=PRIMARY_LIGHT,
                thickness=10)

origen_var = StringVar()
destino_var = StringVar()
calidad_var = StringVar(value="85")
status_var = StringVar()

def dark_label(text):
    return Label(root, text=text, fg=TEXT_COLOR, bg=BACKGROUND_DARK, font=('Segoe UI', 10, 'bold'))

dark_label("Carpeta de origen:").pack(pady=5)
Button(root, text="Seleccionar carpeta", command=lambda: seleccionar_carpeta(origen_var, "Selecciona carpeta de imágenes")).pack(pady=8)
Entry(root, textvariable=origen_var, width=60, bg=SURFACE_DARK, fg=TEXT_COLOR, insertbackground=TEXT_COLOR).pack()

dark_label("Carpeta de destino:").pack(pady=5)
Button(root, text="Seleccionar carpeta", command=lambda: seleccionar_carpeta(destino_var, "Selecciona carpeta de destino")).pack(pady=8)
Entry(root, textvariable=destino_var, width=60, bg=SURFACE_DARK, fg=TEXT_COLOR, insertbackground=TEXT_COLOR).pack()

dark_label("Calidad (1-100):").pack(pady=5)
Entry(root, textvariable=calidad_var, width=10, bg=SURFACE_DARK, fg=TEXT_COLOR, insertbackground=TEXT_COLOR).pack()

# Botones con más separación y mejor diseño
Button(root, text="Convertir carpeta completa", command=convertir_carpeta).pack(pady=15)
Button(root, text="Convertir una sola imagen", command=convertir_imagen_unica).pack(pady=5)

progress_bar = Progressbar(root, length=420)
progress_bar.pack(pady=12)

Label(root, textvariable=status_var, fg=TEXT_COLOR, bg=BACKGROUND_DARK).pack(pady=5)

root.mainloop()
