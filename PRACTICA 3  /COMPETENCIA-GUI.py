import tkinter as tk
from tkinter import messagebox

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
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

def sort_numbers():
    input_text = entry.get()
    try:
        # Convertir la entrada a una lista de enteros
        numbers = list(map(int, input_text.split(',')))
        
        # Ordenar los números usando Merge Sort
        merge_sort(numbers)
        
        # Mostrar el resultado en el label
        result_label.config(text="Array ordenado: " + ', '.join(map(str, numbers)))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una lista de números válidos separados por comas.")

# Crear la ventana principal
root = tk.Tk()
root.title("Merge Sort GUI")

# Crear y colocar los widgets
label = tk.Label(root, text="Ingresa números separados por comas:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

sort_button = tk.Button(root, text="Ordenar", command=sort_numbers)
sort_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
