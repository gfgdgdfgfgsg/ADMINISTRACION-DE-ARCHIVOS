
def countingSort(array, exp):
    """
    Función que realiza el ordenamiento por conteo en base a un dígito específico.
    :param array: Lista de números a ordenar.
    :param exp: El dígito actual (1, 10, 100, etc.) que se está utilizando para el ordenamiento.
    """
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
    """
    Función principal para implementar Radix Sort.
    :param array: Lista de números a ordenar.
    """
    # Encontrar el elemento máximo para saber cuántos dígitos tiene
    max_element = max(array)

 
    exp = 1
    while max_element // exp > 0:
        countingSort(array, exp)
        exp *= 10


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", arr)
    
    radixSort(arr)
    
    print("Array ordenado:", arr)
