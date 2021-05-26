import sqlite3
from cuttlepool import CuttlePool


class SQlitePool(CuttlePool):
    def normalize_resource(self, resource):
        resource.row_factory = None

    def ping(self, resource):
        try:
            rv = resource.execute('SELECT 1').fetchall()
            return (1,) in rv
        except sqlite3.Error:
            return False
