from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def show():
    print(check.text())
    print(check.checkState())
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
 
check = QtWidgets.QCheckBox(win)
check.setText("Option1")
check.stateChanged.connect(show)
check.move(50,100)
 
win.show()
sys.exit(app.exec_())