import platform
import os
import sys
import vlc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("PyMediaPlayer")
        self.instance = vlc.Instance()
        self.media = None
        self.mediaplayer = self.instance.media_player_new()
        #self.create_ui()
        self.is_paused = False
        self.dpath=''
        self.dirpths=[]
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        if platform.system() == "Darwin":
            self.frame = QtWidgets.QMacCocoaViewContainer(0)
        else:
            self.frame = QtWidgets.QFrame(self.centralwidget)
        self.palette = self.frame.palette()
        self.palette.setColor(QPalette.Window, QtGui.QColor(0, 0, 0))
        self.frame.setPalette(self.palette)
        self.frame.setAutoFillBackground(True)
        #self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)

        self.hsl1 = QtWidgets.QSlider(self.centralwidget)
        self.hsl1.setOrientation(QtCore.Qt.Horizontal)
        self.hsl1.setObjectName("hsl1")
        self.hsl1.setMaximum(1000)
        self.verticalLayout.addWidget(self.hsl1)
        self.hsl1.sliderPressed.connect(self.set_position)
        self.hsl1.sliderMoved.connect(self.set_position)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setMaximumSize(QtCore.QSize(50, 20))
        self.play.setObjectName("play")
        self.horizontalLayout.addWidget(self.play)
        self.play.clicked.connect(self.play_pause)
        
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setMaximumSize(QtCore.QSize(50, 20))
        self.stop.setObjectName("pause")
        self.horizontalLayout.addWidget(self.stop)
        self.stop.clicked.connect(self.stop1)

        self.playlist = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlist.sizePolicy().hasHeightForWidth())
        self.playlist.setSizePolicy(sizePolicy)
        self.playlist.setMinimumSize(QtCore.QSize(0, 0))
        self.playlist.setMaximumSize(QtCore.QSize(50, 20))
        self.playlist.setObjectName("playlist")
        self.horizontalLayout.addWidget(self.playlist)
        self.playlist.clicked.connect(self.shplaylist)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        self.hsl2 = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hsl2.sizePolicy().hasHeightForWidth())
        self.hsl2.setSizePolicy(sizePolicy)
        self.hsl2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.hsl2.setOrientation(QtCore.Qt.Horizontal)
        self.hsl2.setObjectName("hsl2")
        self.hsl2.setMaximum(200)
        self.hsl2.setValue(self.mediaplayer.audio_get_volume())
        self.horizontalLayout.addWidget(self.hsl2)
        self.hsl2.valueChanged.connect(self.set_volume)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionadd_File = QtWidgets.QAction(MainWindow)
        self.actionadd_File.setObjectName("actionadd_File")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionadd_File)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionOpen_File.triggered.connect(self.open_file)
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionClose.triggered.connect(sys.exit)
        self.actionadd_File.triggered.connect(self.addtoplaylist)
        self.listWidget.clicked.connect(self.selectfromplaylist)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer(MainWindow)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_ui)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyMediaPlayer"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.playlist.setText(_translate("MainWindow", "Playlist"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionadd_File.setText(_translate("MainWindow", "Add File to Playlist"))
        self.listWidget.setParent(None)

    def play_pause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.play.setText("Play")
            self.is_paused = True
            self.timer.stop()
        else:
            if self.mediaplayer.play() == -1:
                #self.open_file()
                return

            self.mediaplayer.play()
            self.play.setText("Pause")
            self.timer.start()
            self.is_paused = False

    def stop1(self):
        self.mediaplayer.stop()
        self.play.setText("Play")
        self.hsl1.setValue(int(self.mediaplayer.get_position() * 1000))

    def update_ui(self):
        media_pos = int(self.mediaplayer.get_position() * 1000)
        self.hsl1.setValue(media_pos)

        if not self.mediaplayer.is_playing():
            self.timer.stop()
            if not self.is_paused:
                self.stop1()

    def open_file(self):
        dialog_txt = "Choose Media File"
        filename = QtWidgets.QFileDialog.getOpenFileName(MainWindow, dialog_txt, os.path.expanduser('~'))
        if not filename:
            return
        self.media = self.instance.media_new(filename[0])
        self.mediaplayer.set_media(self.media)
        self.media.parse()
        if platform.system() == "Linux": 
            self.mediaplayer.set_xwindow(int(self.frame.winId()))
        elif platform.system() == "Windows": 
            self.mediaplayer.set_hwnd(int(self.frame.winId()))
        elif platform.system() == "Darwin":
            self.mediaplayer.set_nsobject(int(self.frame.winId()))
        self.play_pause()

    def open_folder(self):
        self.dpath = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.getmedia()

    def getmedia(self):
        filess=[]
        dirpthss=[]
        for dirpath,dirs,files in os.walk(self.dpath):
            filess.append(files)
            dirpthss.append(dirpath)

        for files in filess:
            for file in files:
                if os.path.splitext(file)[-1] in ['.mp3','.mp4','.mkv','.avi']:
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
        self.statusbar.showMessage(f"{len(self.dirpths)} Media files in Playlist.")
        self.hsl2.setValue(self.mediaplayer.audio_get_volume())

    def set_volume(self, volume):
        self.mediaplayer.audio_set_volume(volume)

    def set_position(self):
        self.timer.stop()
        pos = self.hsl1.value()
        self.mediaplayer.set_position(pos / 1000.0)
        self.timer.start()

    def shplaylist(self):
        if self.horizontalLayout_2.count() == 1 :
            self.horizontalLayout_2.addWidget(self.listWidget)
        else:
            self.listWidget.setParent(None)

    def selectfromplaylist(self):
        item1=self.listWidget.currentItem().text()
        self.media = self.instance.media_new(item1)
        self.mediaplayer.set_media(self.media)
        self.media.parse()
        if platform.system() == "Linux": 
            self.mediaplayer.set_xwindow(int(self.frame.winId()))
        elif platform.system() == "Windows": 
            self.mediaplayer.set_hwnd(int(self.frame.winId()))
        elif platform.system() == "Darwin":
            self.mediaplayer.set_nsobject(int(self.frame.winId()))
        self.play_pause()

    def addtoplaylist(self):
        dialog_txt = "Choose Media File"
        filename = QtWidgets.QFileDialog.getOpenFileName(MainWindow, dialog_txt, os.path.expanduser('~'))
        if not filename:
            return
        if str(filename[0]) not in self.dirpths:
            self.dirpths.append(str(filename[0]))
        
    

if __name__ == "__main__":
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
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
