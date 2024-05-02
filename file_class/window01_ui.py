# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window01.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1017, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.w_queue = QWidget(self.centralwidget)
        self.w_queue.setObjectName(u"w_queue")
        self.w_queue.setGeometry(QRect(10, 50, 1001, 181))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 10, 481, 20))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(760, 240, 251, 20))
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 240, 231, 20))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.b_openParkingLot = QPushButton(self.centralwidget)
        self.b_openParkingLot.setObjectName(u"b_openParkingLot")
        self.b_openParkingLot.setGeometry(QRect(330, 480, 171, 24))
        self.i_inputExitFrecuency = QLineEdit(self.centralwidget)
        self.i_inputExitFrecuency.setObjectName(u"i_inputExitFrecuency")
        self.i_inputExitFrecuency.setGeometry(QRect(140, 350, 101, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 290, 121, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 340, 91, 51))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_5.setFont(font2)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.l_showExitFrecuency = QLabel(self.centralwidget)
        self.l_showExitFrecuency.setObjectName(u"l_showExitFrecuency")
        self.l_showExitFrecuency.setGeometry(QRect(160, 290, 101, 20))
        self.b_updateExit = QPushButton(self.centralwidget)
        self.b_updateExit.setObjectName(u"b_updateExit")
        self.b_updateExit.setGeometry(QRect(70, 400, 111, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(750, 300, 121, 16))
        self.l_showEntryFrecuency = QLabel(self.centralwidget)
        self.l_showEntryFrecuency.setObjectName(u"l_showEntryFrecuency")
        self.l_showEntryFrecuency.setGeometry(QRect(890, 300, 101, 20))
        self.b_updateEntry = QPushButton(self.centralwidget)
        self.b_updateEntry.setObjectName(u"b_updateEntry")
        self.b_updateEntry.setGeometry(QRect(800, 410, 111, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(750, 350, 111, 51))
        self.label_9.setFont(font2)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.i_inputEntryFrecuency = QLineEdit(self.centralwidget)
        self.i_inputEntryFrecuency.setObjectName(u"i_inputEntryFrecuency")
        self.i_inputEntryFrecuency.setGeometry(QRect(870, 360, 101, 31))
        self.b_closeParkingLot = QPushButton(self.centralwidget)
        self.b_closeParkingLot.setObjectName(u"b_closeParkingLot")
        self.b_closeParkingLot.setGeometry(QRect(520, 480, 171, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1017, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"E S T A C I O N A M I E N T O", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Entrada de Autos", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Salida de Autos", None))
        self.b_openParkingLot.setText(QCoreApplication.translate("MainWindow", u"Abrir Estacionamiento", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Frecuencia Actual:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Actualizar Frecuencia: (Seg)", None))
        self.l_showExitFrecuency.setText(QCoreApplication.translate("MainWindow", u"xxxx segundo", None))
        self.b_updateExit.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frecuencia Actual:", None))
        self.l_showEntryFrecuency.setText(QCoreApplication.translate("MainWindow", u"xxxx segundo", None))
        self.b_updateEntry.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Actualizar Frecuencia: (Seg)", None))
        self.b_closeParkingLot.setText(QCoreApplication.translate("MainWindow", u"Cerrar Estacionamiento", None))
    # retranslateUi

