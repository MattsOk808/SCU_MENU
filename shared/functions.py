from datetime import date,datetime
from shared.shared_vars import saved_menus,new_schedule_dict,favorites_set,weekday_meals,weekenend_meals,ingredient_dict,allergies_and_restrictions
from colorama import Fore,Style,init

default_restaurant_list=set(["The Garden","The Spice Market","Simply Oasis","The Slice","The Global Grill","Soup","The Chef's Table","Chef's Tabel Dessert Night","Chef's Table Dessert Night","Stacks Deli","The Fire","La Parilla"])

init(autoreset=True) 

def get_times(d):
    if datetime.strptime(d,"%Y-%m-%d").weekday()>=5:
        return weekenend_meals
    else:
        return weekday_meals

def print_menu(times=weekday_meals,date=f"{date.today()}"):
    times=get_times(date)
    for time in times:
        if time in saved_menus[date]:
            print(f"{time.upper()}")
            for restaurant in saved_menus[date][time]:
                if restaurant in saved_menus[date][time]:
                    print(restaurant)
                    for i,item in enumerate(saved_menus[date][time][restaurant],start=1):
                        for ingredient in ingredient_dict[item.name]:
                            if ingredient in allergies_and_restrictions:
                                print(f"{[i]} {Style.BRIGHT}{Fore.RED}{item.name}: ${item.price:.2f}{Style.RESET_ALL}")
                                break
                        else:
                            if item.name in favorites_set:
                                print(f"{[i]} {Style.BRIGHT}{Fore.YELLOW}{item.name}: ${item.price:.2f}{Style.RESET_ALL}")
                            else:
                                print(f"{[i]} {item.name}: ${item.price:.2f}")
                    print("")
def update_schedule(d,mealtime,restaurant,item_num):
    if mealtime=="breakfast" or mealtime=="brunch":
        new_schedule_dict[d][0]=saved_menus[d][mealtime][restaurant][item_num]
        return new_schedule_dict[d][0]
    elif mealtime=="lunch":
        new_schedule_dict[d][1]=saved_menus[d][mealtime][restaurant][item_num]
        return new_schedule_dict[d][1]
    elif mealtime=="dinner":
        new_schedule_dict[d][2]=saved_menus[d][mealtime][restaurant][item_num]
        return new_schedule_dict[d][2]
def numcheck(n,limit): #function to check if the user input is a number and with the range [1,limit]. Returns -1 if out of range and -2 if not a number
    try:
        n=int(n)
        if n<1 or n>limit:
            return -1
        return n
    except ValueError:
        return -2
    
def print_options(options):
    for i,options in enumerate(options,start=1):
        print(f"[{i}] {options}")

def get_options(optionlist,addional_options=[]):
    options=[]
    for option in optionlist:
        options.append(option)
    return options+addional_options
