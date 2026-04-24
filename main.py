from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date,datetime
from functions import *
from shared_vars import *
from parse_menu import parse_menu


with open("schedule.txt","r") as old_schedule:
    for line in old_schedule:
        line=line[:-1]
        d=line[:10] #first 10 chars are the date
        if datetime.strptime(d,"%Y-%m-%d").date()>=date.today():
            info=[]
            for item in line[11:].split(','):
                name,price=item.split(':')
                info.append(iteminfo(name,price))
            new_schedule_dict[d]=info
cmd=None
while cmd != "exit":
    cmd=input("Enter command: ")
    if cmd=="menu":
        d=input("Enter date (YYYY-MM-DD) or 'today'\n")
        if d=="today":
            d=f"{date.today()}"
        else:
            try:
                datetime.strptime(d,"%Y-%m-%d").date()
            except:
                print("Invalid date")
                continue
        if d not in saved_menus:
            parse_menu(date=d)
        print_menu(date=d)
    elif cmd=="edit":
        d=input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(d,"%Y-%m-%d").date()   
            if d not in new_schedule_dict:
                new_schedule_dict[d]=[iteminfo("None",0.00),iteminfo("None",0.00),iteminfo("None",0.00)]
            if d not in saved_menus:
                parse_menu(date=d)
            prev_b=new_schedule_dict[d][0]
            prev_l=new_schedule_dict[d][1]
            prev_d=new_schedule_dict[d][2]
            mealtime=None
            while True:
                mealtime=input("Enter desired mealtime to edit (all lowercase), 'menu' to view menu, or 'done' to finish editing: ")
                if mealtime=="menu":
                    print_menu(date=d)
                elif mealtime=="breakfast" or mealtime=="lunch" or mealtime=="dinner":
                    while True:
                        restaurant=input("Enter restaurant or 'cancel': ")
                        if restaurant!="cancel":
                            if restaurant in saved_menus[d][mealtime]:
                                print_menu(times=[mealtime],restaurants=[restaurant],date=d)
                                item_num=input("Enter item number or 'cancel': ")
                                if item_num!="cancel":
                                    item_num=int(item_num)
                                    if item_num<=0 or item_num>len(saved_menus[d][mealtime][restaurant]):
                                        print("Invalid item number")
                                    else:
                                        update_schedule(d,mealtime,restaurant,item_num-1)
                                        break
                            else:
                                print("Restaurant name incorrect or not open")
                        else:
                            break
                elif mealtime=="done":
                    break
                else:
                    print("Invalid input")
            print(f"Updates: \n {prev_b.name} -> {new_schedule_dict[d][0].name}\n {prev_l.name} -> {new_schedule_dict[d][1].name}\n {prev_d.name} -> {new_schedule_dict[d][2].name}")
        except ValueError:
            print("Invalid date")
    elif cmd=="schedule":
        type=input("Enter 'full' for entire schedule or date (YYYY-MM-DD) for specific day: ")
        if type=="full":
            for date in new_schedule_dict:
                total_cost=0.0
                info=new_schedule_dict[date]
                print(f"{date}: ")
                for i,meal in enumerate(info):
                    total_cost+=float(meal.price)
                    print(f"{default_meals[i].upper()}: {meal.name} - ${meal.price}")
                print(f"Total Cost: ${total_cost}\n")
        else:
            try:
                datetime.strptime(type,"%Y-%m-%d").date()   
                info=new_schedule_dict[type]
                total_cost=0.0
                print(f"{type}: ")
                for i,meal in enumerate(info):
                    total_cost+=float(meal.price)
                    print(f"{default_meals[i].upper()}: {meal.name} - ${meal.price}")
                print(f"Total Cost: ${total_cost}\n")
            except ValueError:
                print("Invalid date")


with open("schedule.txt","w") as new_schedule:
    for date in new_schedule_dict:
        new_entry=f"{date}"
        for item in new_schedule_dict[date]:
            new_entry+=f",{item.name}:{item.price}"
        new_schedule.write(new_entry+"\n")

