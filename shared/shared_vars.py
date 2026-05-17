from sortedcontainers import SortedDict
from collections import defaultdict
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

base_url="https://scudining.cafebonappetit.com/cafe/marketplace-2/"

default_restaurant_list=set(["The Garden","The Spice Market","Simply Oasis","The Slice","The Slice","The Global Grill","Globe","The Global Grill Lunch","The Global Grill Dinner","Soup","The Chef's Table","Chef's Tabel Dessert Night","Chef's Table Dessert Night","Stacks Deli","The Fire","La Parilla"])
weekday_meals=["breakfast","lunch","dinner"]
weekenend_meals=["brunch","lunch","dinner"]
saved_menus=defaultdict(lambda: defaultdict(lambda: defaultdict(list)))    

new_schedule_dict=SortedDict() 
ingredient_dict=SortedDict()
favorites_set=set()
allergies_and_restrictions=set()

dates=[]

class iteminfo:
    def __init__(self,name,price,restaurant):
        self.name=name
        self.price=price
        self.restaurant=restaurant

    def to_json(self):
        return {"name": self.name, "price": float(self.price), "restaurant": self.restaurant}
    
    @staticmethod
    def from_dict(d):
        if "name" in d and "price" in d and "restaurant" in d:
            return iteminfo(d["name"],d["price"],d["restaurant"])
        return d

class EnhancedEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,SortedDict):
            return dict(obj)
        if isinstance(obj,iteminfo):
            return obj.to_json()
        return super().default(obj)
    
