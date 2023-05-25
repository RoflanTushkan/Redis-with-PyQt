import sys
import redis
from PyQt5 import QtCore, QtWidgets
from gui import Ui_Hospital

class Patient:
    def __init__(self, patient_id, last_name, first_name, middle_name, date_of_birth, gender, department_number, patients_diagnosis):
        self.patient_id = patient_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.department_number = department_number
        self.patients_diagnosis = patients_diagnosis

class Department:
    def __init__(self, department_id, name, number_of_doctors, number_of_patients, redis_db):
        self.department_id = department_id
        self.name = name
        self.number_of_doctors = number_of_doctors
        self.number_of_patients = number_of_patients
        self.db = redis_db

class Doctor:
    def __init__(self, doctor_id, last_name, first_name, middle_name, specialty, department_number, redis_db):
        self.doctor_id = doctor_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.specialty = specialty
        self.department_number = department_number
        self.db = redis_db

class Treatment:
    def __init__(self, treatment_id, date_of_admission, department_number, patient, doctor, diagnosis, redis_db):
        self.treatment_id = treatment_id
        self.date_of_admission = date_of_admission
        self.department_number = department_number
        self.patient = patient
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.db = redis_db

class Diagnosis:
    def __init__(self, diagnosis_id, name, description):
        self.diagnosis_id = diagnosis_id
        self.name = name
        self.description = description

