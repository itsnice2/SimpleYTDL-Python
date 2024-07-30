from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import * #QApplication, QWidget #QMainWindow
import sys
import webbrowser

#import pathlib
#import subprocess
#from contextlib import redirect_stdout

#C:\Users\ea-da\Documents\GitHub\SimpleYouTubeDownloader\settings.cfg
#C:\Users\ea-da\Desktop\youtube-dl\youtube-dl.exe
#-o
#-x --audio-format mp3

def window():

    def checkOS():
        print("Hallo")

    def openYTDLGit():
        webbrowser.open('https://github.com/ytdl-org/ytdl-nightly/releases/')

    def openYTDL():
        webbrowser.open('https://github.com/itsnice2/SimpleYTDL-Python')

    def checkBoxCheck():
        if audioOnly.checkState() == 2:
            fileEnding.setText(".mp3")
        else:
            fileEnding.setText(".mp4")

    @QtCore.pyqtSlot()
    def downloadVideo():
        textfield.setText("")
        #textfield.setText(textfield.toPlainText() + "Hello there ")
        #with redirect_stdout(textfield) as f:
        #myYTDLPath = pathlib.Path().resolve() + "\\youtube-dl.exe"
        
        process.setArguments(youtubeLink.text())
        #process.setArguments(str(youtubeLink.text()))

        process.start()
        textfield.append(process.readAllStandardOutput().data().decode())
        process.kill()

        #textfield.setText( myYTDLPath + " " + youtubeLink.text())
        #subprocess.run([myYTDLPath, youtubeLink.text()])
        textfield.append("Download abgeschlossen") 


    # initialize the Application
    app = QApplication(sys.argv)
    # Creating the Window
    win = QWidget()

    WIDTH = 600
    HEIGHT = 270

    ##### A P P - W I N D O W ################################################################################################

    win.setGeometry(400,400,WIDTH,HEIGHT)
    win.setFixedSize(WIDTH, HEIGHT)
    win.setWindowTitle("Simple YouTube-Downloader")
    win.setWindowIcon(QtGui.QIcon('ytdl-logo.png'))

    ##### P R O C E S S ######################################################################################################

    process = QtCore.QProcess(win)
    process.setProgram("youtube-dl.exe")
    process.setProcessChannelMode(QtCore.QProcess.MergedChannels)

    ##### L A B E L ##########################################################################################################

    labelYTLink = QtWidgets.QLabel(win)
    labelYTLink.setText("YouTube-Link")
    labelYTLink.adjustSize()
    labelYTLink.move(20,30)

    labelNewName = QtWidgets.QLabel(win)
    labelNewName.setText("Dateiname")
    labelNewName.adjustSize()
    labelNewName.move(20,70)

    ##### T E X T B O X #######################################################################################################

    youtubeLink = QtWidgets.QLineEdit(win)
    youtubeLink.setFixedWidth(400)
    youtubeLink.move(100,20)
    youtubeLink.setText("https://www.youtube.com/watch?v=dLHyoiHg-1M")

    newName = QtWidgets.QLineEdit(win)
    newName.setFixedWidth(320)
    newName.move(100,60)

    fileEnding = QtWidgets.QLineEdit(win)
    fileEnding.setFixedWidth(80)
    fileEnding.move(420,60)
    fileEnding.setText(".mp4")
    fileEnding.setEnabled(False)


    ##### B U T T O N S #######################################################################################################

    button = QtWidgets.QPushButton(win)
    button.setText("Download")
    button.clicked.connect(downloadVideo)
    button.move(510,20)

    button_exit = QtWidgets.QPushButton(win)
    button_exit.setText("Beenden")
    button_exit.clicked.connect(win.close)
    button_exit.move(WIDTH - 90,HEIGHT - 60)

    button_ytdl_git = QtWidgets.QPushButton(win)
    button_ytdl_git.setText("youtube-dl\nherunterladen")
    button_ytdl_git.clicked.connect(openYTDLGit)
    button_ytdl_git.move(20, 130)

    button_ytdl = QtWidgets.QPushButton(win)
    button_ytdl.setText("SimpleYTDL\nbesuchen")
    button_ytdl.clicked.connect(openYTDL)
    button_ytdl.move(20, 190)

    ##### C H E C K B O X #######################################################################################################

    audioOnly = QtWidgets.QCheckBox(win)
    audioOnly.setText("Nur Audio")
    audioOnly.move(100,85)
    audioOnly.stateChanged.connect(checkBoxCheck)

    ##### E D I T #######################################################################################################

    textfield = QtWidgets.QTextEdit(win)
    textfield.setPlaceholderText("")
    textfield.setFixedSize(400,100)
    textfield.move(100,130)
    textfield.setReadOnly(1)


    # Show the Window
    win.show()
    sys.exit(app.exec_())

window()