import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from util.db_util import FoodDatabase
from util.order_util import OrderUtil

connect = FoodDatabase.connect()
c = connect.cursor()
#lasagna
c.execute("SELECT name,price,stock FROM food ")
lasagna =c.fetchall()[0]
#risol
c.execute("SELECT name,price,stock FROM food ")
risol =c.fetchall()[1]
#bulgogi
c.execute("SELECT name,price,stock FROM food ")
bulgogi =c.fetchall()[2]
#ayam
c.execute("SELECT name,price,stock FROM food ")
ayam =c.fetchall()[3]
#tteok
c.execute("SELECT name,price,stock FROM food ")
tteok =c.fetchall()[4]
#bingsoo
c.execute("SELECT name,price,stock FROM food ")
bingsoo =c.fetchall()[5]
#panna
c.execute("SELECT name,price,stock FROM food ")
panna =c.fetchall()[2]
#tiramisu
c.execute("SELECT name,price,stock FROM food ")
tiramisu =c.fetchall()[3]
#orange
c.execute("SELECT name,price,stock FROM food ")
orange =c.fetchall()[4]
#smoothie
c.execute("SELECT name,price,stock FROM food ")
smoothie =c.fetchall()[5]
connect.commit()
connect.close()


class Resto(QMainWindow):
    def __init__(self):
        super(Resto, self).__init__()
        loadUi('Resto2.ui', self)

        self.But_Dashboard.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Dashboard_Page))
        self.But_Menu.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Menu_Page))
        self.But_Bayar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Bayar))
        self.But_Exit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Exit_Page))
        self.Lbl_Lasagna.setText(str(lasagna[2]))
        self.Lbl_Risol.setText(str(risol[2]))
        self.Lbl_Bulgogi.setText(str(bulgogi[2]))
        self.Lbl_Ayam.setText(str(ayam[2]))
        self.Lbl_Ayam.setText(str(tteok[2]))
        self.Lbl_Ayam.setText(str(bingsoo[2]))
        self.Lbl_Ayam.setText(str(panna[2]))
        self.Lbl_Ayam.setText(str(tiramisu[2]))
        self.Lbl_Ayam.setText(str(orange[2]))
        self.Lbl_Ayam.setText(str(smoothie[2]))
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
