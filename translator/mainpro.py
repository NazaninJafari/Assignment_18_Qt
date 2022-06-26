from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Translator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        
        self.word = []
        self.read_file()
        self.ui.pushbutton.clicked.connect(self.translate_func)
        self.ui.clearbutton.clicked.connect(self.clear_func)

    def read_file(self):
        file = open('database.txt' , 'r')
        row = file.read().split('\n')
        x=0
        y=1
        while x < len(row):
            self.word.append({'English': row[x], 'Persian': row[y]})
            x += 2
            y += 2

    def translate_func(self):

        #eng to per
        if self.ui.radioButton.isChecked():
            self.ui.textEdit_2.clear()
            str_txt = self.ui.textEdit.toPlainText()
            txt = str_txt.split('.')
            for i in range(len(txt)):
                list = txt[i].split(' ')
                for i in range(len(list)):
                    for j in range(len(self.word)):
                        if list[i] == self.word[j]['English'] and i != len(list)-1 :
                            self.ui.textEdit_2.setText(self.ui.textEdit_2.toPlainText() + ' ' + self.word[j]['Persian'] + ' ')
                            break

                        elif list[i] == self.word[j]['English'] and i == len(list)-1 :    
                            self.ui.textEdit_2.setText(self.ui.textEdit_2.toPlainText() + ' ' +self.word[j]['Persian'])
                            break
            
                        elif j == len(self.word)-1 and list[i] != self.word[j]['English']:
                            self.ui.textEdit_2.setText(self.ui.textEdit_2.toPlainText() + ' ' + str(list[i]) + ' ')
        #per to eng
        elif self.ui.radioButton_2.isChecked():
            str_txt = self.ui.textEdit.toPlainText()
            txt = str_txt.split('.')
            for i in range(len(txt)):
                list = txt[i].split(' ')
                for i in range(len(list)): 
                    for j in range(len(self.word)):
                        if list[i] == self.word[j]['Persian'] and i != len(list)-1 :
                            self.ui.textEdit_2.setText(self.ui.textEdit_2.toPlainText() + ' ' + self.word[j]['English'] + ' ')
                            break
                        elif list[i] == self.word[j]['Persian'] and i == len(list)-1 :    
                            self.ui.textEdit_2.setText(self.ui.textEdit_2.toPlainText() + ' ' +self.word[j]['English'])
                            break
                        elif j == len(self.word)-1 and list[i] != self.word[j]['Persian']:
                            self.ui.textEdit_2.setText(self.ui.textEdit_2.toPlainText() + ' ' + str(list[i]) + ' ')    
        
    def clear_func(self):
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()        

app = QApplication([])
window = Translator()
app.exec()