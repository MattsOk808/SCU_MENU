from shared.functions import *
from shared.shared_vars import *
from shared.parse_menu import *

edit_options_left=["View Menu","View Current Schedule"]
edit_options_right=["Save and exit","Exit without saving"]

def menu():
    print_options(dates)
    n=numcheck(input("Select date: "),len(dates))
    if n == -2:
        print("Input not a number")
        return
    if n == -1:
        print("Input out of range")
        return
    if n==len(dates): #cancel
        return
    d=dates[n-1]
    if d not in saved_menus:
        parse_menu(date=d)
        parse_fresh_bytes(date=d)
    print_menu(date=d)

def edit():
    print_options(dates)
    n=numcheck(input("Select date: "),len(dates))
    if n==-2:
        print("Input not a number")
        return
    if n==-1:
        print("Input out of range")
        return
    if n==len(dates): #cancel
        return
    d=dates[n-1]
    contains_info=True
    if d not in new_schedule_dict:
        new_schedule_dict[d]=[iteminfo("None",0.00,"None"),iteminfo("None",0.00,"None"),iteminfo("None",0.00,"None")]
        contains_info=False
    if d not in saved_menus:
        parse_menu(date=d)
        parse_fresh_bytes(date=d)
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
            case 2: #view current
                info=new_schedule_dict[d]
                print(f"{d}: ")
                total_cost=0.00
                meal_list=get_times(d)
                for i,meal in enumerate(info):
                    total_cost+=float(meal.price)
                    print(f"{meal_list[i].upper()}: {meal.name} - ${meal.price:.2f},    Restaurant: {meal.restaurant}")
                print(f"Total Cost: ${total_cost:.2f}\n")
            case int() if option > 2 and option < 5: #editing a meal
                mealtime=(edit_options_left+get_times(d)+edit_options_right)[option-1].lower()
                while True:
                    restaurants=get_options(saved_menus[d][mealtime],["Delete","Cancel"])
                    print_options(restaurants)
                    option=numcheck(input("Select Restaurant: "),len(restaurants))
                    if option == -2:
                        print("Input not a number")
                    elif option == -1:
                        print("Input out of range")
                    elif option == len(restaurants)-1:
                        if mealtime=="breakfast" or mealtime=="brunch":
                            t=0
                        elif mealtime=="lunch":
                            t=1
                        elif mealtime=="dinner":
                            t=2
                        print(f"Deleted meal for {mealtime}")
                        new_schedule_dict[d][t]=iteminfo("None",0.00,"None")
                        break
                    elif option == len(restaurants):
                        break
                    else:
                        restaurant=restaurants[option-1]
                        meals=[]
                        for item in saved_menus[d][mealtime][restaurant]:
                            meals.append(f"{item.name}: ${item.price:.2f}")
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
            case 6: #save and exit
                if contains_info:
                    print(f"Updates: \n {prev_b.name} -> {new_schedule_dict[d][0].name}\n {prev_l.name} -> {new_schedule_dict[d][1].name}\n {prev_d.name} -> {new_schedule_dict[d][2].name}")
                else:
                    print("No data detected. Not saving entry")
                    new_schedule_dict.pop(d)
                break
            case 7: #exit and don't save
                if contains_info:
                    new_schedule_dict[d][0]=prev_b
                    new_schedule_dict[d][1]=prev_l
                    new_schedule_dict[d][2]=prev_d
                    print("Updates not saved")
                else:
                    print("Updates not saved")
                    new_schedule_dict.pop(d)
                break
def schedule():
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
                print(f"{meal_list[i].upper()}: {meal.name} - ${meal.price:.2f},    Restaurant: {meal.restaurant}")
            print(f"Total Cost: ${total_cost:.2f}\n")
    elif choice==len(options):
        return
    else:
        info=new_schedule_dict[options[choice-1]]
        print(f"{options[choice-1]}: ")
        total_cost=0.00
        meal_list=get_times(options[choice-1])
        for i,meal in enumerate(info):
            total_cost+=float(meal.price)
            print(f"{meal_list[i].upper()}: {meal.name} - ${meal.price:.2f},    Restaurant: {meal.restaurant}")
        print(f"Total Cost: ${total_cost:.2f}\n")

def ingredients():
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
        return
    else:
        print(f"{meals[check-1]}: {', '.join(ingredient_dict[meals[check-1]])}")

