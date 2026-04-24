from sortedcontainers import SortedDict
from collections import defaultdict

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

base_url="https://scudining.cafebonappetit.com/cafe/marketplace-2/"

default_restaurant_list=set(["The Garden","The Spice Market","Simply Oasis","The Slice","The Slice","The Global Grill","Globe","The Global Grill Lunch","The Global Grill Dinner","Soup","The Chef's Table","Chef's Tabel Dessert Night","Chef's Table Dessert Night","La Parilla Breakfast","Global Grill Breakfast","Stacks Deli","The Fire","La Parilla"])
default_meals=["breakfast","lunch","dinner"]
saved_menus=defaultdict(lambda: defaultdict(lambda: defaultdict(list)))    

new_schedule_dict=SortedDict() 

class iteminfo:
    def __init__(self,name,price):
        self.name=name
        self.price=price