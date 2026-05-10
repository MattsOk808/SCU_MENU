# SCU_MENU

A web scraping tool that allows the user to view the current breakfast/lunch/dinner menu at SCU. Also allows the user to save meals into a schedule, keep track of favorites, and view the ingredients used in a specified meal.

# SETUP

To run correctly, ensure that all libraries are installed using 

```pip install beautifulsoup4 requests colorama sortedcontainers```

# RUNNING

Run with ```python main.py```

Commands:

Commands and all other choices are selected by entering the number next to the option (unless specified otherwise)

```menu```

You will be prompted to select a date in the format after which the menu for breakfast/lunch/dinner for that day will be printed. Items in your list of favorites wil be highlighted yellow.

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

You can choose between adding, viewing, or exiting. 

Adding will prompt you for the date, restaurant, and item after which the selected item will be added to your list of favorites. 

Viewing will display all of your current favorites.

```exit```

Exits the program and writes the schedule into schedule.json, favorites into favorites.json, and ingredients into ingredients.json (for only the meals in your schedule)
