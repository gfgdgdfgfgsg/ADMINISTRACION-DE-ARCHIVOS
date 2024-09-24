import tkinter as tk
from tkinter import messagebox

def countingSort(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (array[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        array[i] = output[i]

def radixSort(array):
    max_element = max(array)
    exp = 1
    while max_element // exp > 0:
        countingSort(array, exp)
        exp *= 10

def sort_numbers():
    input_text = entry.get()
    try:
        # Convertir la entrada a una lista de enteros
        numbers = list(map(int, input_text.split(',')))
        
        # Ordenar los números usando Radix Sort
        radixSort(numbers)
        
        # Mostrar el resultado en el label
        result_label.config(text="Array ordenado: " + ', '.join(map(str, numbers)))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una lista de números válidos separados por comas.")

# Crear la ventana principal
root = tk.Tk()
root.title("Radix Sort GUI")

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
