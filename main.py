from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date,datetime
from sortedcontainers import SortedDict

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

url="https://scudining.cafebonappetit.com/cafe/marketplace-2/"

default_restaurant_list=set(["The Garden","The Spice Market","Simply Oasis","The Slice","The Slice","Globe","The Global Grill Lunch","The Global Grill Dinner","Soup","The Chef's Table","Chef's Tabel Dessert Night","Chef's Table Dessert Night","La Parilla Breakfast","Global Grill Breakfast","Stacks Deli","The Fire","La Parilla"])
default_meals=["breakfast","lunch","dinner"]


def print_menu(times=default_meals,restaurants=default_restaurant_list,date=""):
    page=urlopen(Request(url+date,headers=headers))
    html=page.read().decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    for time in times:
        m=soup.find("section", class_=["panel s-wrapper site-panel site-panel--daypart site-panel--daypart-even","panel s-wrapper site-panel site-panel--daypart"],id=time)
        if m != None:
            menus=m.find("div", class_="c-tab__content site-panel__daypart-tab-content tab-content- c-tab__content--active")
            print(time.upper()+"\n")
            for r in menus.find_all("h3", class_="site-panel__daypart-station-title"):
                if(r.get_text() in restaurants):
                    print(r.get_text())
                    print_items(r)
                    print("")
            menus=menus.find_next_sibling()
            for r in menus.find_all("h3", class_="site-panel__daypart-station-title"):
                if(r.get_text() in restaurants):
                    print(r.get_text())
                    print_items(r)
                    print("")

def print_items(restaurant):
    if(restaurant!=None):
        p=restaurant.parent
        for info in p.find_all("div", class_="site-panel__daypart-item-container"):
            print(info.find("button", class_="h4 site-panel__daypart-item-title").get_text(strip=True),end=" - ")
            for price_info in info.find_all("li",class_="price-item"):
                print(f"{price_info.find("span",class_="price-item__type").get_text(strip=True)} {price_info.find("span",class_="price-item__amount").get_text(strip=True)}",end = " ")
            print("")
        for item in p.find_next_siblings():
            cls=item.get('class')
            if(cls[0]=="site-panel__daypart-item"):
                print(item.find("button", class_="h4 site-panel__daypart-item-title").get_text(strip=True),end=" - ")
                for price_info in item.find_all("li",class_="price-item"):
                    print(f"{price_info.find("span",class_="price-item__type").get_text(strip=True)} {price_info.find("span",class_="price-item__amount").get_text(strip=True)}",end = " ")
                print("")
            else:
                break
    else:
        print("Restaurant not open")

"""
print_menu(["breakfast"],set(["La Parilla Breakfast","Globe"]))
print_menu(["lunch"],set(["The Chef's Table","The Global Grill Lunch"]))
print_menu(["dinner"],set(["The Fire","Simply Oasis"]))
"""

#date=YYYY-MM-DD
#print_menu(date="2026-04-16")
new_schedule_dict=SortedDict()
with open("schedule.txt","r") as old_schedule:
    for line in old_schedule:
        info=line.split(",")
        d=datetime.strptime(info[0],"%Y-%m-%d").date()
        if d>=date.today():
            new_schedule_dict[info[0]]=info[1:]
cmd=None
while cmd != "exit":
    cmd=input("Enter command\n")
    if cmd=="date":
        d=input("Enter date\n") #need to add valid date checking
        if d in new_schedule_dict:
            meals=new_schedule_dict[d]
            if meals!=None:
                for i,meal in enumerate(meals):
                    print(f"{default_meals[i]}:{meal}")
        else:
            print("Entry not found")
    elif cmd=="edit":
        d=input("Enter date\n")
        if d not in new_schedule_dict:
            new_schedule_dict[d]=["None","None","None\n"]
        prev_b=new_schedule_dict[d][0]
        prev_l=new_schedule_dict[d][1]
        prev_d=new_schedule_dict[d][2]
        mealtime=None
        while True:
            mealtime=input("Enter mealtime to edit (all lowercase) or done to finish editing\n")
            if mealtime=="breakfast":
                new_schedule_dict[d][0]=input("Enter new meal\n")
            elif mealtime=="lunch":
                new_schedule_dict[d][1]=input("Enter new meal\n")
            elif mealtime=="dinner":
                new_schedule_dict[d][2]=input("Enter new meal\n")+"\n"
            elif mealtime=="done":
                break
            else:
                print("Invalid mealtime")
        print(f"Updates: \n {prev_b} -> {new_schedule_dict[d][0]}\n {prev_l} -> {new_schedule_dict[d][1]}\n {prev_d[:-1]} -> {new_schedule_dict[d][2][:-1]}")
    elif cmd=="schedule":
        for entry in new_schedule_dict:
            info=new_schedule_dict[entry]
            print(f"{entry}: ")
            for i,meal in enumerate(info):
                print(f"{default_meals[i].upper()}: {meal}")
    elif cmd=="menu":
        print_menu()
with open("schedule.txt","w") as new_schedule:
    for entry in new_schedule_dict:
        info=new_schedule_dict[entry]
        new_entry=f"{entry}"
        for meal in info:
            new_entry = new_entry+f",{meal}"
        new_schedule.write(new_entry)
