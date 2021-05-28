import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from util.db_util import FoodDatabase
from util.foodselect_util import FoodSelect
#from util.order_util import OrderUtil

class Resto(QMainWindow):
    def __init__(self):
        super(Resto, self).__init__()
        loadUi('Resto2.ui', self)

        self.But_Dashboard.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Dashboard_Page))
        self.But_Menu.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Menu_Page))
        self.But_Bayar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Bayar))
        self.But_Exit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Exit_Page))
        self.Lbl_Lasagna.setText(str(FoodSelect.select_stock('Lasagna')))
        self.Lbl_Risol.setText(str(FoodSelect.select_stock('Risol Mayo')))
        self.Lbl_Bulgogi.setText(str(FoodSelect.select_stock('Bulgogi')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Ayam Geprek')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Tteokbokki')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Bingsoo')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Panna Cotta')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Tiramisu')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Orange Juice')))
        self.Lbl_Ayam.setText(str(FoodSelect.select_stock('Smoothie')))
        self.Frame_edit.setVisible(False)
        self.Frame_edit_2.setVisible(False)
        self.Frame_edit_3.setVisible(False)
        self.Frame_edit_4.setVisible(False)
        self.Frame_edit_5.setVisible(False)
        #self.Frame_4.setVisible(False)







app = QApplication(sys.argv)
mainwindow = Resto()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMinimumWidth(1422)
widget.setMinimumHeight(1052)
widget.show()
app.exec()
