from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date,datetime
from shared.shared_vars import saved_menus,base_url,weekday_meals,weekenend_meals,ingredient_dict,headers,iteminfo
from shared.functions import get_times

def parse_menu(url=base_url,date=f"{date.today()}"):
    page=urlopen(Request(url+date,headers=headers))
    html=page.read().decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    meal_list=get_times(date)
    for time in meal_list:
        m=soup.find("section", class_=["panel s-wrapper site-panel site-panel--daypart site-panel--daypart-even","panel s-wrapper site-panel site-panel--daypart"],id=time)
        if m!=None:
            menu=m.find("div", class_="c-tab__content site-panel__daypart-tab-content tab-content- c-tab__content--active")
            for restaurant in menu.find_all("div", class_="station-title-inline-block"):
                restaurant_name=restaurant.find("h3",class_="site-panel__daypart-station-title").get_text(strip=True)
                if restaurant_name=="The Global Grill Lunch" or restaurant_name=="The Global Grill Dinner" or restaurant_name=="Global Grill Breakfast" or restaurant_name=="Globe":
                    restaurant_name="The Global Grill"
                elif restaurant_name=="La Parilla Breakfast":
                    restaurant_name="La Parilla"
                for item in restaurant.find_all("div", class_="site-panel__daypart-item-container"):
                    item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                    item_price=item.find("span",class_="price-item__amount")
                    ingredients=item.find("div",class_="site-panel__daypart-item-description")
                    if item_name!=None and item_price!=None:
                        item_name=item_name.get_text(strip=True)
                        item_price=float(item_price.get_text(strip=True))
                        if ingredients!=None:
                            if item_name not in ingredient_dict:
                                ingredients=ingredients.get_text(strip=True).split(', ')
                                ingredient_list = []
                                for ingredient in ingredients:
                                    if "SIDES:" in ingredient:
                                        parts = ingredient.split("SIDES:")
                                        ingredient_list.extend([p.strip() for p in parts])
                                    else:
                                        ingredient_list.append(ingredient.strip())
                                ingredient_dict[item_name]=ingredient_list
                        else:
                            ingredient_dict[item_name]=["Not provided"]
                        saved_menus[date][time][restaurant_name].append(iteminfo(item_name,item_price))
                for sibling in restaurant.find_next_siblings(): #if a restaurant has more than 2 items all remaining items are stored in a slightly different format
                    cls=sibling.get("class")
                    if(cls[0]!="site-panel__daypart-item"): 
                        break
                    for item in sibling.find_all("div", class_="site-panel__daypart-item-container"):
                        item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                        item_price=item.find("span",class_="price-item__amount")
                        ingredients=item.find("div",class_="site-panel__daypart-item-description")
                        if item_name!=None and item_price!=None:
                            item_name=item_name.get_text(strip=True)
                            item_price=item_price.get_text(strip=True)
                            if ingredients!=None:
                                if item_name not in ingredient_dict:
                                    ingredients=ingredients.get_text(strip=True).split(', ')
                                    ingredient_list = []
                                    for ingredient in ingredients:
                                        if "SIDES:" in ingredient:
                                            parts = ingredient.split("SIDES:")
                                            ingredient_list.extend([p.strip() for p in parts])
                                        else:
                                            ingredient_list.append(ingredient.strip())
                                    ingredient_dict[item_name]=ingredient_list
                            else:
                                ingredient_dict[item_name]=["Not provided"]
                            saved_menus[date][time][restaurant_name].append(iteminfo(item_name,item_price))
            menu=m.find("div",class_="c-tab__content site-panel__daypart-tab-content tab-content-") #Checking secondary tab for items 
            for restaurant in menu.find_all("div", class_="station-title-inline-block"):
                restaurant_name=restaurant.find("h3",class_="site-panel__daypart-station-title").get_text(strip=True)
                if restaurant_name=="The Global Grill Lunch" or restaurant_name=="The Global Grill Dinner" or restaurant_name=="Global Grill Breakfast" or restaurant_name=="Globe":
                    restaurant_name="The Global Grill"
                elif restaurant_name=="La Parilla Breakfast":
                    restaurant_name="La Parilla"
                for item in restaurant.find_all("div", class_="site-panel__daypart-item-container"):
                    item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                    item_price=item.find("span",class_="price-item__amount")
                    ingredients=item.find("div",class_="site-panel__daypart-item-description")
                    if item_name!=None and item_price!=None:
                        item_name=item_name.get_text(strip=True)
                        item_price=item_price.get_text(strip=True)
                        if ingredients!=None:
                            if item_name not in ingredient_dict:
                                ingredients=ingredients.get_text(strip=True).split(', ')
                                ingredient_list = []
                                for ingredient in ingredients:
                                    if "SIDES:" in ingredient:
                                        parts = ingredient.split("SIDES:")
                                        ingredient_list.extend([p.strip() for p in parts])
                                    else:
                                        ingredient_list.append(ingredient.strip())
                                ingredient_dict[item_name]=ingredient_list
                        else:
                            ingredient_dict[item_name]=["Not provided"]
                        saved_menus[date][time][restaurant_name].append(iteminfo(item_name,item_price))
                for sibling in restaurant.find_next_siblings(): #if a restaurant has more than 2 items all remaining items are stored in a slightly different format
                    cls=sibling.get("class")
                    if(cls[0]!="site-panel__daypart-item"): 
                        break
                    for item in sibling.find_all("div", class_="site-panel__daypart-item-container"):
                        item_name=item.find("button",class_="h4 site-panel__daypart-item-title")
                        item_price=item.find("span",class_="price-item__amount")
                        ingredients=item.find("div",class_="site-panel__daypart-item-description")
                        if item_name!=None and item_price!=None:
                            item_name=item_name.get_text(strip=True)
                            item_price=item_price.get_text(strip=True)
                            if ingredients!=None:
                                if item_name not in ingredient_dict:
                                    ingredients=ingredients.get_text(strip=True).split(', ')
                                    ingredient_list = []
                                    for ingredient in ingredients:
                                        if "SIDES:" in ingredient:
                                            parts = ingredient.split("SIDES:")
                                            ingredient_list.extend([p.strip() for p in parts])
                                        else:
                                            ingredient_list.append(ingredient.strip())
                                    ingredient_dict[item_name]=ingredient_list
                            else:
                                ingredient_dict[item_name]=["Not provided"]
                            saved_menus[date][time][restaurant_name].append(iteminfo(item_name,item_price))