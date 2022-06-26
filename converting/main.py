from msilib.schema import Class
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.list = ['Length','Weight','Temprature','Data']
        self.weightlist = ['kilograme','gram','ton','pound']
        self.templist = ['fahrenheit','kelvin','centigrade']
        self.length = ['milimeter','centimeter','metre','kilometer','inch']
        self.datalist = ['bit','byte','kilobyte','megabyte','gigabyte','terabyte']
        
        self.ui.comboBox_3.addItems(self.list)
        self.ui.comboBox.addItems(self.length)
        self.ui.comboBox_3.currentTextChanged.connect(self.additem)
        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.clearbutton.clicked.connect(self.clear_func)
        
    def additem(self):
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        if self.ui.comboBox_3.currentText() == 'Length':
            self.ui.comboBox.addItems(self.length)
            self.ui.comboBox_2.addItems(self.length)
        
        elif self.ui.comboBox_3.currentText() == 'Weight':
            self.ui.comboBox.addItems(self.weightlist)
            self.ui.comboBox_2.addItems(self.weightlist)

        elif  self.ui.comboBox_3.currentText() == 'Temprature':
            self.ui.comboBox.addItems(self.templist)
            self.ui.comboBox_2.addItems(self.templist)
   
        elif self.ui.comboBox_3.currentText() == 'Data':
            self.ui.comboBox.addItems(self.datalist)
            self.ui.comboBox_2.addItems(self.datalist)


    def calculate(self):
        x = self.ui.comboBox.currentText()
        y = self.ui.comboBox_2.currentText()
        input = float(self.ui.lineEdit.text())

        if x == 'kilograme' :
            if y == 'gram':
                output = input * 1000
            elif y == 'ton':
                output = input / 1000           
            elif y == 'pound':
                output = input * 2.20462
            elif y == 'kilograme':
                output = input         
        
        elif x == 'pound' :
            if y == 'gram':
                output = input * 453.59
            elif y == 'ton':
                output = input * 0.00045359            
            elif y == 'kilograme':
                output = input * 0.45359
            elif y == 'pound' :
                output = input    
        
        elif x == 'gram':
            if y == 'pound':
                output = input / 453.59 
            elif y == 'ton':
                output = input / 1000000           
            elif y == 'kilograme':
                output = input / 1000
            elif y == 'gram':
                output = input

        elif x == 'ton':
            if y == 'pound':
                output = input * 2204.6
            elif y == 'gram':
                output = input * 1000000             
            elif y == 'kilograme':
                output = input * 1000
            elif y == 'ton':
                output = input

        elif x == 'fahrenheit' :
            if y == 'kelvin':
                output = (input + 459.67) / 1.8
            elif y == 'centigrade' :
                output = (input - 32) / 1.8
            elif y == 'fahrenheit' :
                output = input
        
        elif x == 'centigrade' :
            if y == 'kelvin':
                output = input + 273.15
            elif y == 'fahrenheit' :
                output = (input * 1.8) + 32
            elif y == 'centigrade' :
                output = input
        
        elif x == 'kelvin':
            if y == 'centigrade':
                output = input - 273.15
            elif y == 'fahrenheit' :
                output = (input * 1.8) - 459.67
            elif y == 'kelvin':
                output = input
        
        elif x == 'milimeter' :
            if y == 'centimeter':
                output = input / 10
            elif y == 'metre' :
                output = input / 1000
            elif y == 'kilometer' :
                output = input / 1000000
            elif y == 'inch' :
                output = input * 0.03937
            elif y == 'milimeter' :
                output = input     

        elif x == 'centimeter':
            if y == 'milimeter':
                output = input * 10
            elif y == 'metre' :
                output = input / 100
            elif y == 'kilometer' :
                output = input / 100000
            elif y == 'inch' :
                output = input * 0.3937
            elif y == 'centimeter':
                output = input
        
        elif x == 'metre' :
            if y == 'milimeter':
                output = input * 1000
            elif y == 'centimeter' :
                output = input * 100
            elif y == 'kilometer' :
                output = input / 1000
            elif y == 'inch' :
                output = input * 39.37
            elif y == 'metre' :
                output = input

        elif x == 'kilometer' :
            if y == 'milimeter':
                output = input * 1000000
            elif y == 'centimeter' :
                output = input * 100000
            elif y == 'metre' :
                output = input * 1000
            elif y == 'inch' :
                output = input * 39370
            elif y == 'kilometer' :
                output = input
       
        elif x == 'inch' :
            if y == 'milimeter':
                output = input * 25.4
            elif y == 'centimeter' :
                output = input * 2.54
            elif y == 'metre' :
                output = input * 0.0254
            elif y == 'kilometer' :
                output = input * 0.0000254
            elif y == 'inch' :
                output = input
        
        elif x == 'bit':
            if y == 'byte':
                output = input / 8
            elif y == 'kilobyte':
                output = input / (1024*8)
            elif y == 'megabyte':
                output = input / (1024**2 *8)
            elif y == 'gigabyte':
                output = input / (1024**3 *8)
            elif y == 'terabyte':
                output = input / (1024**4 *8)
            elif y == 'bit':
                output = input
        
        elif x == 'byte':
            if y == 'bit':
                output = input * 8
            elif y == 'kilobyte':
                output = input / 1024
            elif y == 'megabyte':
                output = input / (1024**2)
            elif y == 'gigabyte':
                output = input / (1024**3)
            elif y == 'terabyte':
                output = input / (1024**4)
            elif y == 'byte':
                output = input
        
        elif x == 'kilobyte':
            if y == 'bit':
                output = input * 8192
            elif y == 'byte' :
                output = input * 1024
            elif y == 'megabyte':
                output = input / 1024
            elif y == 'gigabyte':
                output = input / (1024**2)
            elif y == 'terabyte':
                output = input / (1024**3)
            elif y == 'kilobyte':
                output = input
        
        elif x == 'megabyte':
            if y == 'bit':
                output = input * (1024**2)*8 
            elif y == 'byte' :
                output = input * (1024**2)
            elif y == 'kilobyte':
                output = input * 1024
            elif y == 'gigabyte':
                output = input / 1024
            elif y == 'terabyte':
                output = input / (1024**2)
            elif y == 'megabyte':
                output = input
        
        elif x == 'gigabyte':
            if y == 'bit':
                output = input * (1024**3) *8
            elif y == 'byte' :
                output = input * (1024**3)
            elif y == 'kilobyte':
                output = input * (1024**2)
            elif y == 'megabyte':
                output = input * 1024
            elif y == 'terabyte':
                output = input / 1024
            elif y == 'gigabyte':
                output = input
        
        elif x == 'terabyte':
            if y == 'bit':
                output = input * (1024**4) *8
            elif y == 'byte' :
                output = input * (1024**4)
            elif y == 'kilobyte':
                output = input * (1024**3)
            elif y == 'megabyte':
                output = input * (1024**2)
            elif y == 'gigabyte':
                output = input * 1024
            elif y == 'terabyte':
                output = input    

        self.ui.lineEdit_2.setText(str(output))

    def clear_func(self):        
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')

app = QApplication([])
window = MainWindow()
app.exec()        