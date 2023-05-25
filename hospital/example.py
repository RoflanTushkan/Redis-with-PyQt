import redis

# Підключення до Redis
r = redis.Redis()

# Функція для пошуку пацієнтів
def search_patients():
    # Отримання всіх ключів "treatment"
    treatment_keys = r.keys("treatment:*")

    # Перебір кожного ключа "treatment"
    for key in treatment_keys:
        # Отримання значень для поля "data_of_admission", "patient" та "department"
        data_of_admission = r.hget(key, "data_of_admission")
        patient_key = r.hget(key, "patient")
        department = r.hget(patient_key, "department")
        diagnosis = r.hget(patient_key, "diagnosis")

        # Перевірка на відділення 105, діагноз "flu" та дату після 2022.06.20
        if department == b"105" and diagnosis == b"flu" and data_of_admission > b"2022.06.20.":
            # Отримання прізвища та імені пацієнта
            last_name = r.hget(patient_key, "last_name")
            first_name = r.hget(patient_key, "first_name")

            # Виведення результату
            print(f"Patient: {last_name.decode()} {first_name.decode()}")

# Виклик функції пошуку пацієнтів
search_patients()
