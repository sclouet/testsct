# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPSD.ui'
#
# Created: Wed Aug 19 22:30:10 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(690, 609)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Info = QtGui.QFrame(self.centralwidget)
        self.Info.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Info.setObjectName(_fromUtf8("Info"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Info)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textBrowser = QtGui.QTextBrowser(self.Info)
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 16777215))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.Info)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(150, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 546))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.main_widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.main_widget.setObjectName(_fromUtf8("main_widget"))
        self.verticalLayout.addWidget(self.main_widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_cgns = QtGui.QAction(MainWindow)
        self.actionLoad_cgns.setObjectName(_fromUtf8("actionLoad_cgns"))
        self.actionWrite_vtk = QtGui.QAction(MainWindow)
        self.actionWrite_vtk.setObjectName(_fromUtf8("actionWrite_vtk"))
        self.actionLoad_groups = QtGui.QAction(MainWindow)
        self.actionLoad_groups.setObjectName(_fromUtf8("actionLoad_groups"))
        self.menuFile.addAction(self.actionLoad_cgns)
        self.menuFile.addAction(self.actionLoad_groups)
        self.menuFile.addAction(self.actionWrite_vtk)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">info</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_cgns.setText(QtGui.QApplication.translate("MainWindow", "load cgns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWrite_vtk.setText(QtGui.QApplication.translate("MainWindow", "write vtk", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_groups.setText(QtGui.QApplication.translate("MainWindow", "load groups", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

