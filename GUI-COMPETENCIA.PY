import tkinter as tk
from tkinter import messagebox
import random

def merge_sort(arr, ascending=True):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, ascending)
        merge_sort(right_half, ascending)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if (left_half[i] < right_half[j] and ascending) or (left_half[i] > right_half[j] and not ascending):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def generate_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def sample_list(arr, sample_size):
    if sample_size > len(arr):
        return arr
    
    sample = random.sample(arr, sample_size)
    return sorted(sample)

def sort_and_sample():
    try:
        list_size = int(entry_size.get())
        min_value = int(entry_min.get())
        max_value = int(entry_max.get())
        sample_size = int(entry_sample.get())

        if list_size <= 0 or min_value >= max_value or sample_size <= 0:
            raise ValueError("Valores no válidos")

        # Generar lista aleatoria
        arr = generate_list(list_size, min_value, max_value)
        output_original.delete(0, tk.END)
        output_original.insert(tk.END, str(arr))

        # Ordenar en orden ascendente
        merge_sort(arr, ascending=True)
        output_sorted_asc.delete(0, tk.END)
        output_sorted_asc.insert(tk.END, str(arr))

        # Ordenar en orden descendente
        merge_sort(arr, ascending=False)
        output_sorted_desc.delete(0, tk.END)
        output_sorted_desc.insert(tk.END, str(arr))

        # Muestrear la lista ordenada
        sampled_list = sample_list(arr, sample_size)
        output_sampled.delete(0, tk.END)
        output_sampled.insert(tk.END, str(sampled_list))

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset_fields():
    entry_size.delete(0, tk.END)
    entry_min.delete(0, tk.END)
    entry_max.delete(0, tk.END)
    entry_sample.delete(0, tk.END)
    
    output_original.delete(0, tk.END)
    output_sorted_asc.delete(0, tk.END)
    output_sorted_desc.delete(0, tk.END)
    output_sampled.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Merge Sort GUI")

# Instrucciones
instructions = "Ingresa los valores deseados para el tamaño de la lista y los valores mínimo y máximo.\n" \
               "Haz clic en 'Generar y Ordenar' para ver los resultados.\n" \
               "Si deseas reiniciar los campos y realizar otra operación sin cerrar la aplicación," \
               " simplemente haz clic en 'Reiniciar'."
tk.Label(root, text=instructions).grid(row=0, columnspan=2)

# Crear los widgets de entrada
tk.Label(root, text="Tamaño de la lista:").grid(row=1, column=0)
entry_size = tk.Entry(root)
entry_size.grid(row=1, column=1)

tk.Label(root, text="Valor mínimo:").grid(row=2, column=0)
entry_min = tk.Entry(root)
entry_min.grid(row=2, column=1)

tk.Label(root, text="Valor máximo:").grid(row=3, column=0)
entry_max = tk.Entry(root)
entry_max.grid(row=3, column=1)

tk.Label(root, text="Tamaño de muestra:").grid(row=4, column=0)
entry_sample = tk.Entry(root)
entry_sample.grid(row=4, column=1)

# Botón para ejecutar el algoritmo
btn_sort_sample = tk.Button(root, text="Generar y Ordenar", command=sort_and_sample)
btn_sort_sample.grid(row=5, columnspan=2)

# Botón para reiniciar los campos
btn_reset = tk.Button(root, text="Reiniciar", command=reset_fields)
btn_reset.grid(row=6, columnspan=2)

# Salidas
tk.Label(root, text="Lista Original:").grid(row=7, column=0)
output_original = tk.Entry(root, width=50)
output_original.grid(row=7, column=1)

tk.Label(root, text="Lista Ordenada Ascendente:").grid(row=8, column=0)
output_sorted_asc = tk.Entry(root, width=50)
output_sorted_asc.grid(row=8, column=1)

tk.Label(root, text="Lista Ordenada Descendente:").grid(row=9, column=0)
output_sorted_desc = tk.Entry(root, width=50)
output_sorted_desc.grid(row=9, column=1)

tk.Label(root, text="Muestra:").grid(row=10, column=0)
output_sampled = tk.Entry(root, width=50)
output_sampled.grid(row=10, column=1)

# Iniciar el bucle principal de la GUI
root.mainloop()
