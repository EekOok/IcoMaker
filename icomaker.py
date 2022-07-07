from PIL import Image

import sys

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.monlayout = QVBoxLayout()
        self.ligne1 = QHBoxLayout()
        self.monlayout.addLayout(self.ligne1)

        self.lbl_source = QLabel("Selectionner l'image source")
        self.ligne1.addWidget(self.lbl_source)

        self.buttonGetSource = QPushButton("...")
        self.buttonGetSource.clicked.connect(self.selectsource)
        self.ligne1.addWidget(self.buttonGetSource)

        self.ligne2 = QHBoxLayout()
        self.monlayout.addLayout(self.ligne2)

        self.buttonvalide = QPushButton("Générer icone")
        self.buttonvalide.clicked.connect(self.generico)
        self.monlayout.addWidget(self.buttonvalide)

        self.container = QWidget()
        self.container.setLayout(self.monlayout)
        self.setCentralWidget(self.container)

        self.format = [(64, 64)]
        self.complet = ""
        self.fichext = []

    def selectsource(self):
        dialog = QFileDialog(self)
        dialog.setNameFilter(QObject().tr("Images (*.png *.jpg)"))

        if dialog.exec():
            chemin = str(dialog.directory().path())
            self.complet = str(dialog.selectedFiles()[0])
            fichier = self.complet[len(chemin)+1:]
            self.fichext = fichier.split('.')

    def generico(self):
        img = Image.open(self.complet)
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)

        if dialog.exec():
            chemin = str(dialog.directory().path())

            img.save(chemin+"/"+self.fichext[0]+'_ico.ico', sizes=self.format)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
