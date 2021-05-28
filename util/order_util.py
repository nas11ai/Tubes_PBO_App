from util.db_util import FoodDatabase


class OrderUtil:

    @staticmethod
    def order(name, jumlah):
        try:
            name.isalpha() and int(jumlah)
            connect = FoodDatabase.connect()
            c = connect.cursor()
            c.execute("SELECT name, price, stock from food WHERE name=?", [str(name)])
            meal = c.fetchone()
            list_meal = list(meal)
            print(list_meal)
            if jumlah <= 0:
                print("Harap memasukkan jumlah porsi dengan benar")
            elif list_meal[2] == 0:
                print("Mohon maaf. Makanan/Minuman ini sudah habis")
            elif list_meal[2] < jumlah:
                print(f"Porsi tidak cukup! Sisa porsi = {list_meal[2]}")
            else:
                print(f"{list_meal[0]} = {int(jumlah)} x Rp {list_meal[1]} = Rp {list_meal[1]*int(jumlah)}")
                list_meal[2] -= int(jumlah)
                print(list_meal)
                c.execute("UPDATE food SET stock = ? WHERE name = ?", [list_meal[2], name])
                connect.commit()
                connect.close()
        except (AttributeError, ValueError):
            print("Masukkan nama makanan dan jumlah porsi yang anda inginkan dengan benar!")
