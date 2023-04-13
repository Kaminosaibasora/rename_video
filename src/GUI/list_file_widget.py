import sys

sys.path.append('./engine')
from renamegine import Renamegine

from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QFileDialog, QLabel, QVBoxLayout, QWidget, QListWidget, QListWidgetItem

class List_file_widget(QWidget):
    def __init__(self, rengine):
        QWidget.__init__(self)
        self.rengine = rengine

        self.labelchoose = QLabel()

        self.choosebutton = QPushButton("choose folder")
        self.choosebutton.clicked.connect(self.choosefolder)
        self.folderpath = ""

        self.listwidget = QListWidget(self)
        # self.listwidget.clicked.connect(self.clicklist)
        self.filechoose = ""
        self.linecurrent = None

        layout = QVBoxLayout()
        layout.addWidget(self.labelchoose)
        layout.addWidget(self.choosebutton)
        layout.addWidget(self.listwidget)

        self.setLayout(layout)
        # self.resize(100, 480)
        self.setFixedWidth(200)



    def choosefolder(self):
        try :
            valid = False
            while not valid :
                try :
                    folderPath = QFileDialog.getExistingDirectory(self, "Choose Folder")
                    valid = True
                    self.folderpath = folderPath
                except Exception as e :
                    print(e)
            self.rengine.list_video_folder(self.folderpath)
            for f in self.rengine.listpath :
                self.listwidget.addItem(
                    QListWidgetItem(f)
                )
        except Exception as e :
            print(e)
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Error :"+e)
            error.setWindowTitle("Erreur de validation")
    
    def clicklist(self, test):
        print(test.data())
        self.filechoose = test.data()
        self.labelchoose.setText(test.data())
    
    def updateList(self):
        self.labelchoose.setText("")
        self.listwidget.removeItemWidget(
            self.listwidget.takeItem(self.listwidget.currentRow())
        )
        self.listwidget.repaint()
        self.linecurrent = None