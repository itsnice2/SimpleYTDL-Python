# Simple YouTube-Downloader (Python) für Linux und Windows
Ein kleines Pythonprogramm, das eigentlich nur eine GUI für youtube-dl ist. Es schöpft nicht die vollen Möglichkeiten von youtube-dl aus. Das Ziel sollte sein, ein ganz simples Programm zu schreiben.

## Vorraussetzungen
- Python 3
- youtube-dl
- FFMPEG

### Python-Installation (Windows)
Hier runterladen und installieren:
```
https://www.python.org/downloads/
```
Danach noch mit pip pyqt5 installieren. Dafür die Kommandozeile öffnen und diesen Befehl eintippen:
```
pip install pyqt5
```

### Python-Installation (Linux)
Auf der Konsole folgenden Befehl ausführen:
```
sudo apt install python3
```
Falls Sie keine virtuelle Umgebung nutzen, noch so pyqt5 installieren:
```
python3 -m pip install pyqt5
```

### FFMPEG-Installation
Dies wird gebraucht um das Video in eine MP3 umzuwandeln.
Unter Linux ganz einfach mit
```
sudo apt install ffmpeg
```
Für Windows diese Seite besuchen:
```
https://www.gyan.dev/ffmpeg/builds
```
Unter **release builds**
```
ffmpeg-release-full.7z
```
herunterladen und die Datei danach entpacken. Den Ordner dann am besten nach **ffmpeg** umbennen, und nach **c:** verschieben. Dann die Kommandozeile als Administrator öffnen, und
```
setx /m PATH "C:\ffmpeg\bin;%PATH%"
```
eintippen und ENTER drücken. Fertig.
Bei Problemen hilft diese Anleitung: https://www.wikihow.com/Install-FFmpeg-on-Windows

### youtube-dl
