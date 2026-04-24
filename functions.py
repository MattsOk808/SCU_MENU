from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date,datetime
from sortedcontainers import SortedDict
import parse_menu as parse
from shared_vars import saved_menus,new_schedule_dict


default_restaurant_list=set(["The Garden","The Spice Market","Simply Oasis","The Slice","The Global Grill","Soup","The Chef's Table","Chef's Tabel Dessert Night","Chef's Table Dessert Night","Stacks Deli","The Fire","La Parilla"])
default_meals=["breakfast","lunch","dinner"]

def print_menu(times=default_meals,restaurants=default_restaurant_list,date=f"{date.today()}"):
    for time in times:
        for restaurant in restaurants:
            if restaurant in saved_menus[date][time]:
                print(restaurant)
                i=1
                for item in saved_menus[date][time][restaurant]:
                    print(f"{i}. {item.name}: ${item.price}")
                    i+=1
                print("")
def update_schedule(d,mealtime,restaurant,item_num):
    if mealtime=="breakfast":
        new_schedule_dict[d][0]=saved_menus[d][mealtime][restaurant][item_num]
    elif mealtime=="lunch":
        new_schedule_dict[d][1]=saved_menus[d][mealtime][restaurant][item_num]
    elif mealtime=="dinner":
        new_schedule_dict[d][2]=saved_menus[d][mealtime][restaurant][item_num]
    