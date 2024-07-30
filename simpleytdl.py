from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import * #QApplication, QWidget #QMainWindow
import sys
import webbrowser
import platform
import os
import pathlib
#import subprocess
#from contextlib import redirect_stdout

def window():

    def checkOS():
        #textfield.append(str(platform.architecture()))
        #textfield.append(str(platform.python_version()))
        #textfield.append(str(platform.uname()))
        myOS = platform.uname()
        system, node, release, version, machine, cpu = myOS
        #textfield.append("Betriebssystem...:  " + system)
        #textfield.append("Gerätename.......:  " + node)
        #textfield.append("Release............:  " + release)
        #textfield.append("Version.............:  " + version)
        #textfield.append("Maschine...........:  " + machine)
        #textfield.append("CPU.................:  " + cpu)

        global downloadFolder
        
        #  https://stackoverflow.com/a/48706260
        """Returns the default downloads path for linux or windows"""
        if system == 'Windows':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            #return location
            downloadFolder = location
        else:
            #return os.path.join(os.path.expanduser('~'), 'Downloads')
            downloadFolder = os.path.join(os.path.expanduser('~'), 'Downloads')

        return system

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

        newFileName = ""
        audio = ""
        dlPath = ""
        

        if myOS == "Windows":
            if newName.text() != "":
                newFileName = " -o "+ str(downloadPath.text()) + "\\" + str(newName.text()) + str(fileEnding.text())
            else:
                newFileName = ""

            if audioOnly.checkState() == 2:
                audio = " -x --audio-format mp3"
            else:\
                audio = ""

            textfield.setText(str(pathlib.Path().resolve()) + "\\youtube-dl.exe " + youtubeLink.text() + newFileName + audio)

        if myOS == "Linux":
            if newName.text() != "":
                newFileName = " -o "+ str(downloadPath.text()) + "/" + str(newName.text()) + str(fileEnding.text())
            else:
                newFileName = ""

            if audioOnly.checkState() == 2:
                audio = " -x --audio-format mp3"
            else:\
                audio = ""

            textfield.setText(str(pathlib.Path().resolve()) + "/youtube-dl " + youtubeLink.text() + newFileName + audio)

        #C:\Users\ea-da\Documents\GitHub\SimpleYouTubeDownloader\settings.cfg
        #C:\Users\ea-da\Desktop\youtube-dl\youtube-dl.exe
        #-o
        #-x --audio-format mp3

        

        """
        if myOS == "Windows":
            textfield.setText("")
            
            process.setArguments(youtubeLink.text())

            process.start()
            textfield.append(process.readAllStandardOutput().data().decode())
            process.kill()

            textfield.append("Download abgeschlossen")
        else:
            print("")
        """


    # initialize the Application
    app = QApplication(sys.argv)
    # Creating the Window
    win = QWidget()

    WIDTH = 600
    HEIGHT = 270
    icon = QtGui.QIcon('ytdl-logo.png')
    myOS = checkOS()

    ##### A P P - W I N D O W ################################################################################################

    win.setGeometry(400,400,WIDTH,HEIGHT)
    win.setFixedSize(WIDTH, HEIGHT)
    win.setWindowTitle("Simple YouTube-Downloader (" + checkOS() + ")")
    win.setWindowIcon(icon)

    tray = QSystemTrayIcon()
    tray.setIcon(icon) 
    tray.setVisible(True) 

    ##### P R O C E S S ######################################################################################################

    process = QtCore.QProcess(win)
    process.setProgram("youtube-dl.exe")
    process.setProcessChannelMode(QtCore.QProcess.MergedChannels)

    ##### L A B E L ##########################################################################################################

    labelYTLink = QtWidgets.QLabel(win)
    labelYTLink.setText("YouTube-Link")
    labelYTLink.adjustSize()
    labelYTLink.move(20,25)

    labelDownloadPath = QtWidgets.QLabel(win)
    labelDownloadPath.setText("Download")
    labelDownloadPath.adjustSize()
    labelDownloadPath.move(20,50)

    labelNewName = QtWidgets.QLabel(win)
    labelNewName.setText("Dateiname")
    labelNewName.adjustSize()
    labelNewName.move(20,75)

    ##### T E X T B O X #######################################################################################################

    youtubeLink = QtWidgets.QLineEdit(win)
    youtubeLink.setFixedWidth(400)
    youtubeLink.move(100,20)
    youtubeLink.setText("https://www.youtube.com/watch?v=dLHyoiHg-1M")

    downloadPath = QtWidgets.QLineEdit(win)
    downloadPath.setFixedWidth(400)
    downloadPath.move(100,45)
    downloadPath.setText(downloadFolder)

    newName = QtWidgets.QLineEdit(win)
    newName.setFixedWidth(320)
    newName.move(100,70)

    fileEnding = QtWidgets.QLineEdit(win)
    fileEnding.setFixedWidth(80)
    fileEnding.move(420,70)
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
    audioOnly.move(100,95)
    audioOnly.stateChanged.connect(checkBoxCheck)

    ##### E D I T #######################################################################################################

    textfield = QtWidgets.QTextEdit(win)
    textfield.setPlaceholderText("")
    #textfield.font()
    #textfield.setFont(QtGui.QFont.StyleHint.Courier)
    textfield.setFixedSize(400,100)
    textfield.move(100,130)
    textfield.setReadOnly(1)

    # Show the Window
    win.show()
    sys.exit(app.exec_())

window()