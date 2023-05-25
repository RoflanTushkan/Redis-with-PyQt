import redis

# Підключення до першої бази даних Redis
r = redis.Redis(host='localhost', port=6379, db=1)

# Отримання всіх ключів, що відповідають шаблону "patient:*"
keys = r.keys("patient:*")

# Проходження по кожному ключу
for key in keys:
    # Отримання значень всіх полів ключа
    data = r.hgetall(key)

    # Перевірка значення параметра "department_number" для кожного ключа
    if data[b'department_number'].decode('utf-8') == '105':
        # Виведення даних пацієнта з відділенням 105
        print(f"Department 105: {data[b'last_name'].decode('utf-8')} {data[b'first_name'].decode('utf-8')}")

# Закриття з'єднання з Redis базою даних
r.close()



