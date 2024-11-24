import pandas as pd
import json
import pickle
import msgpack
import os

# Загрузка данных
file_path = 'SpotifyFeatures.csv'  # Укажите путь к вашему файлу
output_dir = 'processed_data'      # Папка для сохранения результатов
os.makedirs(output_dir, exist_ok=True)

# Чтение данных
data = pd.read_csv(file_path)

# Шаг 1: Отбор 7-10 полей
selected_columns = [
    'genre', 'artist_name', 'track_name', 'duration_ms', 'danceability',
    'energy', 'key', 'loudness', 'speechiness', 'acousticness'
]
data = data[selected_columns]

# Шаг 2: Расчет характеристик для числовых и текстовых данных
numerical_summary = {}
categorical_summary = {}

for column in selected_columns:
    if pd.api.types.is_numeric_dtype(data[column]):  # Для числовых данных
        numerical_summary[column] = {
            "max": float(data[column].max()),
            "min": float(data[column].min()),
            "mean": float(data[column].mean()),
            "sum": float(data[column].sum()),
            "std": float(data[column].std())
        }
    elif pd.api.types.is_string_dtype(data[column]):  # Для текстовых данных
        categorical_summary[column] = data[column].value_counts().to_dict()

# Шаг 3: Сохранение расчетов в JSON
summary = {
    "numerical_summary": numerical_summary,
    "categorical_summary": categorical_summary
}
summary_path = os.path.join(output_dir, "data_summary.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=4)

# Шаг 4: Сохранение набора данных в разных форматах
csv_path = os.path.join(output_dir, "dataset.csv")
json_path = os.path.join(output_dir, "dataset.json")
msgpack_path = os.path.join(output_dir, "dataset.msgpack")
pkl_path = os.path.join(output_dir, "dataset.pkl")

# Сохранение в CSV
data.to_csv(csv_path, index=False)

# Сохранение в JSON
data.to_json(json_path, orient="records", lines=False, force_ascii=False)

# Сохранение в MsgPack
with open(msgpack_path, "wb") as f:
    packed = msgpack.packb(data.to_dict(orient="records"))
    f.write(packed)

# Сохранение в PKL
with open(pkl_path, "wb") as f:
    pickle.dump(data, f)

# Шаг 5: Сравнение размеров файлов
original_size = os.path.getsize(file_path)
file_sizes = {
    "CSV": os.path.getsize(csv_path),
    "JSON": os.path.getsize(json_path),
    "MsgPack": os.path.getsize(msgpack_path),
    "PKL": os.path.getsize(pkl_path)
}

# Расчет коэффициентов сжатия
compression_ratios = {fmt: original_size / size for fmt, size in file_sizes.items()}

# Вывод размеров файлов и коэффициентов сжатия
print(f"Размер исходного файла: {original_size / 1024:.2f} КБ")
for fmt, size in file_sizes.items():
    print(f"Размер файла {fmt}: {size / 1024:.2f} КБ (Сжатие: {compression_ratios[fmt]:.2f} раз)")

# Итог
print(f"Сводная информация сохранена в {summary_path}")
