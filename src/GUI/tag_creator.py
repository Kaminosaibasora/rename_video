import sys

sys.path.append('./engine')
import readwriter as rw
from renamegine import Renamegine

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QComboBox, QGridLayout, QLineEdit, QCheckBox, QLabel

class Tag_creator(QWidget):
    def __init__(self, rengine):
        QWidget.__init__(self)
        # --------- Data ---------
        self.currenttheme = "Test"
        self.tags = []
        # ------- Widgets -------
        # Theme
        self.theme = QComboBox()
        self.theme.addItems(self.loadtheme())
        self.theme.currentTextChanged.connect( self.changed_theme )
        self.champtheme = QLineEdit()
        self.champthemevalide = QPushButton("Ajouter le theme")
        self.champthemevalide.clicked.connect(self.addtheme)
        # tag
        self.checktagSolo   = QCheckBox()
        self.checktagDuo    = QCheckBox()
        self.checktagTrio   = QCheckBox()
        self.checktagGroup  = QCheckBox()
        self.checktagMember = QCheckBox()
        self.checktagObject = QCheckBox()
        self.checktagSolo   .setText("solo")
        self.checktagDuo    .setText("duo")
        self.checktagTrio   .setText("trio")
        self.checktagGroup  .setText("group")
        self.checktagMember .setText("member")
        self.checktagObject .setText("object")
        self.checktagSolo   .stateChanged.connect(self.show_state)
        self.checktagDuo    .stateChanged.connect(self.show_state)
        self.checktagTrio   .stateChanged.connect(self.show_state)
        self.checktagGroup  .stateChanged.connect(self.show_state)
        self.checktagMember .stateChanged.connect(self.show_state)
        self.checktagObject .stateChanged.connect(self.show_state)
        # Validation
        self.label = QLabel()
        self.label.setText("Choisissez vos tags")
        self.saveButton = QPushButton("Enregistrer les modifications")
        # self.saveButton.clicked.connect(self.validation_name)

        layout = QGridLayout()

        layout.addWidget(self.theme,        0, 3)
        layout.addWidget(self.champtheme,   1, 3)
        layout.addWidget(self.champthemevalide,2, 3)

        layout.addWidget(self.checktagSolo, 0, 1)
        layout.addWidget(self.checktagDuo,  1, 1)
        layout.addWidget(self.checktagTrio, 2, 1)

        layout.addWidget(self.checktagGroup,0, 2)
        layout.addWidget(self.checktagMember,1, 2)
        layout.addWidget(self.checktagObject,2, 2)

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.saveButton, 1, 0)

        self.setLayout(layout)

    
    def addtheme(self):
        if (len(self.champtheme.text()) != 0) :
            self.theme.addItem(
                self.champtheme.text()
            )
            themeslist = []
            for th in self.loadtheme() + [self.champtheme.text()] :
                themeslist += [th + "\n"]
            rw.writeListtoTXT(
                './GUI/themes.txt',
                themeslist
            )
            self.champtheme.setText("")
    
    def loadtheme(self):
        themelist = []
        for theme in rw.readTXTtoList('./GUI/themes.txt'):
            themelist += [theme.replace('\n', '')]
        return themelist
    
    def changed_theme(self, theme):
        print(theme)
        self.currenttheme = theme
    
    def show_state(self, s):
        # print(s == Qt.Checked)
        # print(s)
        checkwid = [
            self.checktagSolo,
            self.checktagDuo,
            self.checktagTrio,
            self.checktagGroup,
            self.checktagMember,
            self.checktagObject,
        ]
        for check in checkwid :
            if s == Qt.Checked and check.isChecked() :
                if check.text() not in self.tags :
                    self.tags += [check.text()]
            elif s != Qt.Checked and not check.isChecked() :
                if check.text() in self.tags :
                    self.tags.remove(check.text())
        print(self.tags)
        self.label.setText(str(self.tags))
            