def favorites():
    options1=["Add","Remove","View","Cancel"]
    while True:
        print_options(options1)
        choice=numcheck(input("Select Option: "),len(options1))
        if choice == -2:
            print("Input not a number")
        elif choice == -1:
            print("Input out of range")
        elif choice==1: #Add
            options2=dates
            while True:
                print_options(options2)
                d=numcheck(input("Select Date: "),len(options2))
                if d == -2:
                    print("Input not a number")
                elif d == -1:
                    print("Input out of range")
                elif d == len(options2):
                    break
                else:
                    d=dates[d-1]
                    if d not in saved_menus:
                        parse_menu(date=d)
                        parse_fresh_bytes(date=d)
                    options3=get_times(d)+["Cancel"]
                    while True:
                        print_options(options3)
                        m=numcheck(input("Select mealtime: "),len(options3))
                        if m == -2:
                            print("Input not a number")
                        elif m == -1:
                            print("Input out of range")
                        elif m == len(options3):
                            break
                        else:
                            m=get_times(d)[m-1]
                            restaurants=get_options(saved_menus[d][m],["Cancel"])
                            while True:
                                print_options(restaurants)
                                r=numcheck(input("Select restaurant: "),len(restaurants))
                                if r == -2:
                                    print("Input not a number")
                                elif r == -1:
                                    print("Input out of range")
                                elif r == len(restaurants):
                                    break
                                else:
                                    r=restaurants[r-1]
                                    items=get_options([iteminfo.name for iteminfo in saved_menus[d][m][r]],["Cancel"])
                                    while True:
                                        print_options(items)
                                        i=numcheck(input("Select item: "),len(items))
                                        if i == -2:
                                            print("Input not a number")
                                        elif i == -1:
                                            print("Input out of range")
                                        elif i == len(items):
                                            break
                                        else:
                                            if saved_menus[d][m][r][i-1].name in favorites_set:
                                                print(f"{saved_menus[d][m][r][i-1].name} already in favorites\n")
                                            else:
                                                print(f"Added {saved_menus[d][m][r][i-1].name} to favorites\n")
                                                favorites_set.add(saved_menus[d][m][r][i-1].name)
                                                return
        elif choice==2: #Delete
            options=sorted(favorites_set)+["Cancel"]
            while True:
                print_options(options)
                delete=numcheck(input("Select item: "),len(options))
                if delete == -2:
                    print("Input not a number")
                elif delete == -1:
                    print("Input out of range")
                elif delete == len(options):
                    break
                else:
                    print(f"Removed {options[delete-1]} from favorites list")
                    favorites_set.remove(options[delete-1])
                    return
        elif choice==3: #View
            for i,favorite in enumerate(sorted(favorites_set),start=1):
                print(f"[{i}] {favorite}")
            print("")
            return
        else:
            return

def allergies():
    options=["Add","Remove","View","Exit"]
    while True:
        print_options(options)
        choice=numcheck(input("Choose option: "),len(options))
        match choice:
            case -2:
                print("Input not a number")
            case -1:
                print("Input out of range")
            case 1:
                while True:
                    new_item=input("Enter allergy/dietary restriction or any number to cancel: ")
                    if numcheck(new_item,0)==-2:
                        if new_item in allergies_and_restrictions:
                            print(f"{new_item} already in allergy/dietary restrictions\n")
                        else:
                            print(f"Added {new_item} to allergy/dietary restrictions\n")
                            allergies_and_restrictions.add(new_item)
                            return
                    else:
                        break
            case 2:
                options2=sorted(allergies_and_restrictions)+["Cancel"]
                print_options(options2)
                remove_item=numcheck(input("Enter allergy/dietary restriction to remove: "),len(options2))
                if remove_item == -2:
                    print("Input not a number")
                elif remove_item == -1:
                    print("Input out of range")
                elif remove_item == len(options2):
                    continue
                else:   
                    print(f"Removed {options2[remove_item-1]} from allergy/dietary restrictions\n")
                    allergies_and_restrictions.remove(options2[remove_item-1])
                    continue
            case 3:
                print("ALLERGIES AND DIETARY RESTRICTIONS")
                for i,adr in enumerate(sorted(allergies_and_restrictions),start=1):
                    print(f"[{i}] {adr}")
                print("")
            case 4:
                return