from ntpath import join
import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

class Pass_Generatore(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui' , None)
        self.ui.show()

        self.specialcaracter = ['!','@','#','%','^','&','*','?']
        self.listupp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.num = ['0','1','2','3','4','5','6','7','8','9']
        self.list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        self.ui.pushButton.clicked.connect(self.func_generate)

    def func_generate(self):
        
        # 5 letter /a number /an uppercase letter /a special caractere
        if self.ui.radioButton_simple.isChecked() :
            self.ui.textEdit.clear()
            self.password = random.choices(self.list, k=5) 
            self.password.append(random.choice(self.specialcaracter))
            self.password.append(random.choice(self.listupp))
            self.password.append(random.choice(self.num))

        # 6 letter /2 number /2 uppercase letter /2 special caractere
        elif self.ui.radioButton_Extra.isChecked() :
            self.ui.textEdit.clear()
            self.password = random.choices(self.list, k=6)
            for i in range(2): 
                self.password.append(random.choice(self.specialcaracter))
                self.password.append(random.choice(self.listupp))
                self.password.append(random.choice(self.num))

        # 11 letter /3 number /3 uppercase letter /3 special caractere
        elif self.ui.radioButton_superExtra.isChecked() :
            self.ui.textEdit.clear()
            self.password = random.choices(self.list, k=11)
            for i in range(3): 
                self.password.append(random.choice(self.specialcaracter))
                self.password.append(random.choice(self.listupp))
                self.password.append(random.choice(self.num))
        
        random.shuffle(self.password)
        #converting the list to string
        self.ui.textEdit.setText(''.join(self.password))

app = QApplication([])
window = Pass_Generatore()
app.exec()
