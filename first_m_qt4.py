#!/usr/bin/python
# -*- coding: utf8 -*-


import sys, serial, glob
from PyQt4 import QtGui, QtCore
#from PyQt5 import QtCore, QtGui, QtWidgets
#import matplotlib
#matplotlib.use("Qt5Agg")
import numpy as np
#from pylab import *

import matplotlib
matplotlib.use("Qt4Agg")

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

# import klasy
from first_m_qt4_ui import Ui_MainWindow

class Pomiar():    
    
    def __init__(self):
        self.xx=np.array([])
        self.yy=np.array([])
        
    def scan_init(self):
        self.xx=np.array([])
        self.yy=np.array([])
        self.scan_active=1
    
    def moving_average(self,a, n=3) :
        return np.convolve(a,np.ones((n,))/n, 'same')
    
    
    
    def remove_trend(self):
        dim=2
        self.arr=np.polyfit(self.xx,self.yy,dim,cov=False)
        self.pol=np.poly1d(self.arr)
        self.yy=self.yy-self.pol(self.xx)
        self.yy=self.moving_average(self.yy,n=7)
        
    def find_peaks(self):
        from detect_peaks_m import detect_peaks
        self.ind = detect_peaks(self.xx,self.yy, mph=30, mpd=50,threshold=0, valley=True, show=True)
        #self.ind=self.xx[self.ind]
        return self.ind

    
    def load_file(self,filename):
        self.data = np.loadtxt(filename)
        self.xx,self.yy=self.data[:,0],self.data[:,1]
    
    def save_file(self,filename):
        np.savetxt(filename, np.c_[self.xx,self.yy], fmt='%.2f')
    
    def read_oneline(self,i):
        return str(self.xx[i])+str(self.yy[i])
    
    def update_plot(self,widget):
        widget.plotDataPoints(self.xx,self.yy) 

class MainQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        
        
        QtGui.QWidget.__init__(self, parent)
        # nazwa klasy
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.navi_toolbar = NavigationToolbar(self.ui.plot_view.canvas, self)
        self.ui.plotLayout.addWidget(self.navi_toolbar)
        
        # tutaj dajemy wlasne polaczenia slotow
        self.ui.button_scan.clicked.connect( self.scan)
        self.ui.button_load.clicked.connect(self.file_load)
        self.ui.button_save.clicked.connect(self.file_save)
        self.ui.button_analyze.clicked.connect(self.analyze)
        
        self.ui.refreshPortsPushButton.clicked.connect(self.refreshPorts)
      
        self.setup_serial_Ui()
        
        self.pomiar=Pomiar()
        
    def foo(self):
        self.ui.statusbar.showMessage('Nacisłeś guzik!',2000)
        
    def scan(self):
        self.connect()
        self.commtxt=""
        txt="s %d %d %d\n"% (self.ui.spin_start.value(), self.ui.spin_stop.value(), self.ui.spin_step.value())
        self.ui.text_bar.setText("$Command: " + txt)                     
        self.writer.start(self.ser, txt)
        
    def file_load(self):
      
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        print (self.filename)
        from os.path import isfile
        if isfile(self.filename):
            self.pomiar.load_file(self.filename)
            self.pomiar.update_plot(self.ui.plot_view)
            #self.ui.text_bar.setText(self.pomiar.read_oneline(0))
    
    def file_save(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getSaveFileName()
        #self.pomiar.save_file(self.filename)
        with open( self.filename, "w") as text_file:
            print(format(self.commtxt), file=text_file)
            
    def analyze(self):
        self.pomiar.remove_trend()
        self.peaks=self.pomiar.find_peaks()
        self.peaks_s=["%.0f" % num for num in self.peaks]
        self.ui.text_bar.setText("Found peaks: "+" ".join(self.peaks_s))
        self.ui.combo_line_select.addItems(self.peaks_s)
        self.ui.combo_line_select.setEnabled(True)
        self.ui.button_tune.setEnabled(True)
        self.ui.button_tune.clicked.connect(self.tune)
        
    def tune(self):
        self.connect()
        txt=self.ui.combo_line_select.currentText()
        self.ui.text_bar.setText("Current set: "+txt)
        self.writer.start(self.ser, "i "+txt+"\n")
        self.disconnect()
        
    
    def setup_serial_Ui(self):
        
        baudRates = ['38400','9600','19200','115200','1200000',]
        self.ser = None
        self.reader = CReader()
        self.writer = CWriter()
        
        self.ui.baudRateComboBox.addItems(baudRates)
        self.refreshPorts()
        QtCore.QObject.connect(self.ui.refreshPortsPushButton, QtCore.SIGNAL("clicked()"), self.refreshPorts)
        QtCore.QObject.connect(self.reader, QtCore.SIGNAL("newData(QString)"), self.updateLog)
        QtCore.QObject.connect(self.reader, QtCore.SIGNAL("error(QString)"), self.printError)
        QtCore.QObject.connect(self.writer, QtCore.SIGNAL("error(QString)"), self.printError)    
    
    def getUSBPorts(self):
        return glob.glob("/dev/ttyUSB*")

    def getSPPorts(self):
        return glob.glob("/dev/ttyS*")

    def getSelectedPort(self):
        return self.ui.portsComboBox.currentText()

    def getSelectedBaudRate(self):
        return self.ui.baudRateComboBox.currentText()

    def refreshPorts(self):
        self.ui.portsComboBox.clear()
        self.ui.portsComboBox.addItems(sorted(self.getUSBPorts()))
        self.ui.portsComboBox.addItems(sorted(self.getSPPorts()))

    def connect(self):
        self.disconnect()
        try:
            self.printInfo("Connecting to %s with %s baud rate." % \
                            (self.getSelectedPort(), self.getSelectedBaudRate()))
            self.ser = serial.Serial(str(self.getSelectedPort()), \
                                    int(self.getSelectedBaudRate()))
            self.startReader(self.ser)
            self.printInfo("Connected successfully.")
        except:
            self.ser = None
            self.printError("Failed to connect!")

    def disconnect(self):
        self.stopThreads()
        if self.ser == None: return
        try:
            if self.ser.isOpen:
                self.ser.close()
                self.printInfo("Disconnected successfully.")
        except:
            self.printError("Failed to disconnect!")
        self.ser = None

    def startReader(self, ser):
        self.reader.start(ser)

    def stopThreads(self):
        self.stopReader()
        self.stopWriter()
        
    def stopReader(self):
        if self.reader.isRunning():
            self.reader.terminate()

    def stopWriter(self):
        if self.writer.isRunning():
            self.writer.terminate()

    def printInfo(self, text):
        self.ui.statusbar.showMessage(text,2000)

    def printError(self, text):
        self.ui.statusbar.showMessage(text,2000)
        
    def updateLog(self, text):
        #self.ui.text_bar.moveCursor(QTextCursor.End)
        self.ui.text_bar.insertPlainText(text)
        self.commtxt+=text
        #self.ui.text_bar.moveCursor(QTextCursor.End)
        

    def processCmd(self,cmd):
        self.writer.start(self.ser, cmd+"\n")

    def closeEvent(self, event):
        self.disconnect()


class CReader(QtCore.QThread):
    def start(self, ser, priority = QtCore.QThread.InheritPriority):
        self.ser = ser
        QtCore.QThread.start(self, priority)
    
    def run(self):
        while True:
            try:
                data = self.ser.read(1)
                n = self.ser.inWaiting()
                if n:
                    data = data + self.ser.read(n)
                self.emit(QtCore.SIGNAL("newData(QString)"),data.decode('ascii') )
            except:
                errMsg = "Reader thread is terminated unexpectedly."
                self.emit(QtCore.SIGNAL("error(QString)"), errMsg)
                raise
                break

class CWriter(QtCore.QThread):
    def start(self, ser, cmd = "", priority = QtCore.QThread.InheritPriority):
        self.ser = ser
        self.cmd = cmd
        QtCore.QThread.start(self, priority)
    
    def run(self):
        try:
            self.ser.write(str(self.cmd).encode())
        except:
            errMsg = "Writer thread is terminated unexpectedly."
            self.emit(QtCore.SIGNAL("error(QString)"), errMsg)
            raise
        

class MatplotlibWidget(Canvas):        
    def __init__(self, parent=None, title='Current scan', xlabel='[num]', ylabel='[abs]', dpi=100, hold=False):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.canvas = Canvas(self.figure)
        #self.canvas.mpl_connect('pick_event', self.on_pick)
        self.axes = self.figure.add_subplot(111)
        #self.mpl_toolbar = NavigationToolbar(self.canvas, self)
        #self.mpl_toolbar.hide()

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)

    def plotDataPoints(self, x, y):
        self.axes.plot(x,y)
        self.draw() 
    
    def on_pick(self,event):
        box_points = event.artist.get_bbox().get_points()
        msg = "You've clicked on a bar with coords:\n %s" % box_points
        QMessageBox.information(self, "Click!", msg)
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainQT4()
    myapp.show()
    sys.exit(app.exec_()) 
