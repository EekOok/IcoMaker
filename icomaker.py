from PIL import Image

import sys

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IcoMaker")

        self.mylayout = QVBoxLayout()
        self.line1 = QHBoxLayout()
        self.mylayout.addLayout(self.line1)

        self.lbl_img = QLabel("Selectionner l'image source")
        self.line1.addWidget(self.lbl_img)

        self.button_get_img = QPushButton("...")
        self.button_get_img.clicked.connect(self.selectimg)
        self.line1.addWidget(self.button_get_img)

        self.line2 = QHBoxLayout()
        self.mylayout.addLayout(self.line2)

        self.button_create = QPushButton("Générer icone")
        self.button_create.clicked.connect(self.createico)
        self.mylayout.addWidget(self.button_create)

        self.container = QWidget()
        self.container.setLayout(self.mylayout)
        self.setCentralWidget(self.container)

        self.format = [(64, 64)]
        self.path_n_file = ""
        self.file_extension = []

    def selectimg(self):

        dialog = QFileDialog(self)
        dialog.setNameFilter(QObject().tr("Images (*.png *.jpg)"))

        if dialog.exec():
            path = str(dialog.directory().path())
            self.path_n_file = str(dialog.selectedFiles()[0])
            file = self.path_n_file[len(path)+1:]
            self.file_extension = file.split('.')

    def createico(self):
        img = Image.open(self.path_n_file)
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)

        if dialog.exec():
            chemin = str(dialog.directory().path())

            img.save(chemin+"/"+self.file_extension[0]+'_ico.ico', sizes=self.format)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
