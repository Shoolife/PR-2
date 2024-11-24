import numpy as np
import json

# Загружаем матрицу из файла
file_path = 'first_task.npy'
matrix = np.load(file_path)

# Выполняем вычисления
total_sum = matrix.sum()
average = matrix.mean()

# Главная диагональ
main_diag = np.diag(matrix)
sum_main_diag = main_diag.sum()
avg_main_diag = main_diag.mean()

# Побочная диагональ
sec_diag = np.diag(np.fliplr(matrix))
sum_sec_diag = sec_diag.sum()
avg_sec_diag = sec_diag.mean()

# Максимальное и минимальное значения
max_value = matrix.max()
min_value = matrix.min()

# Преобразуем результаты в стандартные Python-типы для JSON
results = {
    "sum": float(total_sum),
    "avr": float(average),
    "sumMD": float(sum_main_diag),
    "avrMD": float(avg_main_diag),
    "sumSD": float(sum_sec_diag),
    "avrSD": float(avg_sec_diag),
    "max": float(max_value),
    "min": float(min_value)
}

# Сохраняем результаты в JSON-файл
json_file_path = 'matrix_results.json'
with open(json_file_path, 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Нормализуем матрицу
normalized_matrix = (matrix - min_value) / (max_value - min_value)

# Сохраняем нормализованную матрицу в новый файл
normalized_file_path = 'normalized_matrix.npy'
np.save(normalized_file_path, normalized_matrix)