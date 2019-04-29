import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messagebox'
        self.left = 10
        self.top = 10
        self.width = 320
        self.heigh = 200
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.heigh)

        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?",
                                           QMessageBox.Yes, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked')

        else:
            print('No clicked.')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())