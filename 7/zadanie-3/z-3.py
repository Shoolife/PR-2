import json
import msgpack
import os
from collections import defaultdict

# Загрузка JSON файла
file_path = 'third_task.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Агрегирование данных по товарам
aggregated_data = defaultdict(list)
for item in data:
    aggregated_data[item['name']].append(item['price'])

# Расчет средней, максимальной и минимальной цены для каждого товара
summary = {}
for name, prices in aggregated_data.items():
    summary[name] = {
        "average_price": sum(prices) / len(prices),
        "max_price": max(prices),
        "min_price": min(prices)
    }

# Сохранение агрегированных данных в формате JSON
json_output_path = 'aggregated_prices.json'
with open(json_output_path, 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=4)

# Сохранение агрегированных данных в формате MsgPack
msgpack_output_path = 'aggregated_prices.msgpack'
with open(msgpack_output_path, 'wb') as f:
    msgpack.pack(summary, f)

# Сравнение размеров файлов
json_size = os.path.getsize(json_output_path)
msgpack_size = os.path.getsize(msgpack_output_path)

# Вывод информации о размерах
print(f"JSON файл: {json_output_path}, размер: {json_size} байт")
print(f"MsgPack файл: {msgpack_output_path}, размер: {msgpack_size} байт")
print(f"MsgPack меньше JSON в {json_size / msgpack_size:.2f} раза")
