from util.db_util import FoodDatabase
from util.order_util import OrderUtil
from util.foodselect_util import FoodSelect

FoodDatabase.create()
FoodSelect.select_price("Lasagna")
