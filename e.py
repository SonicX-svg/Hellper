import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSlot,QThread
from PyQt5.QtGui import QPixmap
import sys
import mouse
import time
from datetime import date
import os 

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.coors_labels = []
        self.initUI()
        self.cell = 0
        self.c_date = []
        self.date_obj = 0
        self.day_to_add = 0
        self.curr_date = 0
        self.date = 0
        
    def asyncFunction(self):
        print("Async function called")
        
    def initUI(self):
        self.setGeometry(200, 200,  498, 276)
        self.setWindowTitle('Transparent Window')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        #self.setStyleSheet("background-color: transparent; border: 1px solid black")

        grid = QGridLayout()
        grid.setSpacing(0)
        self.setLayout(grid)

        for i in range(6):
            for j in range(7):
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)  # Center the image
                grid.addWidget(label, i, j)
                
    
    def set_image(self, row, col, image_path):
        for i in range(self.layout().rowCount()):
            for j in range(self.layout().columnCount()):
                widget = self.layout().itemAtPosition(i, j).widget()
                if isinstance(widget, QLabel):
                    if i == row and j == col:
                        pixmap = QPixmap(image_path)
                        pixmap = pixmap.scaled(58, 40)
                        widget.setPixmap(pixmap)
                        break
                        
    def get_label_coordinates(self):
        for widget in self.findChildren(QLabel):
            rect = widget.geometry()
            screen_rect = self.frameGeometry()
            label_x = rect.x() 
            label_y = rect.y() 
            label_width = rect.width()
            label_height = rect.height()
            self.coors_labels.append([label_x, label_y,label_width, label_height])
            print("Label coordinates:", label_x, label_y, "Size:", label_width, label_height)
            
    def save_cell_number(self, cell_number):
        print('save_cell_number = ', cell_number)
        with open('check_cell_info.txt','r+') as f:
            f.write(str(cell_number))
            f.seek(0)  # move back to the beginning of the file
    
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # Left mouse button
            x, y = event.pos().x(), event.pos().y()
            self.get_label_coordinates()
            for i, params in enumerate(self.coors_labels):

                if x >= params[0] and x <= params[0]+ params[-2]:
                    if y >= params[1] and y <= params[1]+ params[-1]:
                        print('номер ячейки = ', i+1)
                        
                        self.cell = i+1
                        print('self.cell = ', self.cell)
                        self.c_date = [int(i) for i in self.date.split('/')]
                        self.date_obj = date(self.c_date[-1], self.c_date[0], 1) # получаем текущий месяц и год из ткинтера ! узнаем про 1-ое число
                        print('self.date_obj = ', self.date_obj)
                        self.day_to_add = int(self.date_obj.strftime("%w")) - 1
                        print('self.day_to_add = ', self.day_to_add)
                        self.curr_date = self.cell-self.day_to_add
                        print('curr_date!!!!!!!!!!!!!!!!!!!!!!!!!!!! = ',self.curr_date)
                        self.save_cell_number(self.curr_date)
                        break
            i = 0    
            print("Mouse click at qt:", x, y)
    
    def infinite_loop(self):
        prev = 0
        while True:
            # Your infinite loop code here
            #print("Looping...")
            isempty = os.stat("tkc_flags.txt").st_size
            isemptydate = os.stat("date.txt").st_size
            #print("isempty", isempty)
            if isempty > prev:
                prev = isempty
                with open("tkc_flags.txt", "r+") as f:
                    dict_flags = eval(f.readlines()[0])
                    print('dict_flags = ', dict_flags)
                #print('flag flag flag flag flag flag', flag)
                for datee, cortage in dict_flags.items():
                    self.c_date = [int(i) for i in datee.split('/')]
                    self.date_obj = date(self.c_date[-1], self.c_date[0], 1) # получаем текущий месяц и год из ткинтера ! узнаем про 1-ое число
                    self.day_to_add = int(self.date_obj.strftime("%w")) - 1
                    self.curr_date = self.c_date[1]+self.day_to_add
                    print('curr_date!!!!!!!!!!!!!!!!!!!!!!!!!!!! = ',self.curr_date)
                    row, col = self.curr_date//7+1, self.curr_date%7
                    self.set_image(row-1, col-1, cortage[0])
                time.sleep(1)  # Simulate a delay
            elif isemptydate>0:
                with open("date.txt", "r+") as f:
                    self.date = f.read()


class Worker(QThread):
    def __init__(self, window):
        super().__init__()
        self.window = window


    def run(self):
        self.window.infinite_loop()


def start_qt():
    print('START START START START START STARTSTART STARTSTART STARTSTARTSTART START STARTSTARTSTARTSTARTSTART START STARTSTARTSTART START START START ')
    app = QApplication(sys.argv)
    window = TransparentWindow()
    worker = Worker(window)
    window.set_image(1, 2, 'translucent-image.png')
    worker.start()
    window.show()
    sys.exit(app.exec_())
    

start_qt()

