import sys

sys.path.append('./engine')
from renamegine import Renamegine

from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QMessageBox, QAction, QFileDialog
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QIcon

from video_player_widget import Video_player_widget
from list_file_widget import List_file_widget
from tag_creator import Tag_creator

class GUI(QMainWindow):
    def __init__(self, rengine, parent=None):
        super(GUI, self).__init__(parent)
        # QWidget.__init__(self)
        self.setWindowTitle("Video Rename Tag")

        self.rengine = rengine

        # LIST FILE
        self.listwidget = List_file_widget(self.rengine)
        self.listwidget.listwidget.clicked.connect(self.clickchoosepath)
        # VIDEO PLAYER
        self.video = Video_player_widget(self.rengine)
        # TAG CREATOR
        self.tag_creat = Tag_creator(self.rengine)
        self.tag_creat.saveButton.clicked.connect(self.validation_name)
        self.tag_creat.saveButton.setShortcut('Return')

        # MENU

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open and Cut video', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.open_detect_cut)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Fonction')
        fileMenu.addAction(openAction)

        # LAYOUT
        layout = QGridLayout()

        layout.addWidget(self.listwidget,   0, 0)
        layout.addWidget(self.video,        0, 1, 2, 3)
        layout.addWidget(self.tag_creat,    2, 0, 3, 4)


        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)
        # self.resize(1920, 1080)
        self.resize(1000, 500)


    # def mousePressEvent(self, event):
    #     print("appui souris")
    #     print("position = " + str(event.x()) + " " + str(event.y()))

    def validation_name(self):
        try :
            self.rengine.rename_current_file(
                self.tag_creat.currenttheme,
                self.tag_creat.tags,
                delete = True
            )
            # print(self.rengine.listpath)
            self.listwidget.updateList()
        except Exception as e :
            print(e)
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Error :"+e)
            error.setWindowTitle("Erreur de validation")
    
    def clickchoosepath(self, line):
        print(line.data())
        self.rengine.choose_current_file(line.data())
        self.listwidget.labelchoose.setText(line.data())
        self.video.loadMedia(self.rengine.get_current_path())
        self.video.play()
        self.listwidget.linecurrent = line
    
    def open_detect_cut(self):
        try :
            fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())
            # print(fileName)
            self.rengine.cutdetect(fileName)
            self.listwidget.maj_list_files()
            valid = QMessageBox()
            valid.setIcon(QMessageBox.Information)
            valid.setText("cut réalisé avec succès !")
            valid.setWindowTitle("Success")
            valid.exec()
        except Exception as e :
            print(e)
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Error :"+e)
            error.setWindowTitle("Erreur")
            error.exec()


