# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_m.ui'
#
# Created: Mon Mar  2 10:39:09 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(658, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 181, 551))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.button_load = QtGui.QPushButton(self.frame)
        self.button_load.setGeometry(QtCore.QRect(10, 230, 151, 27))
        self.button_load.setObjectName(_fromUtf8("button_load"))
        self.button_save = QtGui.QPushButton(self.frame)
        self.button_save.setGeometry(QtCore.QRect(10, 190, 151, 27))
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.button_analyze = QtGui.QPushButton(self.frame)
        self.button_analyze.setGeometry(QtCore.QRect(10, 290, 151, 27))
        self.button_analyze.setObjectName(_fromUtf8("button_analyze"))
        self.button_tune = QtGui.QPushButton(self.frame)
        self.button_tune.setEnabled(False)
        self.button_tune.setGeometry(QtCore.QRect(40, 370, 91, 27))
        self.button_tune.setObjectName(_fromUtf8("button_tune"))
        self.progress_bar = QtGui.QProgressBar(self.frame)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setGeometry(QtCore.QRect(10, 120, 161, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.button_scan = QtGui.QPushButton(self.frame)
        self.button_scan.setGeometry(QtCore.QRect(90, 90, 81, 27))
        self.button_scan.setObjectName(_fromUtf8("button_scan"))
        self.spin_step = QtGui.QSpinBox(self.frame)
        self.spin_step.setGeometry(QtCore.QRect(10, 90, 71, 24))
        self.spin_step.setMinimum(1)
        self.spin_step.setMaximum(32767)
        self.spin_step.setObjectName(_fromUtf8("spin_step"))
        self.spin_stop = QtGui.QSpinBox(self.frame)
        self.spin_stop.setGeometry(QtCore.QRect(97, 40, 71, 24))
        self.spin_stop.setMinimum(1)
        self.spin_stop.setMaximum(32767)
        self.spin_stop.setProperty("value", 32767)
        self.spin_stop.setObjectName(_fromUtf8("spin_stop"))
        self.spin_start = QtGui.QSpinBox(self.frame)
        self.spin_start.setGeometry(QtCore.QRect(10, 40, 71, 24))
        self.spin_start.setMinimum(1)
        self.spin_start.setMaximum(32767)
        self.spin_start.setProperty("value", 1)
        self.spin_start.setObjectName(_fromUtf8("spin_start"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 59, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 41, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.combo_line_select = QtGui.QComboBox(self.frame)
        self.combo_line_select.setEnabled(False)
        self.combo_line_select.setGeometry(QtCore.QRect(10, 340, 151, 22))
        self.combo_line_select.setObjectName(_fromUtf8("combo_line_select"))
        self.text_bar = QtGui.QTextBrowser(self.centralwidget)
        self.text_bar.setGeometry(QtCore.QRect(200, 430, 451, 51))
        self.text_bar.setObjectName(_fromUtf8("text_bar"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 530, 343, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.portsComboBox = QtGui.QComboBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portsComboBox.sizePolicy().hasHeightForWidth())
        self.portsComboBox.setSizePolicy(sizePolicy)
        self.portsComboBox.setMinimumSize(QtCore.QSize(200, 27))
        self.portsComboBox.setObjectName(_fromUtf8("portsComboBox"))
        self.horizontalLayout.addWidget(self.portsComboBox)
        self.refreshPortsPushButton = QtGui.QPushButton(self.layoutWidget)
        self.refreshPortsPushButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshPortsPushButton.sizePolicy().hasHeightForWidth())
        self.refreshPortsPushButton.setSizePolicy(sizePolicy)
        self.refreshPortsPushButton.setMinimumSize(QtCore.QSize(38, 27))
        self.refreshPortsPushButton.setMaximumSize(QtCore.QSize(38, 27))
        self.refreshPortsPushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPortsPushButton.setIcon(icon)
        self.refreshPortsPushButton.setIconSize(QtCore.QSize(16, 16))
        self.refreshPortsPushButton.setObjectName(_fromUtf8("refreshPortsPushButton"))
        self.horizontalLayout.addWidget(self.refreshPortsPushButton)
        self.baudRateComboBox = QtGui.QComboBox(self.layoutWidget)
        self.baudRateComboBox.setMinimumSize(QtCore.QSize(91, 27))
        self.baudRateComboBox.setObjectName(_fromUtf8("baudRateComboBox"))
        self.horizontalLayout.addWidget(self.baudRateComboBox)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 530, 71, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 10, 401, 371))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.plotLayout = QtGui.QVBoxLayout(self.widget)
        self.plotLayout.setMargin(0)
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.plot_view = MatplotlibWidget(self.widget)
        self.plot_view.setObjectName(_fromUtf8("plot_view"))
        self.plotLayout.addWidget(self.plot_view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LaserControl", None))
        self.button_load.setText(_translate("MainWindow", "Load from file", None))
        self.button_save.setText(_translate("MainWindow", "Save to file", None))
        self.button_analyze.setText(_translate("MainWindow", "Analyze", None))
        self.button_tune.setText(_translate("MainWindow", "Tune", None))
        self.button_scan.setText(_translate("MainWindow", "Start scan", None))
        self.label.setText(_translate("MainWindow", "Start", None))
        self.label_2.setText(_translate("MainWindow", "Stop", None))
        self.label_3.setText(_translate("MainWindow", "Step", None))
        self.label_4.setText(_translate("MainWindow", "Serial port:", None))

from first_m_qt4 import MatplotlibWidget
#import mainWindow_rc

