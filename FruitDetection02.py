import sys
from pathlib import Path

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore 
from PyQt5.QtGui import * 

from FruitDetection01 import predictFruitClass, getTrainedModel

classes = {0: 'Apple Braeburn', 1: 'Avocado', 2: 'Banana', 3: 'Corn', 4: 'Eggplant', 5: 'Fig', 6: 'Grapefruit White', 7: 'Kiwi', 8: 'Lemon', 9: 'Mandarine', 10: 'Mango', 11: 'Mulberry', 12: 'Nut Forest', 13: 'Onion Red', 14: 'Orange', 15: 'Papaya', 16: 'Peach', 17: 'Pear', 18: 'Pepino', 19: 'Pepper Green', 20: 'Physalis', 21: 'Pineapple', 22: 'Plum', 23: 'Pomegranate', 24: 'Pomelo Sweetie', 25: 'Potato White', 26: 'Quince', 27: 'Raspberry', 28: 'Redcurrant', 29: 'Strawberry', 30: 'Tomato 1'}
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        '''
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        '''
        
        self.label1 = QLabel()
        self.label1.move(100,100)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
    def showDialog(self):

        home_dir = str(Path.home())

        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            trainedModel = getTrainedModel("fruit_classify_model_180820.h5")
            output = predictFruitClass(fname[0],trainedModel,classes)
            
            self.label1.setText(output)
             
       

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


