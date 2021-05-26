from util.db_util import FoodDatabase


class OrderUtil:

    @staticmethod
    def order(name, jumlah):
        connect = FoodDatabase.connect()
        c = connect.cursor()
        c.execute("SELECT name, price, stock from food WHERE name=?", [name])
        meal = c.fetchone()
        list_meal = list(meal)
        print(list_meal)
        if list_meal[2] < jumlah:
            print(f"Porsi tidak cukup! Sisa porsi = {list_meal[2]}")
        else:
            print(f"{list_meal[0]} = {int(jumlah)} x Rp {list_meal[1]} = Rp {list_meal[1]*int(jumlah)}")
            #list_meal[2] -= int(jumlah)
            print(list_meal)
