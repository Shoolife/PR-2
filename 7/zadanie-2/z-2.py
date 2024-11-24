import numpy as np
import os

# Загрузка матрицы из файла
matrix_file_path = 'second_task.npy'
matrix = np.load(matrix_file_path)

# Устанавливаем пороговое значение
threshold = 500 + 7

# Создание массивов для индексов и значений
x = []
y = []
z = []

# Проход по матрице и отбор элементов, превышающих порог
rows, cols = matrix.shape
for i in range(rows):
    for j in range(cols):
        if matrix[i, j] > threshold:
            x.append(i)
            y.append(j)
            z.append(matrix[i, j])

# Преобразуем списки в numpy массивы
x = np.array(x)
y = np.array(y)
z = np.array(z)

# Сохранение массивов в формате .npz
npz_file_path = 'matrix_above_threshold.npz'
npz_compressed_file_path = 'matrix_above_threshold_compressed.npz'
np.savez(npz_file_path, x=x, y=y, z=z)
np.savez_compressed(npz_compressed_file_path, x=x, y=y, z=z)

# Сравнение размеров файлов
size_npz = os.path.getsize(npz_file_path)
size_npz_compressed = os.path.getsize(npz_compressed_file_path)

# Расчет разницы в размерах
compression_ratio = size_npz / size_npz_compressed

# Вывод размеров и коэффициента сжатия
print(f"Размер обычного файла .npz: {size_npz} байт")
print(f"Размер сжатого файла .npз: {size_npz_compressed} байт")
print(f"Сжатый файл меньше в {compression_ratio:.2f} раза")
