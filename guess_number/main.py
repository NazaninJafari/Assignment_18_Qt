import random
from tkinter import messagebox
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Guess_Num(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('guess_num.ui', None)
        self.ui.show()

        self.ui.lineEdit.setReadOnly(True)
        self.ui.pushButton.clicked.connect(self.choicenum_func)
        self.ui.check_button.clicked.connect(self.play)

    def choicenum_func(self):
        self.num = random.randint(0 , 500)
        self.ui.lineEdit.setReadOnly(False)

    def play(self):
        
        x = int(self.ui.lineEdit.text())
        if self.num > x :
            message_box = QMessageBox()
            message_box.setText('your number is lower!! ')
            message_box.exec()
            self.ui.lineEdit.setText('')
        elif self.num < x :
            message_box = QMessageBox()
            message_box.setText('your number is upper!! ')
            message_box.exec()
            self.ui.lineEdit.setText('')
        elif self.num == x :
            message_box = QMessageBox()
            message_box.setText('it is correct, You Won!')
            message_box.exec()
            self.ui.lineEdit.setText('')        
            self.ui.lineEdit.setReadOnly(True)


app = QApplication([])
window = Guess_Num()
app.exec()