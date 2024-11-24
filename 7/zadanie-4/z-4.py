import pickle
import json

# Пути к файлам
pkl_products_path = "fourth_task_products.json"  # Этот файл на самом деле PKL
json_updates_path = "fourth_task_updates.json"  # Обычный JSON
updated_pkl_path = "updated_products.pkl"       # Для сохранения

# Чтение "PKL" файла с товарами
with open(pkl_products_path, "rb") as f:
    products = pickle.load(f)

# Чтение JSON файла с обновлениями
with open(json_updates_path, "r", encoding="utf-8") as f:
    updates = json.load(f)

# Обновление цен
for update in updates:
    for product in products:
        if product["name"] == update["name"]:
            if update["method"] == "add":  # Увеличиваем цену
                product["price"] += update["param"]
            elif update["method"] == "sub":  # Уменьшаем цену
                product["price"] -= update["param"]
            elif update["method"] == "percent+":  # Увеличиваем на процент
                product["price"] *= (1 + update["param"])
            elif update["method"] == "percent-":  # Уменьшаем на процент
                product["price"] *= (1 - update["param"])

# Сохранение обновленных данных обратно в PKL
with open(updated_pkl_path, "wb") as f:
    pickle.dump(products, f)