class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Hospital()
        self.ui.setupUi(self)
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        
        self.current_patient_id = self.get_next_available_patient_id()
        self.current_department_id = self.get_next_available_department_id()
        self.current_doctor_id = self.get_next_available_doctor_id()
        self.current_treatment_id = self.get_next_available_treatment_id()
        self.current_diagnosis_id = self.get_next_available_diagnosis_id()

        self.ui.patient_btn_add.clicked.connect(self.add_patient)
        self.ui.department_btn_add.clicked.connect(self.add_department)
        self.ui.doctor_btn_add.clicked.connect(self.add_doctor)
        self.ui.treatment_btn_add.clicked.connect(self.add_treatment)
        self.ui.diagnosis_btn_add.clicked.connect(self.add_diagnosis)

        self.ui.patient_tableWidget.cellClicked.connect(self.select_row)
        self.ui.department_tableWidget.cellClicked.connect(self.select_row)
        self.ui.doctor_tableWidget.cellClicked.connect(self.select_row)
        self.ui.treatment_tableWidget.cellClicked.connect(self.select_row)
        self.ui.diagnosis_tableWidget.cellClicked.connect(self.select_row)

        self.ui.patient_btn_delete.clicked.connect(self.delete_patient)
        self.ui.department_btn_delete.clicked.connect(self.delete_department)
        self.ui.doctor_btn_delete.clicked.connect(self.delete_doctor)
        self.ui.treatment_btn_delete.clicked.connect(self.delete_treatment)
        self.ui.diagnosis_btn_delete.clicked.connect(self.delete_diagnosis)

        self.ui.btn_refresh.clicked.connect(self.update_table_data)
        self.ui.department_btn_refresh.clicked.connect(self.update_table_data)
        self.ui.doctor_btn_refresh.clicked.connect(self.update_table_data)
        self.ui.treatment_btn_refresh.clicked.connect(self.update_table_data)
        self.ui.diagnosis_btn_refresh.clicked.connect(self.update_table_data)

        self.fetch_and_display_patients()
        self.update_patient_combobox()
        self.fetch_and_display_department()
        self.update_department_combobox()
        self.fetch_and_display_doctor()
        self.update_doctor_combobox()
        self.fetch_and_display_treatment()
        self.fetch_and_display_diagnosis()
        self.update_diagnosis_combobox()

    def get_next_available_patient_id(self):
        last_patient_id = self.redis_client.get("last_patient_id")
        if last_patient_id:
            last_patient_id = int(last_patient_id)
            existing_ids = {int(key.decode().split(":")[1]) for key in self.redis_client.keys("patient:*")}
            patient_ids = set(range(1, last_patient_id + 1))
            available_ids = patient_ids - existing_ids
            if available_ids:
                missing_ids = sorted(list(available_ids))
                return missing_ids[0]
            else:
                while last_patient_id in existing_ids:
                    last_patient_id += 1
                return last_patient_id
        else:
            return 1

    def update_next_patient_id(self):
        self.redis_client.set("last_patient_id", self.current_patient_id)

    def get_next_available_department_id(self):
        last_department_id = self.redis_client.get("last_department_id")
        if last_department_id:
            last_department_id = int(last_department_id)
            existing_ids = {int(key.decode().split(":")[1]) for key in self.redis_client.keys("department:*")}
            department_ids = set(range(1, last_department_id + 1))
            available_ids = department_ids - existing_ids
            if available_ids:
                missing_ids = sorted(list(available_ids))
                return missing_ids[0]
            else:
                while last_department_id in existing_ids:
                    last_department_id += 1
                return last_department_id
        else:
            return 1

    def update_next_department_id(self):
        self.redis_client.set("last_department_id", self.current_department_id)

    def get_next_available_doctor_id(self):
        last_doctor_id = self.redis_client.get("last_doctor_id")
        if last_doctor_id:
            last_doctor_id = int(last_doctor_id)
            existing_ids = {int(key.decode().split(":")[1]) for key in self.redis_client.keys("doctor:*")}
            doctor_ids = set(range(1, last_doctor_id + 1))
            available_ids = doctor_ids - existing_ids
            if available_ids:
                missing_ids = sorted(list(available_ids))
                return missing_ids[0]
            else:
                while last_doctor_id in existing_ids:
                    last_doctor_id += 1
                return last_doctor_id
        else:
            return 1

    def update_next_doctor_id(self):
        self.redis_client.set("last_doctor_id", self.current_doctor_id)

    def get_next_available_treatment_id(self):
        last_treatment_id = self.redis_client.get("last_treatment_id")
        if last_treatment_id:
            last_treatment_id = int(last_treatment_id)
            existing_ids = {int(key.decode().split(":")[1]) for key in self.redis_client.keys("treatment:*")}
            treatment_ids = set(range(1, last_treatment_id + 1))
            available_ids = treatment_ids - existing_ids
            if available_ids:
                missing_ids = sorted(list(available_ids))
                return missing_ids[0]
            else:
                while last_treatment_id in existing_ids:
                    last_treatment_id += 1
                return last_treatment_id
        else:
            return 1

    def update_next_treatment_id(self):
        self.redis_client.set("last_treatment_id", self.current_treatment_id)

    def get_next_available_diagnosis_id(self):
        last_diagnosis_id = self.redis_client.get("last_diagnosis_id")
        if last_diagnosis_id:
            last_diagnosis_id = int(last_diagnosis_id)
            existing_ids = {int(key.decode().split(":")[1]) for key in self.redis_client.keys("diagnosis:*")}
            diagnosis_ids = set(range(1, last_diagnosis_id + 1))
            available_ids = diagnosis_ids - existing_ids
            if available_ids:
                missing_ids = sorted(list(available_ids))
                return missing_ids[0]
            else:
                while last_diagnosis_id in existing_ids:
                    last_diagnosis_id += 1
                return last_diagnosis_id
        else:
            return 1

    def update_next_diagnosis_id(self):
        self.redis_client.set("last_diagnosis_id", self.current_diagnosis_id)

    def add_patient(self):
        last_name = self.ui.patient_last_name_line.text()
        first_name = self.ui.patient_first_name_line.text()
        middle_name = self.ui.lineEdit.text()
        date_of_birth = self.ui.patient_date_of_birth_dateEdit.date().toString("yyyy-MM-dd")
        gender = self.ui.patient_gender_comboBox.currentText()
        department_number = self.ui.patient_department_number_comboBox.currentText()
        patients_diagnosis = self.ui.patient_patients_diagnosis_comboBox.currentText()

        patient = Patient(self.current_patient_id, last_name, first_name, middle_name, date_of_birth, gender, department_number, patients_diagnosis)

        patient_data = {
            "last_name": patient.last_name,
            "first_name": patient.first_name,
            "middle_name": patient.middle_name,
            "date_of_birth": patient.date_of_birth,
            "gender": patient.gender,
            "department_number": patient.department_number,
            "patients_diagnosis": patient.patients_diagnosis
        }

        self.redis_client.hmset(f"patient:{self.current_patient_id}", patient_data)

        self.current_patient_id = self.get_next_available_patient_id()
        self.update_next_patient_id()

        QtWidgets.QMessageBox.information(self, "Успіх", "Дані пацієнта збережені в Redis.")

        self.ui.patient_last_name_line.clear()
        self.ui.patient_first_name_line.clear()
        self.ui.lineEdit.clear()
        self.ui.patient_date_of_birth_dateEdit.setDate(QtCore.QDate.currentDate())
        self.ui.patient_gender_comboBox.setCurrentIndex(0)
        self.ui.patient_department_number_comboBox.setCurrentIndex(0)
        self.ui.patient_patients_diagnosis_comboBox.setCurrentIndex(0)

        self.fetch_and_display_patients()
        self.update_department_combobox()
        self.update_patient_combobox()
        self.update_diagnosis_combobox()

    def add_department(self):
            name = self.ui.department_name_line.text()
            number_of_doctors = self.ui.department_number_of_doctors_spinBox.text()
            number_of_patients = self.ui.department_number_of_patients_spinBox.text()

            department_id = self.get_next_available_department_id()

            department = Department(department_id, name, number_of_doctors, number_of_patients, self.redis_client)

            department_data = {
                "name": department.name,
                "number_of_doctors": department.number_of_doctors,
                "number_of_patients": department.number_of_patients
            }

            self.redis_client.hmset(f"department:{department_id}", department_data)

            self.update_next_department_id()

            QtWidgets.QMessageBox.information(self, "Успіх", "Дані відділення збережені в Redis.")

            self.ui.department_name_line.clear()
            self.ui.department_number_of_doctors_spinBox.setValue(0)
            self.ui.department_number_of_patients_spinBox.setValue(0)

            self.fetch_and_display_department()
            
            self.update_department_combobox()

    def add_doctor(self):
                last_name = self.ui.doctor_last_name_line.text()
                first_name = self.ui.doctor_first_name_line.text()
                middle_name = self.ui.doctor_middle_name_line.text()
                specialty = self.ui.doctor_specialty_line.text()
                department_number = self.ui.doctor_department_number_comboBox.currentText()

                doctor_id = self.get_next_available_doctor_id()

                doctor = Doctor(doctor_id, last_name, first_name, middle_name, specialty, department_number, self.redis_client)

                doctor_data = {
                    "last_name": doctor.last_name,
                    "first_name": doctor.first_name,
                    "middle_name": doctor.middle_name,
                    "specialty": doctor.specialty,
                    "department_number": doctor.department_number
                }

                self.redis_client.hmset(f"doctor:{self.current_doctor_id}", doctor_data)

                self.current_doctor_id = self.get_next_available_doctor_id()
                self.update_next_doctor_id()

                QtWidgets.QMessageBox.information(self, "Успіх", "Дані лікаря збережені в Redis.")

                self.ui.doctor_last_name_line.clear()
                self.ui.doctor_first_name_line.clear()
                self.ui.doctor_middle_name_line.clear()
                self.ui.doctor_specialty_line.clear()
                self.ui.doctor_department_number_comboBox.setCurrentIndex(0)

                self.fetch_and_display_doctor()
                self.update_doctor_combobox()
                self.update_department_combobox()

    def add_treatment(self):
                    date_of_admission = self.ui.treatment_date_of_admission_dateEdit.date().toString("yyyy-MM-dd")
                    department_number = self.ui.treatment_department_number_comboBox.currentText()
                    patient = self.ui.treatment_patient_comboBox.currentText()
                    doctor = self.ui.treatment_doctor_comboBox.currentText()
                    diagnosis = self.ui.treatment_diagnosis_comboBox.currentText()

                    treatment_id = self.get_next_available_treatment_id()

                    treatment = Treatment(treatment_id, date_of_admission, department_number, patient, doctor, diagnosis, self.redis_client)

                    treatment_data = {
                        "date_of_admission": treatment.date_of_admission,
                        "department_number": treatment.department_number,
                        "patient": treatment.patient,
                        "doctor": treatment.doctor,
                        "diagnosis": treatment.diagnosis
                    }

                    self.redis_client.hmset(f"treatment:{treatment_id}", treatment_data)

                    self.update_next_treatment_id()

                    QtWidgets.QMessageBox.information(self, "Успіх", "Дані лікування збережені в Redis.")

                    self.ui.treatment_date_of_admission_dateEdit.setDate(QtCore.QDate.currentDate())
                    self.ui.treatment_department_number_comboBox.setCurrentIndex(0)
                    self.ui.treatment_patient_comboBox.setCurrentIndex(0)
                    self.ui.treatment_doctor_comboBox.setCurrentIndex(0)
                    self.ui.treatment_diagnosis_comboBox.setCurrentIndex(0)

                    self.fetch_and_display_treatment()
                    self.update_department_combobox()

    def add_diagnosis(self):
            # Отримання назви та опису діагнозу з відповідних полів інтерфейсу
            name = self.ui.diagnosis_name_lineEdit.text()
            description = self.ui.diagnosis_description_textEdit.toPlainText()

            # Створення об'єкту Diagnosis з отриманими даними
            diagnosis = Diagnosis(self.current_diagnosis_id, name, description)

            # Створення словника diagnosis_data з полями діагнозу та їх значеннями
            diagnosis_data = {
                "name": diagnosis.name, 
                "description": diagnosis.description
            }

            # Збереження даних діагнозу у базі даних Redis за допомогою hmset
            self.redis_client.hmset(f"diagnosis:{self.current_diagnosis_id}", diagnosis_data)

            # Оновлення current_diagnosis_id на наступний доступний ідентифікатор діагнозу
            self.current_diagnosis_id = self.get_next_available_diagnosis_id()
            self.update_next_diagnosis_id()

            # Відображення повідомлення про успішне збереження даних діагнозу
            QtWidgets.QMessageBox.information(self, "Успіх", "Дані діагноза збережені в Redis.")

            # Очищення полів введення даних діагнозу в інтерфейсі
            self.ui.diagnosis_name_lineEdit.clear()
            self.ui.diagnosis_description_textEdit.clear()

            # Оновлення таблиці діагнозів та комбобоксу з діагнозами
            self.fetch_and_display_diagnosis()
            self.update_diagnosis_combobox()

    def fetch_and_display_patients(self):
        self.ui.patient_tableWidget.setRowCount(0)

        patient_keys = self.redis_client.keys("patient:*")
        patient_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

        for key in patient_keys:
            patient_data = self.redis_client.hgetall(key)
            patient_id = key.decode()
            last_name = patient_data[b"last_name"].decode()
            first_name = patient_data[b"first_name"].decode()
            middle_name = patient_data[b"middle_name"].decode()
            date_of_birth = patient_data[b"date_of_birth"].decode()
            gender = patient_data[b"gender"].decode()
            department_id = patient_data[b"department_number"].decode()
            diagnosis_id = patient_data[b"patients_diagnosis"].decode()

            department_number = f"department:{department_id}"
            patients_diagnosis = f"diagnosis:{diagnosis_id}"


            row_position = self.ui.patient_tableWidget.rowCount()
            self.ui.patient_tableWidget.insertRow(row_position)

            self.ui.patient_tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(patient_id))
            self.ui.patient_tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(last_name))
            self.ui.patient_tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(first_name))
            self.ui.patient_tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(middle_name))
            self.ui.patient_tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(date_of_birth))
            self.ui.patient_tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(gender))
            self.ui.patient_tableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(department_number))
            self.ui.patient_tableWidget.setItem(row_position, 7, QtWidgets.QTableWidgetItem(patients_diagnosis))

    def fetch_and_display_department(self):
        self.ui.department_tableWidget.setRowCount(0)

        department_keys = self.redis_client.keys("department:*")
        department_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

        for key in department_keys:
            department_data = self.redis_client.hgetall(key)
            department_id = key.decode()
            name = department_data[b"name"].decode()
            number_of_doctors = department_data[b"number_of_doctors"].decode()
            number_of_patients = department_data[b"number_of_patients"].decode()

            row_position = self.ui.department_tableWidget.rowCount()
            self.ui.department_tableWidget.insertRow(row_position)

            self.ui.department_tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(department_id))
            self.ui.department_tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(name))
            self.ui.department_tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(number_of_doctors))
            self.ui.department_tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(number_of_patients))

    def fetch_and_display_doctor(self):
        self.ui.doctor_tableWidget.setRowCount(0)

        doctor_keys = self.redis_client.keys("doctor:*")
        doctor_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

        for key in doctor_keys:
            doctor_data = self.redis_client.hgetall(key)
            doctor_id = key.decode()

            last_name = doctor_data[b"last_name"].decode()
            first_name = doctor_data[b"first_name"].decode()
            middle_name = doctor_data[b"middle_name"].decode()
            specialty = doctor_data[b"specialty"].decode()
            department_id = doctor_data[b"department_number"].decode()

            department_number = f"department:{department_id}"

            row_position = self.ui.doctor_tableWidget.rowCount()
            self.ui.doctor_tableWidget.insertRow(row_position)

            self.ui.doctor_tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(doctor_id))
            self.ui.doctor_tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(last_name))
            self.ui.doctor_tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(first_name))
            self.ui.doctor_tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(middle_name))
            self.ui.doctor_tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(specialty))
            self.ui.doctor_tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(department_number))

    def fetch_and_display_treatment(self):
            self.ui.treatment_tableWidget.setRowCount(0)

            treatment_keys = self.redis_client.keys("treatment:*")
            treatment_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

            for key in treatment_keys:
                treatment_data = self.redis_client.hgetall(key)
                treatment_id = key.decode()

                date_of_admission = treatment_data[b"date_of_admission"].decode()
                department_id = treatment_data[b"department_number"].decode()
                patient_id = treatment_data[b"patient"].decode()
                doctor_id = treatment_data[b"doctor"].decode()
                diagnosis_id = treatment_data[b"diagnosis"].decode()

                department_number = f"department:{department_id}"
                patient = f"patient:{patient_id}"
                doctor = f"doctor:{doctor_id}"
                diagnosis = f"diagnosis:{diagnosis_id}"

                row_position = self.ui.treatment_tableWidget.rowCount()
                self.ui.treatment_tableWidget.insertRow(row_position)

                self.ui.treatment_tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(treatment_id))
                self.ui.treatment_tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(date_of_admission))
                self.ui.treatment_tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(department_number))
                self.ui.treatment_tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(patient))
                self.ui.treatment_tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(doctor))
                self.ui.treatment_tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(diagnosis))

    def fetch_and_display_diagnosis(self):
        # Очистити таблицю перед заповненням
        self.ui.diagnosis_tableWidget.setRowCount(0)

        # Отримати ключі всіх діагнозів з бази даних Redis
        diagnosis_keys = self.redis_client.keys("diagnosis:*")

        # Сортувати ключі діагнозів за їх числовим ідентифікатором
        diagnosis_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

        # Проходження по кожному ключу діагнозу
        for key in diagnosis_keys:
            # Отримати дані діагнозу з Redis
            diagnosis_data = self.redis_client.hgetall(key)
            diagnosis_id = key.decode()

            # Розпакування назви та опису діагнозу з отриманих даних
            name = diagnosis_data[b"name"].decode()
            description = diagnosis_data[b"description"].decode()

            # Додати новий рядок до таблиці і заповнити його даними
            row_position = self.ui.diagnosis_tableWidget.rowCount()
            self.ui.diagnosis_tableWidget.insertRow(row_position)
            self.ui.diagnosis_tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(diagnosis_id))
            self.ui.diagnosis_tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(name))
            self.ui.diagnosis_tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(description))

    def select_row(self, row):
        table_widget = self.sender()
        table_widget.selectRow(row)

        self.selected_row = row

    def update_department_combobox(self):
            self.ui.patient_department_number_comboBox.clear()
            self.ui.doctor_department_number_comboBox.clear()
            self.ui.treatment_department_number_comboBox.clear()

            department_keys = self.redis_client.keys("department:*")
            department_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

            for key in department_keys:
                department_id = key.decode().split(":")[1]
                self.ui.patient_department_number_comboBox.addItem(department_id)
                self.ui.doctor_department_number_comboBox.addItem(department_id)
                self.ui.treatment_department_number_comboBox.addItem(department_id)

    def update_patient_combobox(self):
            self.ui.treatment_patient_comboBox.clear()

            patient_keys = self.redis_client.keys("patient:*")
            patient_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

            for key in patient_keys:
                patient_id = key.decode().split(":")[1]
                self.ui.treatment_patient_comboBox.addItem(patient_id)

    def update_doctor_combobox(self):
            self.ui.treatment_doctor_comboBox.clear()

            doctor_keys = self.redis_client.keys("doctor:*")
            doctor_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

            for key in doctor_keys:
                doctor_id = key.decode().split(":")[1]
                self.ui.treatment_doctor_comboBox.addItem(doctor_id)

    def update_diagnosis_combobox(self):
        # Очищення комбобоксів з діагнозами пацієнта і лікування
        self.ui.patient_patients_diagnosis_comboBox.clear()
        self.ui.treatment_diagnosis_comboBox.clear()

        # Отримання всіх ключів діагнозів з Redis
        diagnosis_keys = self.redis_client.keys("diagnosis:*")

        # Сортування ключів діагнозів за числовою частиною ключа
        diagnosis_keys.sort(key=lambda k: int(k.decode().split(":")[1]))

        # Ітерація по кожному ключу діагнозу
        for key in diagnosis_keys:
            # Виділення ідентифікатора діагнозу з ключа
            diagnosis_id = key.decode().split(":")[1]
            # Додавання ідентифікатора діагнозу до комбо-боксу діагнозів пацієнта
            self.ui.patient_patients_diagnosis_comboBox.addItem(diagnosis_id)
            # Додавання ідентифікатора діагнозу до комбо-боксу діагнозів лікування
            self.ui.treatment_diagnosis_comboBox.addItem(diagnosis_id)

    def delete_patient(self):
        if hasattr(self, 'selected_row'):
            patient_id_item = self.ui.patient_tableWidget.item(self.selected_row, 0)
            if patient_id_item:
                patient_id = patient_id_item.text()
                self.redis_client.delete(patient_id.encode())
                self.fetch_and_display_patients()
                self.selected_row = None
                QtWidgets.QMessageBox.information(self, "Успіх", "Дані пацієнта видалені з Redis.")

                if not self.redis_client.keys("patient:*"):
                    self.current_patient_id = 1
                else:
                    self.current_patient_id = self.get_next_available_patient_id()
                self.update_next_patient_id()

                self.update_patient_combobox()

    def delete_department(self):
        if hasattr(self, 'selected_row'):
            department_id_item = self.ui.department_tableWidget.item(self.selected_row, 0)
            if department_id_item:
                department_id = department_id_item.text()
                self.redis_client.delete(department_id.encode())
                self.fetch_and_display_department()
                self.selected_row = None
                QtWidgets.QMessageBox.information(self, "Успіх", "Дані відділення видалені з Redis.")

                if not self.redis_client.keys("department:*"):
                    self.current_department_id = 1
                else:
                    self.current_department_id = self.get_next_available_department_id()
                self.update_next_department_id()

                self.update_department_combobox()

    def delete_doctor(self):
        if hasattr(self, 'selected_row'):
            doctor_id_item = self.ui.doctor_tableWidget.item(self.selected_row, 0)
            if doctor_id_item:
                doctor_id = doctor_id_item.text()
                self.redis_client.delete(doctor_id.encode())
                self.fetch_and_display_doctor()
                self.selected_row = None
                QtWidgets.QMessageBox.information(self, "Успіх", "Дані лікаря видалені з Redis.")

                if not self.redis_client.keys("doctor:*"):
                    self.current_doctor_id = 1
                else:
                    self.current_doctor_id = self.get_next_available_doctor_id()
                self.update_next_doctor_id()

                self.update_doctor_combobox()

    def delete_treatment(self):
        if hasattr(self, 'selected_row'):
            treatment_id_item = self.ui.treatment_tableWidget.item(self.selected_row, 0)
            if treatment_id_item:
                treatment_id = treatment_id_item.text()
                self.redis_client.delete(treatment_id.encode())
                self.fetch_and_display_treatment()
                self.selected_row = None
                QtWidgets.QMessageBox.information(self, "Успіх", "Дані пацієнта видалені з Redis.")

                if not self.redis_client.keys("treatment:*"):
                    self.current_treatment_id = 1
                else:
                    self.current_treatment_id = self.get_next_available_treatment_id()
                self.update_next_treatment_id()

    def delete_diagnosis(self):
        # Перевірка, чи існує вибраний рядок для видалення
        if hasattr(self, 'selected_row'):
            # Отримання елемента зі значенням ідентифікатора діагнозу з таблиці
            diagnosis_id_item = self.ui.diagnosis_tableWidget.item(self.selected_row, 0)
            if diagnosis_id_item:
                # Отримання текстового значення ідентифікатора діагнозу
                diagnosis_id = diagnosis_id_item.text()
                # Видалення діагнозу з Redis за його ідентифікатором
                self.redis_client.delete(diagnosis_id.encode())
                # Оновлення таблиці діагнозів
                self.fetch_and_display_diagnosis()
                # Скидання вибраного рядка на значення None
                self.selected_row = None
                # Відображення повідомлення про успішне видалення діагнозу
                QtWidgets.QMessageBox.information(self, "Успіх", "Дані діагноза видалені з Redis.")

                # Перевірка, чи існують ще діагнози в Redis
                if not self.redis_client.keys("diagnosis:*"):
                    # Якщо діагнозів немає, присвоєння початкового ідентифікатора 1
                    self.current_diagnosis_id = 1
                else:
                    # Якщо є діагнози, отримання наступного доступного ідентифікатора діагнозу
                    self.current_diagnosis_id = self.get_next_available_diagnosis_id()
                # Оновлення відображення наступного ідентифікатора діагнозу
                self.update_next_diagnosis_id()
                # Оновлення комбо-боксів з діагнозами
                self.update_diagnosis_combobox()

    def update_table_data(self):
        # Оновлення даних таблиць

        self.fetch_and_display_patients()
        self.fetch_and_display_department()
        self.fetch_and_display_doctor()
        self.fetch_and_display_treatment()
        self.fetch_and_display_diagnosis()

        # Відображення повідомлення про успішне оновлення даних таблиці
        QtWidgets.QMessageBox.information(self, "Успіх", "Дані таблиці оновлено з Redis».")

    def closeEvent(self, event):
        # Відображення діалогового вікна для підтвердження виходу
        reply = QtWidgets.QMessageBox.question(self, "Підтвердження", "Ви впевнені, що хочете вийти?", 
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        
        # Перевірка відповіді користувача
        if reply == QtWidgets.QMessageBox.Yes:
            # Якщо користувач підтвердив вихід, приймаємо подію закриття вікна
            event.accept()
        else:
            # Якщо користувач відмінив вихід, ігноруємо подію закриття вікна
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())
