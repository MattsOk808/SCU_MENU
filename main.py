from datetime import date,datetime,timedelta
from functions import *
from shared_vars import *
from parse_menu import parse_menu
import json
from recommendation import get_recommendation

NUMDAYS=7 #number of days that you can view after current day plus 1

try:
    with open("schedule.json","r") as old_schedule:
        raw_data=json.load(old_schedule)
        today=date.today()
        sorted_data = {
            d: [iteminfo.from_dict(meal) for meal in item] 
            for d, item in raw_data.items() 
            if datetime.strptime(d, "%Y-%m-%d").date() >= today
        }
        new_schedule_dict.clear()
        new_schedule_dict.update(sorted_data)
except FileNotFoundError:
    with open("schedule.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass
try:
    with open("ingredients.json","r") as ingredient_list:
        ingredient_dict.clear()
        ingredient_dict.update(json.load(ingredient_list))
except FileNotFoundError:
    with open("ingredients.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass
try:
    with open("favorites.json","r") as favorites:
        favorites_set.clear()
        favorites_set.update(set(json.load(favorites)))
except FileNotFoundError:
    with open("favorites.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass

cmd_num=None
dates=[]
commands=["Menu","Edit","Schedule","Ingredients","Favorites","Recomendation","Exit"]
edit_options_left=["Menu"]
edit_options_right=["Save and exit","Exit without saving"]

for i in range(NUMDAYS): #website only shows menu for previous day, current day, and up to 6 days in the future
    dates.append((date.today()+timedelta(days=i)).strftime("%Y-%m-%d"))
dates.append("Cancel")
while True:
    print_options(commands)
    cmd=numcheck(input("Enter command: "),len(commands))
    match cmd:
        case -2:
            print("Input not a number")
            continue
        case -1:
            print("Input out of range")
            continue
        case 1: #menu
            print_options(dates)
            n=numcheck(input("Select date: "),len(dates))
            if n == -2:
                print("Input not a number")
                continue
            if n == -1:
                print("Input out of range")
                continue
            if n==len(dates): #cancel
                continue
            d=dates[n-1]
            if d not in saved_menus:
                parse_menu(date=d)
            print_menu(date=d)
        case 2: #edit
            print_options(dates)
            n=numcheck(input("Select date: "),len(dates))
            if n==-2:
                print("Input not a number")
                continue
            if n==-1:
                print("Input out of range")
                continue
            if n==len(dates): #cancel
                continue
            d=dates[n-1]
            contains_info=True
            if d not in new_schedule_dict:
                new_schedule_dict[d]=[iteminfo("None","0.00"),iteminfo("None","0.00"),iteminfo("None","0.00")]
                contains_info=False
            if d not in saved_menus:
                parse_menu(date=d)
            prev_b=new_schedule_dict[d][0]
            prev_l=new_schedule_dict[d][1]
            prev_d=new_schedule_dict[d][2]
            mealtime=None
            while True:
                print_options(edit_options_left+get_times(d)+edit_options_right)
                option=numcheck(input("Select option: "),len(edit_options_left+get_times(d)+edit_options_right))
                match option:
                    case -2:
                        print("Input not a number")
                    case -1:
                        print("Input out of range")
                    case 1: #menu
                        print_menu(date=d)
                    case int() if option > 1 and option < 5: #editing a meal
                        mealtime=(edit_options_left+get_times(d)+edit_options_right)[option-1].lower()
                        while True:
                            restaurants=get_options(saved_menus[d][mealtime],["Cancel"])
                            print_options(restaurants)
                            option=numcheck(input("Select Restaurant: "),len(restaurants))
                            if option == -2:
                                print("Input not a number")
                            elif option == -1:
                                print("Input out of range")
                            elif option!=len(restaurants):
                                restaurant=restaurants[option-1]
                                meals=[]
                                for item in saved_menus[d][mealtime][restaurant]:
                                    meals.append(f"{item.name}: ${item.price}")
                                meals.append("Cancel")
                                print_options(meals)
                                option=numcheck(input("Select item: "),len(meals))
                                if option == -2:
                                    print("Input not a number")
                                elif option == -1:
                                    print("Input out of range")
                                elif option==len(meals):
                                    continue
                                else:
                                    item_num=option-1
                                    new_meal=update_schedule(d,mealtime,restaurant,item_num)
                                    contains_info=True
                                    print(f"Updated {mealtime} to {new_meal.name}")
                                    break
                            else:
                                break
                    case 5: #save and exit
                        if contains_info:
                            print(f"Updates: \n {prev_b.name} -> {new_schedule_dict[d][0].name}\n {prev_l.name} -> {new_schedule_dict[d][1].name}\n {prev_d.name} -> {new_schedule_dict[d][2].name}")
                        else:
                            print("No data detected. Not saving entry")
                            new_schedule_dict.pop(d)
                        break
                    case 6: #exit and don't save
                        if contains_info:
                            new_schedule_dict[d][0]=prev_b
                            new_schedule_dict[d][1]=prev_l
                            new_schedule_dict[d][2]=prev_d
                            print("Updates not saved")
                        else:
                            print("Updates not saved")
                            new_schedule_dict.pop(d)
                        break
        case 3: #schedule
            options=get_options(new_schedule_dict,["All","Cancel"])
            print_options(options)
            choice=numcheck(input("Select Date: "),len(options))
            if choice == -2:
                print("Input not a number")
            elif choice == -1:
                print("Input out of range")
            if choice==len(options)-1:
                for d in options[:-2]:
                    total_cost=0.0
                    info=new_schedule_dict[d]
                    meal_list=get_times(d)
                    print(f"{d}: ")
                    for i,meal in enumerate(info):
                        total_cost+=float(meal.price)
                        print(f"{meal_list[i].upper()}: {meal.name} - ${meal.price}")
                    print(f"Total Cost: ${total_cost}\n")
            elif choice==len(options):
                continue
            else:
                info=new_schedule_dict[options[choice-1]]
                print(f"{options[choice-1]}: ")
                total_cost=0.0
                meal_list=get_times(options[choice-1])
                for i,meal in enumerate(info):
                    total_cost+=float(meal.price)
                    print(f"{meal_list[i].upper()}: {meal.name} - ${meal.price}")
                print(f"Total Cost: ${total_cost}\n")
        case 4: #ingredients
            meals=[]
            for m in ingredient_dict:
                meals.append(m)
            meals.append("Cancel")
            print_options(meals)
            meal=input("Enter meal name or select option: ")
            check=numcheck(meal,len(meals))
            if check==-1:
                print("Input out of range")
            elif check==-2:
                if meal in ingredient_dict:
                    print(f"{meal}:\n {', '.join(ingredient_dict[meal])}")
                else:
                    print("Meal not found")
            elif check==len(meals):
                continue
            else:
                print(f"{meals[check-1]}: {', '.join(ingredient_dict[meals[check-1]])}")
        case 5: #favorites
            options=["Add","Remove","View","Cancel"]
            print_options(options)
            choice=numcheck(input("Select Option: "),len(options))
            if choice == -2:
                print("Input not a number")
            elif choice == -1:
                print("Input out of range")
            elif choice==1: #Add
                options=dates
                print_options(options)
                d=numcheck(input("Select Date: "),len(options))
                if d == -2:
                    print("Input not a number")
                elif d == -1:
                    print("Input out of range")
                elif d == len(options):
                    continue
                else:
                    d=dates[d-1]
                    if d not in saved_menus:
                        parse_menu(date=d)
                    meal_list=get_times(d)
                    options=get_times(d)+["Cancel"]
                    print_options(options)
                    m=numcheck(input("Select mealtime: "),len(options))
                    if m == -2:
                        print("Input not a number")
                    elif m == -1:
                        print("Input out of range")
                    elif m == len(options):
                        continue
                    else:
                        m=get_times(d)[m-1]
                        restaurants=get_options(saved_menus[d][m],["Cancel"])
                        print_options(restaurants)
                        r=numcheck(input("Select restaurant: "),len(restaurants))
                        if r == -2:
                            print("Input not a number")
                        elif r == -1:
                            print("Input out of range")
                        elif r == len(restaurants):
                            continue
                        else:
                            r=restaurants[r-1]
                            items=get_options([iteminfo.name for iteminfo in saved_menus[d][m][r]],["Cancel"])
                            print_options(items)
                            i=numcheck(input("Select item: "),len(items))
                            if i == -2:
                                print("Input not a number")
                            elif i == -1:
                                print("Input out of range")
                            elif i == len(items):
                                continue
                            else:
                                print(f"Added {saved_menus[d][m][r][i-1].name} to favorites\n")
                                favorites_set.add(saved_menus[d][m][r][i-1].name)
            elif choice==2: #Delete
                options=sorted(favorites_set)+["Cancel"]
                print_options(options)
                delete=numcheck(input("Select item: "),len(options))
                if delete == -2:
                    print("Input not a number")
                elif delete == -1:
                    print("Input out of range")
                elif delete == len(options):
                    continue
                else:
                    print(f"Removed {options[delete-1]} from favorites list")
                    favorites_set.remove(options[delete-1])
            elif choice==3: #View
                for i,favorite in enumerate(sorted(favorites_set),start=1):
                    print(f"[{i}] {favorite}")
                print("")
            else:
                continue
        case 6: #recommendation
            print_options(dates)
            n=numcheck(input("Select date: "),len(dates))
            if n == -2:
                print("Input not a number")
                continue
            if n == -1:
                print("Input out of range")
                continue
            if n==len(dates): #cancel
                continue
            d=dates[n-1]
            if d not in saved_menus:
                parse_menu(date=d)
            print(get_recommendation(favorites_set,ingredient_dict,saved_menus,d).text)
            continue #I'm not completely sure why but if you remove this continue and run out of request, after get_recommendations returns, the program stops reading inputs and gets stuck asking you for input
        case 7: #exit
            break

with open("schedule.json",'w') as new_schedule:
    json.dump(dict(new_schedule_dict),new_schedule,cls=EnhancedEncoder,indent=4)
with open("ingredients.json","w") as ingredient_list:
    temp_dict={}
    for d in new_schedule_dict:
        for meal,_ in enumerate(new_schedule_dict[d]):
            if new_schedule_dict[d][meal].name in ingredient_dict:
                temp_dict[new_schedule_dict[d][meal].name]=ingredient_dict[new_schedule_dict[d][meal].name]
    for meal in favorites_set:
        if meal not in temp_dict and meal in ingredient_dict:
            temp_dict[meal]=ingredient_dict[meal]
    json.dump(temp_dict,ingredient_list,indent=4)
with open("favorites.json","w") as favorites:
    json.dump(list(favorites_set),favorites,indent=4)

