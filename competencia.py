import random

def merge_sort(arr, ascending=True):
    # Si la longitud del arreglo es mayor a 1, se divide
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio
        left_half = arr[:mid]  # Divide el arreglo en la mitad izquierda
        right_half = arr[mid:]  # Divide el arreglo en la mitad derecha

        # Llama recursivamente a merge_sort para ordenar ambas mitades
        merge_sort(left_half, ascending)
        merge_sort(right_half, ascending)

        i = j = k = 0  # Inicializa los índices para las mitades y el arreglo original

        # Combina las mitades ordenadas
        while i < len(left_half) and j < len(right_half):
            if (left_half[i] < right_half[j] and ascending) or (left_half[i] > right_half[j] and not ascending):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copia los elementos restantes de left_half, si los hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia los elementos restantes de right_half, si los hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Función para generar una lista aleatoria de números
def generate_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

# Función para muestrear la lista ordenada
def sample_list(arr, sample_size):
    if sample_size > len(arr):
        return arr  # Si el tamaño de muestra es mayor que la longitud de la lista, devuelve la lista completa
    
    # Selecciona aleatoriamente elementos de la lista ordenada
    sample = random.sample(arr, sample_size)
    
    # Devuelve la muestra ordenada
    return sorted(sample)

# Ejemplo de uso del algoritmo Merge Sort, generación de lista y muestreo
list_size = 10
min_value = 1
max_value = 100
arr = generate_list(list_size, min_value, max_value)
print("Lista desordenada:", arr)

# Ordenar la lista en orden ascendente
merge_sort(arr, ascending=True)
print("Lista ordenada ascendentemente:", arr)

# Ordenar la lista en orden descendente
merge_sort(arr, ascending=False)
print("Lista ordenada descendentemente:", arr)

# Muestrear la lista ordenada
sample_size = 3
sampled_list = sample_list(arr, sample_size)
print(f"Muestra de tamaño {sample_size}: {sampled_list}")
