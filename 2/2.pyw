from PyQt5.QtWidgets import (QApplication, QFileDialog, QDialog,
    QGridLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from image_to_ascii import ImageToAscii


class Wind(QDialog):
    def __init__(self):
        super(Wind, self).__init__()

        self.setMinimumSize(300, 200)
        self.setWindowTitle("The homework to 19.09.23")

        layout = QGridLayout(self)
        self.setLayout(layout)
        label1 = QLabel("Please select an option", alignment=Qt.AlignCenter)
        label1.setFont(QFont('Arial', 17))
        layout.addWidget(label1, 0, 0, 1, 5)
        

        img_but = QPushButton("Image to ASCII")
        txt_but = QPushButton("Text to file")
        img_but.setMinimumSize(100, 50)
        txt_but.setMinimumSize(100, 50)
        cancel = QPushButton("Exit")

        img_but.clicked.connect(self.img_to_ascii)
        txt_but.clicked.connect(self.txt_to_file)
        cancel.clicked.connect(exit)

        layout.addWidget(img_but, 1, 0, 1, 2)
        layout.addWidget(txt_but, 1, 3, 1, 2)
        layout.addWidget(cancel, 2, 0, 1, 5)
    
    def img_to_ascii(self):
        imagepath = QFileDialog.getOpenFileName(filter="Image (*.png *.jpg *.bmp)", caption="Choose Image")[0]
        
        if imagepath != '':
            import os
            ImageToAscii(imagePath=imagepath, outputFile="result.txt")

            os.system('result.txt')  
        else:   
            msg = QMessageBox()
            msg.setText("Please select the image file!!!")
            msg.setWindowTitle("Error")
            msg.exec_()

    def txt_to_file(self):
        Text_input = QDialog()
        Text_input.setMaximumSize(500, 500)
        Text_input.setWindowTitle('Please enter the text, and push the button')

        self.text = QTextEdit('Please enter the text, and push the button')
        self.text.setMinimumSize(500, 300)

        but = QPushButton('Enter')
        but.setMinimumSize(500, 100)

        layot = QVBoxLayout(Text_input)
        layot.addWidget(self.text)
        layot.addWidget(but)

        but.clicked.connect(self.output_text)

        Text_input.exec_()

    def output_text(self):
        text = self.text.toPlainText()

        if text != '':
            import os

            with open("result.txt", 'w') as f:
                f.write(text)
            os.system('result.txt')

        else:   
            msg = QMessageBox()
            msg.setText("Please enter any text!!!")
            msg.setWindowTitle("Error")
            msg.exec_()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wind = Wind()
    sys.exit(wind.exec_())