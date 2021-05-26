from util.db_util import FoodDatabase
from util.order_util import OrderUtil

FoodDatabase.create()
OrderUtil.order("Lasagna", 2)