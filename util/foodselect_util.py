from util.db_util import FoodDatabase


class FoodSelect:

    @staticmethod
    def select_stock(name):
        try:
            name.isalpha()
            connect = FoodDatabase.connect()
            c = connect.cursor()
            c.execute("SELECT stock from food WHERE name=?", [name])
            stock = c.fetchone()
            return stock[0]
        except AttributeError:
            print("Invalid input! name should be alphabet")

    @staticmethod
    def select_price(name):
        try:
            name.isalpha()
            connect = FoodDatabase.connect()
            c = connect.cursor()
            c.execute("SELECT price from food WHERE name=?", [name])
            price = c.fetchone()
            return price[0]
        except AttributeError:
            print("Invalid input! name should be alphabet")