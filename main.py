from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date,datetime
from sortedcontainers import SortedDict

"""
KNOWN BUGS
    restaurants printed twice due to multiple pages -> can't update schedule with items not on the first page
    cannot add items from Globe (breakfast)
"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

url="https://scudining.cafebonappetit.com/cafe/marketplace-2/"

default_restaurant_list=set(["The Garden","The Spice Market","Simply Oasis","The Slice","The Slice","The Global Grill","Globe","The Global Grill Lunch","The Global Grill Dinner","Soup","The Chef's Table","Chef's Tabel Dessert Night","Chef's Table Dessert Night","La Parilla Breakfast","Global Grill Breakfast","Stacks Deli","The Fire","La Parilla"])
default_meals=["breakfast","lunch","dinner"]
saved_menus={}

def print_menu(times=default_meals,restaurants=default_restaurant_list,date=""):
    soup=saved_menus[date]
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
    names,prices=get_item_infos(restaurant)
    for i in range(len(names)):
        print(f"{i+1}. {names[i]} - ",end="")
        for p1,p2 in prices[i]:
            print(f"{p1} {p2}",end=" ")
        print("")

def get_item_infos(restaurant):
    if(restaurant!=None):
        names=[]
        prices=[]
        p=restaurant.parent
        for info in p.find_all("div", class_="site-panel__daypart-item-container"):
            names.append(info.find("button", class_="h4 site-panel__daypart-item-title").get_text(strip=True))
            price=[]
            for price_info in info.find_all("li",class_="price-item"):
                price.append([price_info.find("span",class_="price-item__type").get_text(strip=True), price_info.find("span",class_="price-item__amount").get_text(strip=True)])
            prices.append(price)
        for item in p.find_next_siblings():
            cls=item.get('class')
            if(cls[0]=="site-panel__daypart-item"):
                price=[]
                names.append(item.find("button", class_="h4 site-panel__daypart-item-title").get_text(strip=True))
                for price_info in item.find_all("li",class_="price-item"):
                    price.append([price_info.find("span",class_="price-item__type").get_text(strip=True), price_info.find("span",class_="price-item__amount").get_text(strip=True)])
                prices.append(price)
            else:
                break
        return names,prices
    else:
        return None,None
def get_restaurant(date,mealtime,name):
    soup=saved_menus[date]
    if name=="The Global Grill":
        if mealtime=="breakfast":
            name="Global Grill Breakfast"
        else:
            name=name+" "+mealtime.capitalize()
    m=soup.find("section", class_=["panel s-wrapper site-panel site-panel--daypart site-panel--daypart-even","panel s-wrapper site-panel site-panel--daypart"],id=mealtime)
    menus=m.find("div", class_="c-tab__content site-panel__daypart-tab-content tab-content- c-tab__content--active")
    return menus.find("h3", class_="site-panel__daypart-station-title",string=name)

def update_meal(mealnum):
    r=input("Enter restaurant\n")
    if r in default_restaurant_list:
        n=input("Enter item number\n")
        try:
            n=int(n)
            if mealnum==0:
                names,_=get_item_infos(get_restaurant(d,"breakfast",r))
            elif mealnum==1:
                names,_=get_item_infos(get_restaurant(d,"lunch",r))
            else:
                names,_=get_item_infos(get_restaurant(d,"dinner",r))
            new_schedule_dict[d][mealnum]=names[n-1]
        except ValueError:
            print("Input not a number")
        except IndexError:
            print("Item number does not exist")
    else:
        print("Restaurant not found")

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
        d=input("Enter date\n") 
        if d in new_schedule_dict:
            meals=new_schedule_dict[d]
            if meals!=None:
                for i,meal in enumerate(meals):
                    print(f"{default_meals[i]}:{meal}")
        else:
            print("Entry not found")
    elif cmd=="edit":
        d=input("Enter date\n")
        try:
            test=datetime.strptime(d,"%Y-%m-%d").date()   
            if d not in new_schedule_dict:
                new_schedule_dict[d]=["None","None","None\n"]
            if d not in saved_menus:
                page=urlopen(Request(url+d,headers=headers))
                html=page.read().decode("utf-8")
                saved_menus[d]=BeautifulSoup(html,"html.parser")
            prev_b=new_schedule_dict[d][0]
            prev_l=new_schedule_dict[d][1]
            prev_d=new_schedule_dict[d][2]
            mealtime=None
            while True:
                mealtime=input("Enter desired mealtime to edit (all lowercase), 'menu' to view menu, or 'done' to finish editing\n")
                if mealtime=="menu":
                    print_menu(date=d)
                elif mealtime=="breakfast":
                    update_meal(0)
                elif mealtime=="lunch":
                    update_meal(1)
                elif mealtime=="dinner":
                    update_meal(2)
                elif mealtime=="done":
                    break
                else:
                    print("Invalid mealtime")
            print(f"Updates: \n {prev_b} -> {new_schedule_dict[d][0]}\n {prev_l} -> {new_schedule_dict[d][1]}\n {prev_d[:-1]} -> {new_schedule_dict[d][2][:-1]}")
        except:
            print("Invalid date")
    elif cmd=="schedule":
        for entry in new_schedule_dict:
            info=new_schedule_dict[entry]
            print(f"{entry}: ")
            for i,meal in enumerate(info):
                print(f"{default_meals[i].upper()}: {meal}")
    elif cmd=="menu":
        d=input("Enter date (YYYY-MM-DD) or 'today'\n")
        if d=="today":
            d=f"{date.today()}"
            if d not in saved_menus:
                page=urlopen(Request(url,headers=headers))
                html=page.read().decode("utf-8")
                saved_menus[d]=BeautifulSoup(html,"html.parser")
        elif d not in saved_menus:
            try:
                test=datetime.strptime(d,"%Y-%m-%d").date()
                page=urlopen(Request(url+d,headers=headers))
                html=page.read().decode("utf-8")
                saved_menus[d]=BeautifulSoup(html,"html.parser")
            except:
                print("Invalid date")
                continue
        print_menu(date=d)
with open("schedule.txt","w") as new_schedule:
    for entry in new_schedule_dict:
        info=new_schedule_dict[entry]
        new_entry=f"{entry}"
        for meal in info:
            new_entry = new_entry+f",{meal}"
        new_schedule.write(new_entry)
