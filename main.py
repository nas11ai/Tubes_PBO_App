import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
#from util.db_util import FoodDatabase
from util.foodselect_util import FoodSelect
from util.order_util import OrderUtil
import datetime

x = datetime.datetime.now()
o= x.strftime("%A")+", "+x.strftime("%b")+" "+x.strftime("%d")+" "+x.strftime("%Y")
pembayaran = []
harga = []
total_harga=[]
total1=[0]
total2=[0]
total3=[0]
total4=[0]
total5=[0]



class Resto(QMainWindow):
    def __init__(self):
        super(Resto, self).__init__()
        loadUi('Resto2.ui', self)
        self.But_Dashboard.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Dashboard_Page))
        self.But_Menu.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.Menu_Page))
        self.But_Bayar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Bayar))
        self.But_Exit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Exit_Page))
        self.But_Done.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Frame_Meja))
        self.But_Ok.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Exit_Page))
        self.But_Done.clicked.connect(self.stock)
        self.But_Ok.clicked.connect(self.back)
        self.Frame_edit.setVisible(False)
        self.Frame_edit_2.setVisible(False)
        self.Frame_edit_3.setVisible(False)
        self.Frame_edit_4.setVisible(False)
        self.Frame_edit_5.setVisible(False)
        self.Frame_1.setVisible(False)
        self.Frame_2.setVisible(False)
        self.Frame_3.setVisible(False)
        self.Frame_4.setVisible(False)
        self.Frame_5.setVisible(False)
        self.But_edit.clicked.connect(lambda:self.Clear())
        self.But_Menu.clicked.connect(self.Visible)
        self.But_plus.clicked.connect(self.Plus1)
        self.But_min.clicked.connect(self.Min1)
        self.But_plus2.clicked.connect(self.Plus2)
        self.But_min2.clicked.connect(self.Min2)
        self.But_plus3.clicked.connect(self.Plus3)
        self.But_min3.clicked.connect(self.Min3)
        self.But_plus4.clicked.connect(self.Plus4)
        self.But_min4.clicked.connect(self.Min4)
        self.But_plus5.clicked.connect(self.Plus5)
        self.But_min5.clicked.connect(self.Min5)
        self.But_Lasagna.clicked.connect(self.Lasagna)
        self.But_Risol.clicked.connect(self.Risol)
        self.But_Bulgogi.clicked.connect(self.Bulgogi)
        self.But_Ayam.clicked.connect(self.Ayam)
        self.But_Tteok.clicked.connect(self.Tteok)
        self.But_Bingsoo.clicked.connect(self.Bingsoo)
        self.But_Panna.clicked.connect(self.Panna)
        self.But_Tiramisu.clicked.connect(self.Tiramisu)
        self.But_Orange.clicked.connect(self.Orange)
        self.But_Smoothie.clicked.connect(self.Smoothie)
        self.But_Refresh.clicked.connect(self.Refresh)
        self.But_Clear.clicked.connect(self.Edit1)
        self.But_Clear_2.clicked.connect(self.Edit2)
        self.But_Clear_3.clicked.connect(self.Edit3)
        self.But_Clear_4.clicked.connect(self.Edit4)
        self.But_Clear_5.clicked.connect(self.Edit5)
        self.But_Complate.clicked.connect(self.Pay)
        self.But_Bayar.setEnabled(False)
        self.Tgl.setText(o)
        self.Tgl_2.setText(o)
        self.Tgl_3.setText(o)
        self.Tgl_4.setText(o)
        if FoodSelect.select_stock(self.Label_Lasagna.text()) == 0:
            self.Frame_Lasagna.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Risol.text()) == 0:
            self.Frame_Risol.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Ayam.text()) == 0:
            self.Frame_Ayam.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Tteok.text()) == 0:
            self.Frame_Tteok.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Bulgogi.text()) == 0:
            self.Frame_Bulgogi.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Bingsoo.text()) == 0:
            self.Frame_Bingsoo.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Panna.text()) == 0:
            self.Frame_Panna.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Orange.text()) == 0:
            self.Frame_Orange.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Smoothie.text()) == 0:
            self.Frame_Smoothie.setEnabled(False)
        if FoodSelect.select_stock(self.Label_Tiramisu.text()) == 0:
            self.Frame_Tiramisu.setEnabled(False)


    def Lasagna(self):
        pembayaran.append('Lasagna')
        self.Frame_Lasagna.setEnabled(False)

    def Risol(self):
        pembayaran.append('Risol Mayo')
        self.Frame_Risol.setEnabled(False)

    def Bulgogi(self):
        pembayaran.append('Bulgogi')
        self.Frame_Bulgogi.setEnabled(False)

    def Ayam(self):
        pembayaran.append('Ayam Geprek')
        self.Frame_Ayam.setEnabled(False)

    def Tteok(self):
        pembayaran.append('Tteokbokki')
        self.Frame_Tteok.setEnabled(False)

    def Bingsoo(self):
        pembayaran.append('Bingsoo')
        self.Frame_Bingsoo.setEnabled(False)

    def Panna(self):
        pembayaran.append('Panna Cotta')
        self.Frame_Panna.setEnabled(False)

    def Tiramisu(self):
        pembayaran.append('Tiramisu')
        self.Frame_Tiramisu.setEnabled(False)

    def Orange(self):
        pembayaran.append('Orange Juice')
        self.Frame_Orange.setEnabled(False)

    def Smoothie(self):
        pembayaran.append('Smoothie')
        self.Frame_Smoothie.setEnabled(False)




    def Clear(self):
        self.Frame_edit.setVisible(True)
        self.Frame_edit_2.setVisible(True)
        self.Frame_edit_3.setVisible(True)
        self.Frame_edit_4.setVisible(True)
        self.Frame_edit_5.setVisible(True)

    def Visible(self):
        self.Frame_edit.setVisible(False)
        self.Frame_edit_2.setVisible(False)
        self.Frame_edit_3.setVisible(False)
        self.Frame_edit_4.setVisible(False)
        self.Frame_edit_5.setVisible(False)
        harga.clear()
        self.Lbl_Stock_Lasagna.setText(str(FoodSelect.select_stock('Lasagna')))
        self.Lbl_Stock_Risol.setText(str(FoodSelect.select_stock('Risol Mayo')))
        self.Lbl_Stock_Bulgogi.setText(str(FoodSelect.select_stock('Bulgogi')))
        self.Lbl_Stock_Ayam.setText(str(FoodSelect.select_stock('Ayam Geprek')))
        self.Lbl_Stock_Tteo.setText(str(FoodSelect.select_stock('Tteokbokki')))
        self.Lbl_Stock_Bingso.setText(str(FoodSelect.select_stock('Bingsoo')))
        self.Lbl_Stock_Panna.setText(str(FoodSelect.select_stock('Panna Cotta')))
        self.Lbl_Stock_Tiramisu.setText(str(FoodSelect.select_stock('Tiramisu')))
        self.Lbl_Stock_Orange.setText(str(FoodSelect.select_stock('Orange Juice')))
        self.Lbl_Stock_Smoothie.setText(str(FoodSelect.select_stock('Smoothie')))


    def Pay(self):
        self.But_Bayar.setEnabled(True)
        for j in pembayaran:
            if j in pembayaran[0]:
                self.Frame_1.setVisible(True)
                harga.append(FoodSelect.select_price(pembayaran[0]))
                total1.append(harga[0])
                if total1[1]:
                    total1.remove(total1[0])
                self.Lbl_quantity.setText(str(1))
                if pembayaran[0] == 'Lasagna':
                    self.label_Food.setText(self.Label_Lasagna.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Lasagna')))
                    total_harga=sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Risol Mayo':
                    self.label_Food.setText(self.Label_Risol.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Risol Mayo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Bulgogi':
                    self.label_Food.setText(self.Label_Bulgogi.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Bulgogi')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Ayam Geprek':
                    self.label_Food.setText(self.Label_Ayam.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Ayam Geprek')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Tteokbokki':
                    self.label_Food.setText(self.Label_Tteok.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Tteokbokki')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Bingsoo':
                    self.label_Food.setText(self.Label_Bingsoo.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Bingsoo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Panna Cotta':
                    self.label_Food.setText(self.Label_Panna.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Panna Cotta')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Tiramisu':
                    self.label_Food.setText(self.Label_Tiramisu.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Tiramisu')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Orange Juice':
                    self.label_Food.setText(self.Label_Orange.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Orange Juice')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[0] == 'Smoothie':
                    self.label_Food.setText(self.Label_Smoothie.text())
                    self.label_harga.setText("Rp. "+str(FoodSelect.select_price('Smoothie')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
            elif j in pembayaran[1]:
                self.Frame_2.setVisible(True)
                harga.append(FoodSelect.select_price(pembayaran[1]))
                total2.append(harga[1])
                if total2[1]:
                    total2.remove(total2[0])
                self.Lbl_quantity_2.setText(str(1))
                if pembayaran[1] == 'Lasagna':
                    self.label_Food2.setText(self.Label_Lasagna.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Lasagna')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Risol Mayo':
                    self.label_Food2.setText(self.Label_Risol.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Risol Mayo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Bulgogi':
                    self.label_Food2.setText(self.Label_Bulgogi.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Bulgogi')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Ayam Geprek':
                    self.label_Food2.setText(self.Label_Ayam.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Ayam Geprek')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Tteokbokki':
                    self.label_Food2.setText(self.Label_Tteok.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Tteokbokki')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Bingsoo':
                    self.label_Food2.setText(self.Label_Bingsoo.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Bingsoo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Panna Cotta':
                    self.label_Food2.setText(self.Label_Panna.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Panna Cotta')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Tiramisu':
                    self.label_Food2.setText(self.Label_Tiramisu.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Tiramisu')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Orange Juice':
                    self.label_Food2.setText(self.Label_Orange.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Orange Juice')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[1] == 'Smoothie':
                    self.label_Food2.setText(self.Label_Smoothie.text())
                    self.label_harga2.setText("Rp. "+str(FoodSelect.select_price('Smoothie')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
            elif j in pembayaran[2]:
                self.Frame_3.setVisible(True)
                harga.append(FoodSelect.select_price(pembayaran[2]))
                total3.append(harga[2])
                if total3[1]:
                    total3.remove(total3[0])
                self.Lbl_quantity_3.setText(str(1))
                if pembayaran[2] == 'Lasagna':
                    self.label_Food3.setText(self.Label_Lasagna.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Lasagna')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Risol Mayo':
                    self.label_Food3.setText(self.Label_Risol.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Risol Mayo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Bulgogi':
                    self.label_Food3.setText(self.Label_Bulgogi.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Bulgogi')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Ayam Geprek':
                    self.label_Food3.setText(self.Label_Ayam.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Ayam Geprek')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Tteokbokki':
                    self.label_Food3.setText(self.Label_Tteok.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Tteokbokki')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Bingsoo':
                    self.label_Food3.setText(self.Label_Bingsoo.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Bingsoo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Panna Cotta':
                    self.label_Food3.setText(self.Label_Panna.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Panna Cotta')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Tiramisu':
                    self.label_Food3.setText(self.Label_Tiramisu.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Tiramisu')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Orange Juice':
                    self.label_Food3.setText(self.Label_Orange.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Orange Juice')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[2] == 'Smoothie':
                    self.label_Food3.setText(self.Label_Smoothie.text())
                    self.label_harga3.setText("Rp. "+str(FoodSelect.select_price('Smoothie')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
            elif j in pembayaran[3]:
                self.Frame_4.setVisible(True)
                harga.append(FoodSelect.select_price(pembayaran[3]))
                total4.append(harga[3])
                if total4[1]:
                    total4.remove(total4[0])
                self.Lbl_quantity_4.setText(str(1))
                if pembayaran[3] == 'Lasagna':
                    self.label_Food4.setText(self.Label_Lasagna.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Lasagna')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Risol Mayo':
                    self.label_Food4.setText(self.Label_Risol.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Risol Mayo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Bulgogi':
                    self.label_Food4.setText(self.Label_Bulgogi.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Bulgogi')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Ayam Geprek':
                    self.label_Food4.setText(self.Label_Ayam.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Ayam Geprek')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Tteokbokki':
                    self.label_Food4.setText(self.Label_Tteok.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Tteokbokki')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Bingsoo':
                    self.label_Food4.setText(self.Label_Bingsoo.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Bingsoo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Panna Cotta':
                    self.label_Food4.setText(self.Label_Panna.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Panna Cotta')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Tiramisu':
                    self.label_Food4.setText(self.Label_Tiramisu.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Tiramisu')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Orange Juice':
                    self.label_Food4.setText(self.Label_Orange.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Orange Juice')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[3] == 'Smoothie':
                    self.label_Food4.setText(self.Label_Smoothie.text())
                    self.label_harga4.setText("Rp. "+str(FoodSelect.select_price('Smoothie')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
            elif j in pembayaran[4]:
                self.Frame_5.setVisible(True)
                harga.append(FoodSelect.select_price(pembayaran[4]))
                total5.append(harga[4])
                if total5[1]:
                    total5.remove(total1[0])
                self.Lbl_quantity_5.setText(str(1))
                if pembayaran[4] == 'Lasagna':
                    self.label_Food5.setText(self.Label_Lasagna.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Lasagna')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Risol Mayo':
                    self.label_Food5.setText(self.Label_Risol.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Risol Mayo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Bulgogi':
                    self.label_Food5.setText(self.Label_Bulgogi.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Bulgogi')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Ayam Geprek':
                    self.label_Food5.setText(self.Label_Ayam.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Ayam Geprek')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Tteokbokki':
                    self.label_Food5.setText(self.Label_Tteok.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Tteokbokki')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Bingsoo':
                    self.label_Food5.setText(self.Label_Bingsoo.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Bingsoo')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Panna Cotta':
                    self.label_Food5.setText(self.Label_Panna.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Panna Cotta')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Tiramisu':
                    self.label_Food5.setText(self.Label_Tiramisu.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Tiramisu')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Orange Juice':
                    self.label_Food5.setText(self.Label_Orange.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Orange Juice')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
                elif pembayaran[4] == 'Smoothie':
                    self.label_Food5.setText(self.Label_Smoothie.text())
                    self.label_harga5.setText("Rp. "+str(FoodSelect.select_price('Smoothie')))
                    total_harga = sum(harga)
                    self.lbl_Total.setText('Rp. ' + str(total_harga))
        print(harga)


    def Plus1(self):
        nilai = int(self.Lbl_quantity.text())
        plus = nilai + 1
        if plus > FoodSelect.select_stock(self.label_Food.text()):
            return FoodSelect.select_stock(self.label_Food.text())
        self.Lbl_quantity.setText(str(plus))
        if harga[1]:
            total = (plus * harga[0])
            total1.append(total)
            if total1[1]:
                total1.remove(total1[0])

    def Min1(self):
        nilai = int(self.Lbl_quantity.text())
        plus = nilai - 1
        if plus < 1:
            return nilai
        self.Lbl_quantity.setText(str(plus))
        if harga[0]:
            total=(plus*harga[0])
            total1.append(total)
            if total1[1]:
                total1.remove(total1[0])



    def Plus2(self):
        nilai = int(self.Lbl_quantity_2.text())
        plus = nilai + 1
        if plus > FoodSelect.select_stock(self.label_Food2.text()):
            return FoodSelect.select_stock(self.label_Food2.text())
        self.Lbl_quantity_2.setText(str(plus))
        if harga[1]:
            total = (plus * harga[1])
            total2.append(total)
            if total2[1]:
                total2.remove(total2[0])


    def Min2(self):
        nilai = int(self.Lbl_quantity_2.text())
        plus = nilai - 1
        if plus < 1:
            return nilai
        self.Lbl_quantity_2.setText(str(plus))
        if harga[1]:
            total = (plus * harga[1])
            total2.append(total)
            if total2[1]:
                total2.remove(total2[0])


    def Plus3(self):
        nilai = int(self.Lbl_quantity_3.text())
        plus = nilai + 1
        if plus > FoodSelect.select_stock(self.label_Food3.text()):
            return FoodSelect.select_stock(self.label_Food3.text())
        self.Lbl_quantity_3.setText(str(plus))
        if harga[2]:
            total = (plus * harga[2])
            total3.append(total)
            if total3[1]:
                total3.remove(total3[0])

    def Min3(self):
        nilai = int(self.Lbl_quantity_3.text())
        plus = nilai - 1
        if plus < 1:
            return nilai
        self.Lbl_quantity_3.setText(str(plus))
        if harga[2]:
            total = (plus * harga[2])
            total3.append(total)
            if total3[1]:
                total3.remove(total3[0])

    def Plus4(self):
        nilai = int(self.Lbl_quantity_4.text())
        plus = nilai + 1
        if plus > FoodSelect.select_stock(self.label_Food4.text()):
            return FoodSelect.select_stock(self.label_Food4.text())
        self.Lbl_quantity_4.setText(str(plus))
        if harga[3]:
            total = (plus * harga[3])
            total4.append(total)
            if total4[1]:
                total4.remove(total4[0])

    def Min4(self):
        nilai = int(self.Lbl_quantity_4.text())
        plus = nilai - 1
        if plus < 1:
            return nilai
        self.Lbl_quantity_4.setText(str(plus))
        if harga[3]:
            total = (plus * harga[3])
            total4.append(total)
            if total4[1]:
                total4.remove(total4[0])

    def Plus5(self):
        nilai = int(self.Lbl_quantity_5.text())
        plus = nilai + 1
        if plus > FoodSelect.select_stock(self.label_Food5.text()):
            return FoodSelect.select_stock(self.label_Food5.text())
        self.Lbl_quantity_5.setText(str(plus))
        if harga[4]:
            total = (plus * harga[4])
            total5.append(total)
            if total5[1]:
                total5.remove(total5[0])

    def Min5(self):
        nilai = int(self.Lbl_quantity_5.text())
        plus = nilai - 1
        if plus < 1:
            return nilai
        self.Lbl_quantity_5.setText(str(plus))
        if harga[4]:
            total = (plus * harga[4])
            total5.append(total)
            if total5[1]:
                total5.remove(total5[0])

    def Refresh(self):
        Total=total1[0]+total2[0]+total3[0]+total4[0]+total5[0]
        total_harga.append(Total)
        self.lbl_Total.setText('Rp. '+str(Total))

    def Edit1(self):
        if self.label_Food.text()== "Lasagna":
            self.Frame_Lasagna.setEnabled(True)
        elif self.label_Food.text()== "Risol Mayo":
            self.Frame_Risol.setEnabled(True)
        elif self.label_Food.text()== "Bulgogi":
            self.Frame_Bulgogi.setEnabled(True)
        elif self.label_Food.text()== "Ayam Geprek":
            self.Frame_Ayam.setEnabled(True)
        elif self.label_Food.text()== "Tteokbokki":
            self.Frame_Tteok.setEnabled(True)
        elif self.label_Food.text()== "Bingsoo":
            self.Frame_Bingsoo.setEnabled(True)
        elif self.label_Food.text()== "Tiramisu":
            self.Frame_Tiramisu.setEnabled(True)
        elif self.label_Food.text()== "Panna Cotta":
            self.Frame_Panna.setEnabled(True)
        elif self.label_Food.text()== "Orange Juice":
            self.Frame_Orange.setEnabled(True)
        elif self.label_Food.text()== "Smoothie":
            self.Frame_Smoothie.setEnabled(True)
        total1.clear()
        total2.clear()
        total3.clear()
        total4.clear()
        total5.clear()
        total1.append(0)
        total2.append(0)
        total3.append(0)
        total4.append(0)
        total5.append(0)
        pembayaran.remove(self.label_Food.text())
        self.Lbl_quantity.setText(str(1))
        self.Frame_1.setVisible(False)

    def Edit2(self):
        if self.label_Food2.text()== "Lasagna":
            self.Frame_Lasagna.setEnabled(True)
        elif self.label_Food2.text()== "Risol Mayo":
            self.Frame_Risol.setEnabled(True)
        elif self.label_Food2.text()== "Bulgogi":
            self.Frame_Bulgogi.setEnabled(True)
        elif self.label_Food2.text()== "Ayam Geprek":
            self.Frame_Ayam.setEnabled(True)
        elif self.label_Food2.text()== "Tteokbokki":
            self.Frame_Tteok.setEnabled(True)
        elif self.label_Food2.text()== "Bingsoo":
            self.Frame_Bingsoo.setEnabled(True)
        elif self.label_Food2.text()== "Tiramisu":
            self.Frame_Tiramisu.setEnabled(True)
        elif self.label_Food2.text()== "Panna Cotta":
            self.Frame_Panna.setEnabled(True)
        elif self.label_Food2.text()== "Orange Juice":
            self.Frame_Orange.setEnabled(True)
        elif self.label_Food2.text()== "Smoothie":
            self.Frame_Smoothie.setEnabled(True)
        pembayaran.remove(self.label_Food2.text())
        self.Lbl_quantity_2.setText(str(1))
        total1.clear()
        total2.clear()
        total3.clear()
        total4.clear()
        total5.clear()
        total1.append(0)
        total2.append(0)
        total3.append(0)
        total4.append(0)
        total5.append(0)
        self.Frame_2.setVisible(False)


    def Edit3(self):
        if self.label_Food3.text()== "Lasagna":
            self.Frame_Lasagna.setEnabled(True)
        elif self.label_Food3.text()== "Risol Mayo":
            self.Frame_Risol.setEnabled(True)
        elif self.label_Food3.text()== "Bulgogi":
            self.Frame_Bulgogi.setEnabled(True)
        elif self.label_Food3.text()== "Ayam Geprek":
            self.Frame_Ayam.setEnabled(True)
        elif self.label_Food3.text()== "Tteokbokki":
            self.Frame_Tteok.setEnabled(True)
        elif self.label_Food3.text()== "Bingsoo":
            self.Frame_Bingsoo.setEnabled(True)
        elif self.label_Food3.text()== "Tiramisu":
            self.Frame_Tiramisu.setEnabled(True)
        elif self.label_Food3.text()== "Panna Cotta":
            self.Frame_Panna.setEnabled(True)
        elif self.label_Food3.text()== "Orange Juice":
            self.Frame_Orange.setEnabled(True)
        elif self.label_Food3.text()== "Smoothie":
            self.Frame_Smoothie.setEnabled(True)
        pembayaran.remove(self.label_Food3.text())
        self.Lbl_quantity_3.setText(str(1))
        total1.clear()
        total2.clear()
        total3.clear()
        total4.clear()
        total5.clear()
        total1.append(0)
        total2.append(0)
        total3.append(0)
        total4.append(0)
        total5.append(0)
        self.Frame_3.setVisible(False)

    def Edit4(self):
        if self.label_Food4.text()== "Lasagna":
            self.Frame_Lasagna.setEnabled(True)
        elif self.label_Food4.text()== "Risol Mayo":
            self.Frame_Risol.setEnabled(True)
        elif self.label_Food4.text()== "Bulgogi":
            self.Frame_Bulgogi.setEnabled(True)
        elif self.label_Food4.text()== "Ayam Geprek":
            self.Frame_Ayam.setEnabled(True)
        elif self.label_Food4.text()== "Tteokbokki":
            self.Frame_Tteok.setEnabled(True)
        elif self.label_Food4.text()== "Bingsoo":
            self.Frame_Bingsoo.setEnabled(True)
        elif self.label_Food4.text()== "Tiramisu":
            self.Frame_Tiramisu.setEnabled(True)
        elif self.label_Food4.text()== "Panna Cotta":
            self.Frame_Panna.setEnabled(True)
        elif self.label_Food4.text()== "Orange Juice":
            self.Frame_Orange.setEnabled(True)
        elif self.label_Food4.text()== "Smoothie":
            self.Frame_Smoothie.setEnabled(True)
        pembayaran.remove(self.label_Food4.text())
        self.Lbl_quantity_4.setText(str(1))
        total1.clear()
        total2.clear()
        total3.clear()
        total4.clear()
        total5.clear()
        total1.append(0)
        total2.append(0)
        total3.append(0)
        total4.append(0)
        total5.append(0)
        self.Frame_4.setVisible(False)

    def Edit5(self):
        if self.label_Food5.text()== "Lasagna":
            self.Frame_Lasagna.setEnabled(True)
        elif self.label_Food5.text()== "Risol Mayo":
            self.Frame_Risol.setEnabled(True)
        elif self.label_Food5.text()== "Bulgogi":
            self.Frame_Bulgogi.setEnabled(True)
        elif self.label_Food5.text()== "Ayam Geprek":
            self.Frame_Ayam.setEnabled(True)
        elif self.label_Food5.text()== "Tteokbokki":
            self.Frame_Tteok.setEnabled(True)
        elif self.label_Food5.text()== "Bingsoo":
            self.Frame_Bingsoo.setEnabled(True)
        elif self.label_Food5.text()== "Tiramisu":
            self.Frame_Tiramisu.setEnabled(True)
        elif self.label_Food5.text()== "Panna Cotta":
            self.Frame_Panna.setEnabled(True)
        elif self.label_Food5.text()== "Orange Juice":
            self.Frame_Orange.setEnabled(True)
        elif self.label_Food5.text()== "Smoothie":
            self.Frame_Smoothie.setEnabled(True)
        pembayaran.remove(self.label_Food5.text())
        self.Lbl_quantity_5.setText(str(1))
        total1.clear()
        total2.clear()
        total3.clear()
        total4.clear()
        total5.clear()
        total1.append(0)
        total2.append(0)
        total3.append(0)
        total4.append(0)
        total5.append(0)
        self.Frame_5.setVisible(False)

    def stock(self):
        if self.label_Food.text():
            OrderUtil.order(self.label_Food.text(),(int(self.Lbl_quantity.text())))
        if self.label_Food2.text():
            OrderUtil.order(self.label_Food2.text(),(int(self.Lbl_quantity_2.text())))
        if self.label_Food3.text():
            OrderUtil.order(self.label_Food3.text(),(int(self.Lbl_quantity_3.text())))
        if self.label_Food4.text():
            OrderUtil.order(self.label_Food4.text(),(int(self.Lbl_quantity_4.text())))
        if self.label_Food5.text():
            OrderUtil.order(self.label_Food5.text(),(int(self.Lbl_quantity_5.text())))

    def back(self):
        self.But_Bayar.setEnabled(False)
        if self.label_Food.text():
            self.Frame_1.setVisible(False)
            if self.label_Food.text()== "Lasagna":
                self.Frame_Lasagna.setEnabled(True)
            elif self.label_Food.text()== "Risol Mayo":
                self.Frame_Risol.setEnabled(True)
            elif self.label_Food.text()== "Bulgogi":
                self.Frame_Bulgogi.setEnabled(True)
            elif self.label_Food.text()== "Ayam Geprek":
                self.Frame_Ayam.setEnabled(True)
            elif self.label_Food.text()== "Tteokbokki":
                self.Frame_Tteok.setEnabled(True)
            elif self.label_Food.text()== "Bingsoo":
                self.Frame_Bingsoo.setEnabled(True)
            elif self.label_Food.text()== "Tiramisu":
                self.Frame_Tiramisu.setEnabled(True)
            elif self.label_Food.text()== "Panna Cotta":
                self.Frame_Panna.setEnabled(True)
            elif self.label_Food.text()== "Orange Juice":
                self.Frame_Orange.setEnabled(True)
            elif self.label_Food.text()== "Smoothie":
                self.Frame_Smoothie.setEnabled(True)

        if self.label_Food2.text():
            self.Frame_2.setVisible(False)
            if self.label_Food2.text()== "Lasagna":
                self.Frame_Lasagna.setEnabled(True)
            elif self.label_Food2.text()== "Risol Mayo":
                self.Frame_Risol.setEnabled(True)
            elif self.label_Food2.text()== "Bulgogi":
                self.Frame_Bulgogi.setEnabled(True)
            elif self.label_Food2.text()== "Ayam Geprek":
                self.Frame_Ayam.setEnabled(True)
            elif self.label_Food2.text()== "Tteokbokki":
                self.Frame_Tteok.setEnabled(True)
            elif self.label_Food2.text()== "Bingsoo":
                self.Frame_Bingsoo.setEnabled(True)
            elif self.label_Food2.text()== "Tiramisu":
                self.Frame_Tiramisu.setEnabled(True)
            elif self.label_Food2.text()== "Panna Cotta":
                self.Frame_Panna.setEnabled(True)
            elif self.label_Food2.text()== "Orange Juice":
                self.Frame_Orange.setEnabled(True)
            elif self.label_Food2.text()== "Smoothie":
                self.Frame_Smoothie.setEnabled(True)

        if self.label_Food3.text():
            self.Frame_3.setVisible(False)
            if self.label_Food3.text()== "Lasagna":
                self.Frame_Lasagna.setEnabled(True)
            elif self.label_Food3.text()== "Risol Mayo":
                self.Frame_Risol.setEnabled(True)
            elif self.label_Food3.text()== "Bulgogi":
                self.Frame_Bulgogi.setEnabled(True)
            elif self.label_Food3.text()== "Ayam Geprek":
                self.Frame_Ayam.setEnabled(True)
            elif self.label_Food3.text()== "Tteokbokki":
                self.Frame_Tteok.setEnabled(True)
            elif self.label_Food3.text()== "Bingsoo":
                self.Frame_Bingsoo.setEnabled(True)
            elif self.label_Food3.text()== "Tiramisu":
                self.Frame_Tiramisu.setEnabled(True)
            elif self.label_Food3.text()== "Panna Cotta":
                self.Frame_Panna.setEnabled(True)
            elif self.label_Food3.text()== "Orange Juice":
                self.Frame_Orange.setEnabled(True)
            elif self.label_Food3.text()== "Smoothie":
                self.Frame_Smoothie.setEnabled(True)

        if self.label_Food4.text():
            self.Frame_4.setVisible(False)
            if self.label_Food4.text()== "Lasagna":
                self.Frame_Lasagna.setEnabled(True)
            elif self.label_Food4.text()== "Risol Mayo":
                self.Frame_Risol.setEnabled(True)
            elif self.label_Food4.text()== "Bulgogi":
                self.Frame_Bulgogi.setEnabled(True)
            elif self.label_Food4.text()== "Ayam Geprek":
                self.Frame_Ayam.setEnabled(True)
            elif self.label_Food4.text()== "Tteokbokki":
                self.Frame_Tteok.setEnabled(True)
            elif self.label_Food4.text()== "Bingsoo":
                self.Frame_Bingsoo.setEnabled(True)
            elif self.label_Food4.text()== "Tiramisu":
                self.Frame_Tiramisu.setEnabled(True)
            elif self.label_Food4.text()== "Panna Cotta":
                self.Frame_Panna.setEnabled(True)
            elif self.label_Food4.text()== "Orange Juice":
                self.Frame_Orange.setEnabled(True)
            elif self.label_Food4.text()== "Smoothie":
                self.Frame_Smoothie.setEnabled(True)

        if self.label_Food5.text():
            self.Frame_5.setVisible(False)
            if self.label_Food5.text()== "Lasagna":
                self.Frame_Lasagna.setEnabled(True)
            elif self.label_Food5.text()== "Risol Mayo":
                self.Frame_Risol.setEnabled(True)
            elif self.label_Food5.text()== "Bulgogi":
                self.Frame_Bulgogi.setEnabled(True)
            elif self.label_Food5.text()== "Ayam Geprek":
                self.Frame_Ayam.setEnabled(True)
            elif self.label_Food5.text()== "Tteokbokki":
                self.Frame_Tteok.setEnabled(True)
            elif self.label_Food5.text()== "Bingsoo":
                self.Frame_Bingsoo.setEnabled(True)
            elif self.label_Food5.text()== "Tiramisu":
                self.Frame_Tiramisu.setEnabled(True)
            elif self.label_Food5.text()== "Panna Cotta":
                self.Frame_Panna.setEnabled(True)
            elif self.label_Food5.text()== "Orange Juice":
                self.Frame_Orange.setEnabled(True)
            elif self.label_Food5.text()== "Smoothie":
                self.Frame_Smoothie.setEnabled(True)
        pembayaran.clear()
        total1.clear()
        total2.clear()
        total3.clear()
        total4.clear()
        total5.clear()
        total1.append(0)
        total2.append(0)
        total3.append(0)
        total4.append(0)
        total5.append(0)








app = QApplication(sys.argv)
mainwindow = Resto()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMinimumWidth(1422)
widget.setMinimumHeight(1052)
widget.show()
app.exec()
