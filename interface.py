from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLineEdit, QMainWindow, QLabel
 

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Желтые окружности')
        
        self.make_button = QPushButton('Сделать окружность', self)
        self.make_button.move(10, 10)
        self.make_button.adjustSize()
