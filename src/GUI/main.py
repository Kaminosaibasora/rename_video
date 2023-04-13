import sys
sys.path.append('./engine')
from renamegine import Renamegine

from PyQt5.QtWidgets import QApplication

from GUI import GUI

rengine = Renamegine()

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

fen = GUI(rengine)
fen.show()

app.exec_()