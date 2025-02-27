        import numpy as np
import pandas as pd
import csv
import os

### 1. Работа с NumPy ###
# Создаем массив от 0 до 9
arr = np.arange(10)
print("Исходный массив:", arr)

# Вывод элементов с индексами от 3 до 6
print("Элементы с индексами 3-6:", arr[3:7])

# Изменение значений элементов с индексами 7, 8, 9
arr[7:10] = [10, 20, 30]
print("Измененный массив:", arr)
