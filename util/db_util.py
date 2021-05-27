from util.db_pool import SQlitePool
import sqlite3


class FoodDatabase:

    @staticmethod
    def connect() -> object:
        pool = SQlitePool(factory=sqlite3.connect, database="database.db",
                          capacity=100, overflow=10, timeout=10)

        conn = pool.get_resource()

        return conn

    @staticmethod
    def create():
        try:
            connect = FoodDatabase().connect()
            c = connect.cursor()
            print("Berhasil membuat koneksi ke database")

            c.execute('''CREATE TABLE IF NOT EXISTS food
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             price INT NOT NULL,
             stock INT NOT NULL);''')
            print("....")
            print("\nBerhasil membuat tabel\n")
            connect.commit()
            connect.close()

        except sqlite3.Error:
            print("Gagal membuat database")
            raise

    @staticmethod
    def insert(name, price, stock):
        try:
            name.isalpha()
            connect = FoodDatabase().connect()
            c = connect.cursor()

            c.execute('''INSERT INTO food (name, price, stock) values (?, ?, ?)''',
                      [str(name), int(price), int(stock)])
            connect.commit()
            connect.close()
        except (AttributeError, ValueError):
            print("Invalid input! name should be alphabet, stock and price should be numeric")

    @staticmethod
    def delete(id):
        try:
            connect = FoodDatabase().connect()
            c = connect.cursor()

            c.execute("DELETE from food WHERE id=?", [int(id)])
            connect.commit()
            connect.close()
        except ValueError:
            print("id should be numeric")


    @staticmethod
    def get_info():
        connect = FoodDatabase().connect()
        c = connect.cursor()

        c.execute("SELECT * from food")
        info = c.fetchall()
        print("Daftar makanan dan minuman : ")
        for value in info:
            print(value)

        connect.close()
