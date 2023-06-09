# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hospital(object):
    def setupUi(self, Hospital):
        Hospital.setObjectName("Hospital")
        Hospital.resize(1110, 573)
        self.centralwidget = QtWidgets.QWidget(Hospital)
        self.centralwidget.setObjectName("centralwidget")
        self.diagnosis_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.diagnosis_tabWidget.setGeometry(QtCore.QRect(0, 0, 1221, 701))
        self.diagnosis_tabWidget.setObjectName("diagnosis_tabWidget")
        self.patient_tab = QtWidgets.QWidget()
        self.patient_tab.setObjectName("patient_tab")
        self.patient_insert = QtWidgets.QGroupBox(self.patient_tab)
        self.patient_insert.setGeometry(QtCore.QRect(10, 10, 241, 500))
        self.patient_insert.setObjectName("patient_insert")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.patient_insert)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 201, 215))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.patient_last_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.patient_last_name_line.setText("")
        self.patient_last_name_line.setObjectName("patient_last_name_line")
        self.horizontalLayout.addWidget(self.patient_last_name_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.patient_first_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.patient_first_name_line.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_first_name_line.sizePolicy().hasHeightForWidth())
        self.patient_first_name_line.setSizePolicy(sizePolicy)
        self.patient_first_name_line.setAcceptDrops(True)
        self.patient_first_name_line.setObjectName("patient_first_name_line")
        self.horizontalLayout_2.addWidget(self.patient_first_name_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.patient_date_of_birth_dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.patient_date_of_birth_dateEdit.setObjectName("patient_date_of_birth_dateEdit")
        self.horizontalLayout_4.addWidget(self.patient_date_of_birth_dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.patient_gender_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.patient_gender_comboBox.setObjectName("patient_gender_comboBox")
        self.patient_gender_comboBox.addItem("")
        self.patient_gender_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.patient_gender_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.patient_department_number_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.patient_department_number_comboBox.setObjectName("patient_department_number_comboBox")
        self.horizontalLayout_6.addWidget(self.patient_department_number_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        self.patient_patients_diagnosis_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.patient_patients_diagnosis_comboBox.setObjectName("patient_patients_diagnosis_comboBox")
        self.horizontalLayout_15.addWidget(self.patient_patients_diagnosis_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.patient_insert)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 270, 201, 83))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.patient_btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.patient_btn_add.setObjectName("patient_btn_add")
        self.verticalLayout_3.addWidget(self.patient_btn_add)
        self.patient_btn_delete = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.patient_btn_delete.setObjectName("patient_btn_delete")
        self.verticalLayout_3.addWidget(self.patient_btn_delete)
        self.btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayout_3.addWidget(self.btn_refresh)
        self.groupBox = QtWidgets.QGroupBox(self.patient_tab)
        self.groupBox.setGeometry(QtCore.QRect(260, 10, 861, 501))
        self.groupBox.setObjectName("groupBox")
        self.patient_tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.patient_tableWidget.setGeometry(QtCore.QRect(20, 20, 821, 461))
        self.patient_tableWidget.setObjectName("patient_tableWidget")
        self.patient_tableWidget.setColumnCount(8)
        self.patient_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_tableWidget.setHorizontalHeaderItem(7, item)
        self.diagnosis_tabWidget.addTab(self.patient_tab, "")
        self.department_tab = QtWidgets.QWidget()
        self.department_tab.setObjectName("department_tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.department_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 10, 771, 501))
        self.groupBox_2.setObjectName("groupBox_2")
        self.department_tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.department_tableWidget.setGeometry(QtCore.QRect(20, 20, 731, 461))
        self.department_tableWidget.setObjectName("department_tableWidget")
        self.department_tableWidget.setColumnCount(4)
        self.department_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.department_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.department_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.department_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.department_tableWidget.setHorizontalHeaderItem(3, item)
        self.patient_insert_2 = QtWidgets.QGroupBox(self.department_tab)
        self.patient_insert_2.setGeometry(QtCore.QRect(10, 10, 241, 500))
        self.patient_insert_2.setObjectName("patient_insert_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.patient_insert_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 201, 215))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.department_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.department_name_line.setText("")
        self.department_name_line.setObjectName("department_name_line")
        self.horizontalLayout_7.addWidget(self.department_name_line)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.department_number_of_doctors_spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.department_number_of_doctors_spinBox.setObjectName("department_number_of_doctors_spinBox")
        self.horizontalLayout_8.addWidget(self.department_number_of_doctors_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.department_number_of_patients_spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.department_number_of_patients_spinBox.setObjectName("department_number_of_patients_spinBox")
        self.horizontalLayout_9.addWidget(self.department_number_of_patients_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.patient_insert_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 270, 201, 83))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.department_btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.department_btn_add.setObjectName("department_btn_add")
        self.verticalLayout_5.addWidget(self.department_btn_add)
        self.department_btn_delete = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.department_btn_delete.setObjectName("department_btn_delete")
        self.verticalLayout_5.addWidget(self.department_btn_delete)
        self.department_btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.department_btn_refresh.setObjectName("department_btn_refresh")
        self.verticalLayout_5.addWidget(self.department_btn_refresh)
        self.diagnosis_tabWidget.addTab(self.department_tab, "")
        self.doctor_tab = QtWidgets.QWidget()
        self.doctor_tab.setObjectName("doctor_tab")
        self.patient_insert_3 = QtWidgets.QGroupBox(self.doctor_tab)
        self.patient_insert_3.setGeometry(QtCore.QRect(10, 10, 241, 500))
        self.patient_insert_3.setObjectName("patient_insert_3")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.patient_insert_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 201, 215))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.doctor_last_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.doctor_last_name_line.setText("")
        self.doctor_last_name_line.setObjectName("doctor_last_name_line")
        self.horizontalLayout_10.addWidget(self.doctor_last_name_line)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.doctor_first_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.doctor_first_name_line.setText("")
        self.doctor_first_name_line.setObjectName("doctor_first_name_line")
        self.horizontalLayout_11.addWidget(self.doctor_first_name_line)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.doctor_middle_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.doctor_middle_name_line.setText("")
        self.doctor_middle_name_line.setObjectName("doctor_middle_name_line")
        self.horizontalLayout_12.addWidget(self.doctor_middle_name_line)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.doctor_specialty_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.doctor_specialty_line.setText("")
        self.doctor_specialty_line.setObjectName("doctor_specialty_line")
        self.horizontalLayout_13.addWidget(self.doctor_specialty_line)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.doctor_department_number_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.doctor_department_number_comboBox.setObjectName("doctor_department_number_comboBox")
        self.horizontalLayout_14.addWidget(self.doctor_department_number_comboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.patient_insert_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 270, 201, 83))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.doctor_btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.doctor_btn_add.setObjectName("doctor_btn_add")
        self.verticalLayout_7.addWidget(self.doctor_btn_add)
        self.doctor_btn_delete = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.doctor_btn_delete.setObjectName("doctor_btn_delete")
        self.verticalLayout_7.addWidget(self.doctor_btn_delete)
        self.doctor_btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.doctor_btn_refresh.setObjectName("doctor_btn_refresh")
        self.verticalLayout_7.addWidget(self.doctor_btn_refresh)
        self.groupBox_3 = QtWidgets.QGroupBox(self.doctor_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(260, 10, 771, 501))
        self.groupBox_3.setObjectName("groupBox_3")
        self.doctor_tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.doctor_tableWidget.setGeometry(QtCore.QRect(20, 20, 731, 461))
        self.doctor_tableWidget.setObjectName("doctor_tableWidget")
        self.doctor_tableWidget.setColumnCount(6)
        self.doctor_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_tableWidget.setHorizontalHeaderItem(5, item)
        self.diagnosis_tabWidget.addTab(self.doctor_tab, "")
        self.treatment_tab = QtWidgets.QWidget()
        self.treatment_tab.setObjectName("treatment_tab")
        self.groupBox_4 = QtWidgets.QGroupBox(self.treatment_tab)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 10, 771, 501))
        self.groupBox_4.setObjectName("groupBox_4")
        self.treatment_tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.treatment_tableWidget.setGeometry(QtCore.QRect(20, 20, 731, 461))
        self.treatment_tableWidget.setObjectName("treatment_tableWidget")
        self.treatment_tableWidget.setColumnCount(6)
        self.treatment_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.treatment_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.treatment_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.treatment_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.treatment_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.treatment_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.treatment_tableWidget.setHorizontalHeaderItem(5, item)
        self.patient_insert_4 = QtWidgets.QGroupBox(self.treatment_tab)
        self.patient_insert_4.setGeometry(QtCore.QRect(10, 10, 241, 500))
        self.patient_insert_4.setObjectName("patient_insert_4")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.patient_insert_4)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 201, 215))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.treatment_date_of_admission_dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_7)
        self.treatment_date_of_admission_dateEdit.setObjectName("treatment_date_of_admission_dateEdit")
        self.horizontalLayout_16.addWidget(self.treatment_date_of_admission_dateEdit)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.treatment_department_number_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.treatment_department_number_comboBox.setObjectName("treatment_department_number_comboBox")
        self.horizontalLayout_17.addWidget(self.treatment_department_number_comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.treatment_patient_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.treatment_patient_comboBox.setObjectName("treatment_patient_comboBox")
        self.horizontalLayout_18.addWidget(self.treatment_patient_comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.treatment_doctor_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.treatment_doctor_comboBox.setObjectName("treatment_doctor_comboBox")
        self.horizontalLayout_19.addWidget(self.treatment_doctor_comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.treatment_diagnosis_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.treatment_diagnosis_comboBox.setObjectName("treatment_diagnosis_comboBox")
        self.horizontalLayout_20.addWidget(self.treatment_diagnosis_comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_20)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.patient_insert_4)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 270, 201, 83))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.treatment_btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.treatment_btn_add.setObjectName("treatment_btn_add")
        self.verticalLayout_9.addWidget(self.treatment_btn_add)
        self.treatment_btn_delete = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.treatment_btn_delete.setObjectName("treatment_btn_delete")
        self.verticalLayout_9.addWidget(self.treatment_btn_delete)
        self.treatment_btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.treatment_btn_refresh.setObjectName("treatment_btn_refresh")
        self.verticalLayout_9.addWidget(self.treatment_btn_refresh)
        self.diagnosis_tabWidget.addTab(self.treatment_tab, "")
        self.diagnosis_tab = QtWidgets.QWidget()
        self.diagnosis_tab.setObjectName("diagnosis_tab")
        self.patient_insert_5 = QtWidgets.QGroupBox(self.diagnosis_tab)
        self.patient_insert_5.setGeometry(QtCore.QRect(10, 10, 241, 500))
        self.patient_insert_5.setObjectName("patient_insert_5")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.patient_insert_5)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(20, 20, 201, 215))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_21.addWidget(self.label_21)
        self.diagnosis_name_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.diagnosis_name_lineEdit.setObjectName("diagnosis_name_lineEdit")
        self.horizontalLayout_21.addWidget(self.diagnosis_name_lineEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_10.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_25.addWidget(self.label_25)
        self.diagnosis_description_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_9)
        self.diagnosis_description_textEdit.setObjectName("diagnosis_description_textEdit")
        self.horizontalLayout_25.addWidget(self.diagnosis_description_textEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.patient_insert_5)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(20, 270, 201, 83))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.diagnosis_btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.diagnosis_btn_add.setObjectName("diagnosis_btn_add")
        self.verticalLayout_11.addWidget(self.diagnosis_btn_add)
        self.diagnosis_btn_delete = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.diagnosis_btn_delete.setObjectName("diagnosis_btn_delete")
        self.verticalLayout_11.addWidget(self.diagnosis_btn_delete)
        self.diagnosis_btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.diagnosis_btn_refresh.setObjectName("diagnosis_btn_refresh")
        self.verticalLayout_11.addWidget(self.diagnosis_btn_refresh)
        self.groupBox_5 = QtWidgets.QGroupBox(self.diagnosis_tab)
        self.groupBox_5.setGeometry(QtCore.QRect(260, 10, 771, 501))
        self.groupBox_5.setObjectName("groupBox_5")
        self.diagnosis_tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.diagnosis_tableWidget.setGeometry(QtCore.QRect(20, 20, 731, 461))
        self.diagnosis_tableWidget.setObjectName("diagnosis_tableWidget")
        self.diagnosis_tableWidget.setColumnCount(3)
        self.diagnosis_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.diagnosis_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.diagnosis_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.diagnosis_tableWidget.setHorizontalHeaderItem(2, item)
        self.diagnosis_tabWidget.addTab(self.diagnosis_tab, "")
        Hospital.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hospital)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        Hospital.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hospital)
        self.statusbar.setObjectName("statusbar")
        Hospital.setStatusBar(self.statusbar)

        self.retranslateUi(Hospital)
        self.diagnosis_tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Hospital)

    def retranslateUi(self, Hospital):
        _translate = QtCore.QCoreApplication.translate
        Hospital.setWindowTitle(_translate("Hospital", "Hospital"))
        self.patient_insert.setTitle(_translate("Hospital", "Управління"))
        self.label_4.setText(_translate("Hospital", "Прізвище"))
        self.label_5.setText(_translate("Hospital", "Ім\'я"))
        self.label_3.setText(_translate("Hospital", "По батькові"))
        self.label_2.setText(_translate("Hospital", "Дата народження"))
        self.label.setText(_translate("Hospital", "Стать"))
        self.patient_gender_comboBox.setItemText(0, _translate("Hospital", "Чоловіча"))
        self.patient_gender_comboBox.setItemText(1, _translate("Hospital", "Жіноча"))
        self.label_6.setText(_translate("Hospital", "Відділення"))
        self.label_15.setText(_translate("Hospital", "Діагноз"))
        self.patient_btn_add.setText(_translate("Hospital", "Додати"))
        self.patient_btn_delete.setText(_translate("Hospital", "Видалити"))
        self.btn_refresh.setText(_translate("Hospital", "Оновити дані таблиці"))
        self.groupBox.setTitle(_translate("Hospital", "Перегляд"))
        item = self.patient_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Hospital", "ID"))
        item = self.patient_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Hospital", "Прізвище"))
        item = self.patient_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Hospital", "Ім\'я"))
        item = self.patient_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Hospital", "По батькові"))
        item = self.patient_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Hospital", "Дата народження"))
        item = self.patient_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Hospital", "Стать"))
        item = self.patient_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Hospital", "Відділення"))
        item = self.patient_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Hospital", "Діагноз"))
        self.diagnosis_tabWidget.setTabText(self.diagnosis_tabWidget.indexOf(self.patient_tab), _translate("Hospital", "Пацієнт"))
        self.groupBox_2.setTitle(_translate("Hospital", "Перегляд"))
        item = self.department_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Hospital", "ID"))
        item = self.department_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Hospital", "Назва"))
        item = self.department_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Hospital", "Кількість лікарів"))
        item = self.department_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Hospital", "Кількість пацієнтів"))
        self.patient_insert_2.setTitle(_translate("Hospital", "Управління"))
        self.label_7.setText(_translate("Hospital", "Назва"))
        self.label_8.setText(_translate("Hospital", "Кількість лікарів"))
        self.label_9.setText(_translate("Hospital", "Кількість пацієнтів"))
        self.department_btn_add.setText(_translate("Hospital", "Додати"))
        self.department_btn_delete.setText(_translate("Hospital", "Видалити"))
        self.department_btn_refresh.setText(_translate("Hospital", "Оновити дані таблиці"))
        self.diagnosis_tabWidget.setTabText(self.diagnosis_tabWidget.indexOf(self.department_tab), _translate("Hospital", "Відділення"))
        self.patient_insert_3.setTitle(_translate("Hospital", "Управління"))
        self.label_10.setText(_translate("Hospital", "Прізвище"))
        self.label_11.setText(_translate("Hospital", "Ім\'я"))
        self.label_12.setText(_translate("Hospital", "По батькові"))
        self.label_13.setText(_translate("Hospital", "Спеціальність"))
        self.label_14.setText(_translate("Hospital", "Відділення"))
        self.doctor_btn_add.setText(_translate("Hospital", "Додати"))
        self.doctor_btn_delete.setText(_translate("Hospital", "Видалити"))
        self.doctor_btn_refresh.setText(_translate("Hospital", "Оновити дані таблиці"))
        self.groupBox_3.setTitle(_translate("Hospital", "Перегляд"))
        item = self.doctor_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Hospital", "ID"))
        item = self.doctor_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Hospital", "Призвіще"))
        item = self.doctor_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Hospital", "Ім\'я"))
        item = self.doctor_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Hospital", "По батькові"))
        item = self.doctor_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Hospital", "Спеціальність"))
        item = self.doctor_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Hospital", "Відділення"))
        self.diagnosis_tabWidget.setTabText(self.diagnosis_tabWidget.indexOf(self.doctor_tab), _translate("Hospital", "Лікар"))
        self.groupBox_4.setTitle(_translate("Hospital", "Перегляд"))
        item = self.treatment_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Hospital", "ID"))
        item = self.treatment_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Hospital", "Дата находження"))
        item = self.treatment_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Hospital", "Відділення"))
        item = self.treatment_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Hospital", "Пацієнт"))
        item = self.treatment_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Hospital", "Лікар"))
        item = self.treatment_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Hospital", "Діагноз"))
        self.patient_insert_4.setTitle(_translate("Hospital", "Управління"))
        self.label_16.setText(_translate("Hospital", "Дата находження"))
        self.label_17.setText(_translate("Hospital", "Відділення"))
        self.label_18.setText(_translate("Hospital", "Пацієнт"))
        self.label_19.setText(_translate("Hospital", "Лікар"))
        self.label_20.setText(_translate("Hospital", "Діагноз"))
        self.treatment_btn_add.setText(_translate("Hospital", "Додати"))
        self.treatment_btn_delete.setText(_translate("Hospital", "Видалити"))
        self.treatment_btn_refresh.setText(_translate("Hospital", "Оновити дані таблиці"))
        self.diagnosis_tabWidget.setTabText(self.diagnosis_tabWidget.indexOf(self.treatment_tab), _translate("Hospital", "Лікування"))
        self.patient_insert_5.setTitle(_translate("Hospital", "Управління"))
        self.label_21.setText(_translate("Hospital", "Назва"))
        self.label_25.setText(_translate("Hospital", "Опис"))
        self.diagnosis_btn_add.setText(_translate("Hospital", "Додати"))
        self.diagnosis_btn_delete.setText(_translate("Hospital", "Видалити"))
        self.diagnosis_btn_refresh.setText(_translate("Hospital", "Оновити дані таблиці"))
        self.groupBox_5.setTitle(_translate("Hospital", "Перегляд"))
        item = self.diagnosis_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Hospital", "ID"))
        item = self.diagnosis_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Hospital", "Назва"))
        item = self.diagnosis_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Hospital", "Опис"))
        self.diagnosis_tabWidget.setTabText(self.diagnosis_tabWidget.indexOf(self.diagnosis_tab), _translate("Hospital", "Діагноз"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hospital = QtWidgets.QMainWindow()
    ui = Ui_Hospital()
    ui.setupUi(Hospital)
    Hospital.show()
    sys.exit(app.exec_())
