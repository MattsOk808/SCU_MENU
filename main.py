from datetime import date,datetime,timedelta
from shared.commands import *
import json

NUMDAYS=7 #number of days that you can view after current day plus 1

try:
    with open("shared/schedule.json","r") as old_schedule:
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
    with open("shared/schedule.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass
try:
    with open("shared/ingredients.json","r") as ingredient_list:
        ingredient_dict.clear()
        ingredient_dict.update(json.load(ingredient_list))
except FileNotFoundError:
    with open("shared/ingredients.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass
try:
    with open("shared/favorites.json","r") as fav:
        favorites_set.clear()
        favorites_set.update(set(json.load(fav)))
except FileNotFoundError:
    with open("shared/favorites.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass
try:
    with open("shared/allergies_and_restrictions.json","r") as ar:
        allergies_and_restrictions.clear()
        allergies_and_restrictions.update(set(json.load(ar)))
except FileNotFoundError:
    with open("shared/allergies_and_restrictions.json","w") as temp:
        pass
except json.JSONDecodeError:
    pass

cmd_num=None
commands=["Menu","Edit","Schedule","Ingredients","Favorites","Allergies/Dietary Restrictions","Exit"]

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
            menu()
        case 2: #edit
            edit()
        case 3: #schedule
            schedule()
        case 4: #ingredients
            ingredients()
        case 5: #favorites
            favorites()
        case 6: #allergies
            allergies()
        case 7: #exit
            break

with open("shared/schedule.json",'w') as new_schedule:
    json.dump(dict(new_schedule_dict),new_schedule,cls=EnhancedEncoder,indent=4)
with open("shared/ingredients.json","w") as ingredient_list:
    temp_dict={}
    for d in new_schedule_dict:
        for meal,_ in enumerate(new_schedule_dict[d]):
            if new_schedule_dict[d][meal].name in ingredient_dict:
                temp_dict[new_schedule_dict[d][meal].name]=ingredient_dict[new_schedule_dict[d][meal].name]
    for meal in favorites_set:
        if meal not in temp_dict and meal in ingredient_dict:
            temp_dict[meal]=ingredient_dict[meal]
    json.dump(temp_dict,ingredient_list,indent=4)
with open("shared/favorites.json","w") as favorites:
    json.dump(sorted(list(favorites_set)),favorites,indent=4)
with open("shared/allergies_and_restrictions.json","w") as ar:
    json.dump(sorted(list(allergies_and_restrictions)),ar,indent=4)

