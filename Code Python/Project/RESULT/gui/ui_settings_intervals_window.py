# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_intervals_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(710, 407)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.fromInterval_timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.fromInterval_timeEdit.setGeometry(QtCore.QRect(40, 10, 150, 40))
        self.fromInterval_timeEdit.setObjectName("fromInterval_timeEdit")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(200, 10, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.toInterval_timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.toInterval_timeEdit.setGeometry(QtCore.QRect(230, 10, 140, 40))
        self.toInterval_timeEdit.setObjectName("toInterval_timeEdit")
        self.alternativeIntervals_groupBox = QtWidgets.QGroupBox(Dialog)
        self.alternativeIntervals_groupBox.setGeometry(QtCore.QRect(470, 240, 230, 150))
        self.alternativeIntervals_groupBox.setObjectName("alternativeIntervals_groupBox")
        self.addAllIntervals_pushButton = QtWidgets.QPushButton(self.alternativeIntervals_groupBox)
        self.addAllIntervals_pushButton.setGeometry(QtCore.QRect(120, 100, 100, 40))
        self.addAllIntervals_pushButton.setObjectName("addAllIntervals_pushButton")
        self.label_3 = QtWidgets.QLabel(self.alternativeIntervals_groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 140, 17))
        self.label_3.setObjectName("label_3")
        self.alternativeIntervals_comboBox = QtWidgets.QComboBox(self.alternativeIntervals_groupBox)
        self.alternativeIntervals_comboBox.setGeometry(QtCore.QRect(10, 60, 210, 23))
        self.alternativeIntervals_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.alternativeIntervals_comboBox.setObjectName("alternativeIntervals_comboBox")
        self.addInterval_pushButton = QtWidgets.QPushButton(self.alternativeIntervals_groupBox)
        self.addInterval_pushButton.setGeometry(QtCore.QRect(10, 100, 97, 40))
        self.addInterval_pushButton.setObjectName("addInterval_pushButton")
        self.intervals_listBox = QtWidgets.QListWidget(Dialog)
        self.intervals_listBox.setGeometry(QtCore.QRect(10, 89, 450, 251))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.intervals_listBox.setFont(font)
        self.intervals_listBox.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.intervals_listBox.setObjectName("intervals_listBox")
        self.deleteInterval_button = QtWidgets.QPushButton(Dialog)
        self.deleteInterval_button.setGeometry(QtCore.QRect(10, 350, 110, 40))
        self.deleteInterval_button.setObjectName("deleteInterval_button")
        self.clearAllIntervals_button = QtWidgets.QPushButton(Dialog)
        self.clearAllIntervals_button.setGeometry(QtCore.QRect(140, 350, 150, 40))
        self.clearAllIntervals_button.setObjectName("clearAllIntervals_button")
        self.joinIntervals_groupBox = QtWidgets.QGroupBox(Dialog)
        self.joinIntervals_groupBox.setGeometry(QtCore.QRect(470, 60, 230, 170))
        self.joinIntervals_groupBox.setObjectName("joinIntervals_groupBox")
        self.label = QtWidgets.QLabel(self.joinIntervals_groupBox)
        self.label.setGeometry(QtCore.QRect(80, 30, 80, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.joinIntervals_groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 80, 17))
        self.label_2.setObjectName("label_2")
        self.joinIntervals_pushButton = QtWidgets.QPushButton(self.joinIntervals_groupBox)
        self.joinIntervals_pushButton.setGeometry(QtCore.QRect(70, 130, 90, 29))
        self.joinIntervals_pushButton.setObjectName("joinIntervals_pushButton")
        self.interval1_comboBox = QtWidgets.QComboBox(self.joinIntervals_groupBox)
        self.interval1_comboBox.setGeometry(QtCore.QRect(10, 50, 210, 23))
        self.interval1_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.interval1_comboBox.setObjectName("interval1_comboBox")
        self.interval2_comboBox = QtWidgets.QComboBox(self.joinIntervals_groupBox)
        self.interval2_comboBox.setGeometry(QtCore.QRect(10, 100, 210, 23))
        self.interval2_comboBox.setMaxVisibleItems(10)
        self.interval2_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.interval2_comboBox.setObjectName("interval2_comboBox")
        self.saveIntervals_button = QtWidgets.QPushButton(Dialog)
        self.saveIntervals_button.setGeometry(QtCore.QRect(310, 350, 150, 40))
        self.saveIntervals_button.setObjectName("saveIntervals_button")
        self.changeInterval_button = QtWidgets.QPushButton(Dialog)
        self.changeInterval_button.setGeometry(QtCore.QRect(390, 10, 120, 40))
        self.changeInterval_button.setObjectName("changeInterval_button")
        self.addInterval_button = QtWidgets.QPushButton(Dialog)
        self.addInterval_button.setGeometry(QtCore.QRect(520, 10, 120, 40))
        self.addInterval_button.setObjectName("addInterval_button")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 450, 30))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройка интервалов"))
        self.label_7.setText(_translate("Dialog", "От"))
        self.fromInterval_timeEdit.setDisplayFormat(_translate("Dialog", "H.m.s.zzz"))
        self.label_8.setText(_translate("Dialog", "До"))
        self.toInterval_timeEdit.setDisplayFormat(_translate("Dialog", "H.m.s.zzz"))
        self.alternativeIntervals_groupBox.setTitle(_translate("Dialog", "Альтернативный тип"))
        self.addAllIntervals_pushButton.setText(_translate("Dialog", "Добавить все"))
        self.label_3.setText(_translate("Dialog", "Выберите интервал"))
        self.addInterval_pushButton.setText(_translate("Dialog", "Добавить"))
        self.deleteInterval_button.setText(_translate("Dialog", "Удалить"))
        self.clearAllIntervals_button.setText(_translate("Dialog", "Очистить все"))
        self.joinIntervals_groupBox.setTitle(_translate("Dialog", "Склеить интервалы"))
        self.label.setText(_translate("Dialog", "Интервал 1"))
        self.label_2.setText(_translate("Dialog", "Интервал 2"))
        self.joinIntervals_pushButton.setText(_translate("Dialog", "Склеить"))
        self.saveIntervals_button.setText(_translate("Dialog", "Сохранить"))
        self.changeInterval_button.setText(_translate("Dialog", "Изменить"))
        self.addInterval_button.setText(_translate("Dialog", "Добавить"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
