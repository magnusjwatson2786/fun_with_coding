from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QStatusBar
import os



class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.dpath=''
        self.dirpths=[]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 804)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bprev = QtWidgets.QPushButton(self.centralwidget)
        self.bprev.setMaximumSize(QtCore.QSize(25, 75))
        self.bprev.setObjectName("bprev")
        self.horizontalLayout.addWidget(self.bprev)
        self.sca2 = QtWidgets.QScrollArea(self.centralwidget)
        self.sca2.setMinimumSize(QtCore.QSize(640, 480))
        self.sca2.setWidgetResizable(True)
        self.sca2.setObjectName("sca2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 795, 478))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imgcont = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.imgcont.setText("")
        self.imgcont.setObjectName("imgcont")
        self.gridLayout_2.addWidget(self.imgcont, 0, 0, 1, 1)
        self.sca2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.sca2)
        self.bnext = QtWidgets.QPushButton(self.centralwidget)
        self.bnext.setMaximumSize(QtCore.QSize(25, 75))
        self.bnext.setObjectName("bnext")
        self.horizontalLayout.addWidget(self.bnext)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.dtshow = QtWidgets.QPushButton(self.centralwidget)
        self.dtshow.setObjectName("dtshow")
        self.verticalLayout.addWidget(self.dtshow)
        self.dtshow.setHidden(True)
        self.sca1 = QtWidgets.QScrollArea(self.centralwidget)
        self.sca1.setWidgetResizable(True)
        self.sca1.setObjectName("sca1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 859, 226))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.sca1.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.sca1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.a_OF = QtWidgets.QAction(MainWindow)
        self.a_OF.setObjectName("a_OF")
        self.menuFile.addAction(self.a_OF)
        self.menubar.addAction(self.menuFile.menuAction())
        self.a_OF.triggered.connect(self.fetchfolder)
        self.listWidget.clicked.connect(self.listItemclicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyImgViewer"))
        self.bprev.setText(_translate("MainWindow", "⫷"))
        self.bnext.setText(_translate("MainWindow", "⫸"))
        self.dtshow.setText(_translate("MainWindow", "⨹⩒"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.a_OF.setText(_translate("MainWindow", "Open Folder"))
        self.a_OF.setShortcut(_translate("MainWindow", "Ctrl+O"))

    def fetchfolder(self):
        self.dpath = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.getimgs()

    def getimgs(self):
        filess=[]
        dirpthss=[]
        for dirpath,dirs,files in os.walk(self.dpath):
            filess.append(files)
            dirpthss.append(dirpath)

        for files in filess:
            for file in files:
                if os.path.splitext(file)[-1] in ['.jpg','.jpeg','.png']:
                    self.dirpths.append(str(os.path.join(dirpthss[filess.index(files)], file)))
        self.fillists(self.listWidget)
        

    def fillists(self,a):
        i=0
        _translate = QtCore.QCoreApplication.translate
        for dirs in self.dirpths:
            item = QtWidgets.QListWidgetItem()
            a.addItem(item)
            item = a.item(i)
            item.setText(_translate("MainWindow", str(dirs)))
            i+=1
        self.statusbar.showMessage(f"{len(self.dirpths)} images found.")

    def listItemclicked(self):
        item1=self.listWidget.currentItem().text()
        self.imgcont.setPixmap(QtGui.QPixmap(item1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(255,255,255))
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(255,255,255))
    dark_palette.setColor(QPalette.ToolTipText, QColor(255,255,255))
    dark_palette.setColor(QPalette.Text, QColor(255,255,255))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QColor(255,255,255))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(142,45,197).lighter())
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
