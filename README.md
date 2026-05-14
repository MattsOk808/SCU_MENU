# SCU_MENU

A web scraping tool that allows the user to view the current breakfast/lunch/dinner menu at SCU. Also allows the user to save meals into a schedule, keep track of favorites, and view the ingredients used in a specified meal.

# SETUP

To run correctly, ensure that all libraries are installed using 

```pip install -r requirements.txt```

You also must have a gemini api key and create a .env file that contains

```
API_KEY="YOUR_API_KEY"
```
without the quotations and with your api key

# RUNNING

Run with ```python main.py```

Commands:

Commands and all other choices are selected by entering the number next to the option (unless specified otherwise)

```menu```

You will be prompted to select a date in the format after which the menu for breakfast/lunch/dinner for that day will be printed. Items in your list of favorites wil be highlighted yellow and items that contain ingredients mentioned in your allergy/dietary restriction list will be highlighted red.

```edit```

You will be prompted to select a date. 
If you do not have a prexisting entry for that date, a new one will be created. The new entry will not be saved if no edits are made to it.

You will then be able to choose between viewing the menu for that date, editing your meal for breakfast/lunch/dinner, or exiting the editor via saving or not saving the changes.

When choosing to edit the meal, you will be given two prompts, the first to select the restaurant and the second to select the meal.

When exiting, the changes to your schedule will be printed.

```schedule```

You will be prompted to select a date or 'full'. If a date was chosen, your schedule for that date will be printed. If 'full' was entered, all entries in your schedule are printed out. Additionally, the total cost of all meals for that day will be printed in both cases.

```ingredients```

You will be shown a list of all meals in your schedule and all meals you have seen in the menu thus far. You can choose a meal after which the ingredients for that meal will be printed out.

```favorites```

You can choose between adding, deleting, viewing, or exiting. 

Adding will prompt you for the date, restaurant, and item after which the selected item will be added to your list of favorites. 

Deleting will prompt you to select an item in your favorites list or cancel after which the selected item will be deleted from the list.

Viewing will display all of your current favorites.

```allergies/dietary restrictions```

You can choose between adding, deleting, viewing, or exiting. 

Adding will prompt you to enter the name of the allergen/dietary restriction after which the specified allergen/dietary restriction will be added to the list

Deleting will prompt you to select an allergen/dietary restriction in your list or cancel after which the selected item will be deleted from the list.

Viewing will display all of your current allergen/dietary restriction.

``` recommendation (main_ai.py only)```
You will be prompted to select a date. You can then toggle additional preferences (which will be displayed) or continue. Then, using Gemini's API, you will be recommended breakfast, lunch, and dinner for that date using the menu for that date, your list of favorite meals, the ingredients in your favorite meals, foods in your allergy/dietary restriction list, toggled preferences, and meals on the menu.

```exit```

Exits the program and writes the schedule into schedule.json, favorites into favorites.json, and ingredients into ingredients.json (for only the meals in your schedule and favorites list)
