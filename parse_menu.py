from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date
from shared_vars import saved_menus,base_url,default_meals,headers,iteminfo

def parse_menu(url=base_url,date=f"{date.today()}"):
    page=urlopen(Request(url+date,headers=headers))
    html=page.read().decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    for time in default_meals:
        m=soup.find("section", class_=["panel s-wrapper site-panel site-panel--daypart site-panel--daypart-even","panel s-wrapper site-panel site-panel--daypart"],id=time)
        if m!=None:
            menu=m.find("div", class_="c-tab__content site-panel__daypart-tab-content tab-content- c-tab__content--active")
            for restaurant in menu.find_all("div", class_="station-title-inline-block"):
                restaurant_name=restaurant.find("h3",class_="site-panel__daypart-station-title").get_text()
                if restaurant_name=="The Global Grill Lunch" or restaurant_name=="The Global Grill Dinner" or restaurant_name=="Global Grill Breakfast" or restaurant_name=="Globe":
                    restaurant_name="The Global Grill"
                elif restaurant_name=="La Parilla Breakfast":
                    restaurant_name="La Parilla"
                for item in restaurant.find_all("div", class_="site-panel__daypart-item-container"):
                    item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                    item_price=item.find("span",class_="price-item__amount")
                    if item_name!=None and item_price!=None:
                        saved_menus[date][time][restaurant_name].append(iteminfo(item_name.get_text(strip=True),item_price.get_text(strip=True)))
                for sibling in restaurant.find_next_siblings(): #if a restaurant has more than 2 items all remaining items are stored in a slightly different format
                    cls=sibling.get("class")
                    if(cls[0]!="site-panel__daypart-item"): 
                        break
                    for item in sibling.find_all("div", class_="site-panel__daypart-item-container"):
                        item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                        item_price=item.find("span",class_="price-item__amount")
                        if item_name!=None and item_price!=None:
                            saved_menus[date][time][restaurant_name].append(iteminfo(item_name.get_text(strip=True),item_price.get_text(strip=True)))
            menu=m.find("div",class_="c-tab__content site-panel__daypart-tab-content tab-content-") #Checking secondary tab for items 
            for restaurant in menu.find_all("div", class_="station-title-inline-block"):
                restaurant_name=restaurant.find("h3",class_="site-panel__daypart-station-title").get_text()
                if restaurant_name=="The Global Grill Lunch" or restaurant_name=="The Global Grill Dinner" or restaurant_name=="Global Grill Breakfast" or restaurant_name=="Globe":
                    restaurant_name="The Global Grill"
                elif restaurant_name=="La Parilla Breakfast":
                    restaurant_name="La Parilla"
                for item in restaurant.find_all("div", class_="site-panel__daypart-item-container"):
                    item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                    item_price=item.find("span",class_="price-item__amount")
                    if item_name!=None and item_price!=None:
                        saved_menus[date][time][restaurant_name].append(iteminfo(item_name.get_text(strip=True),item_price.get_text(strip=True)))
                for sibling in restaurant.find_next_siblings(): #if a restaurant has more than 2 items all remaining items are stored in a slightly different format
                    cls=sibling.get("class")
                    if(cls[0]!="site-panel__daypart-item"): 
                        break
                    for item in sibling.find_all("div", class_="site-panel__daypart-item-container"):
                        item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                        item_price=item.find("span",class_="price-item__amount")
                        if item_name!=None and item_price!=None:
                            saved_menus[date][time][restaurant_name].append(iteminfo(item_name.get_text(strip=True),item_price.get_text(strip=True)))