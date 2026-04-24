# SCU_MENU

A web scraping tool that allows the user to view the current breakfast/lunch/dinner menu at SCU. Also allows the user to save meals into a schedule.


# SETUP

To run correctly, ensure that BeautifulSoup is installed using 

```pip install beautifulsoup4```

# RUNNING

Run with ```python main.py```

Commands:

```menu```

You will be prompted to enter a date in the format "YYYY-MM-DD" or 'today' after which the menu for breakfast/lunch/dinner for that day will be printed

```schedule```

You will be prompted to enter a date in the format "YYYY-MM-DD" or 'full'. If a date was entered, your schedule for that date will be printed. If 'full' was entered, all entries in your schedule are printed out. Additionally, the total cost of all meals for that day will be printed in both cases.

```edit```

You will be prompted to enter a date in the format "YYYY-MM-DD". 
If you do not have a prexisting entry for that date, a new one will be created.

To view the menu, enter ```menu```

To finish editing, enter ```done```

To update your schedule, enter a mealtime(breakfast/lunch/dinner) then you will be prompted to enter the restaurant you want to save the meal from. Finally, you will be prompted to enter the number of the item (which can be seen in the printed menu) after which your new meal for that time will be updated.

After exiting, the changes to your schedule will be printed.

```exit```

Exits the program and writes the schedule into schedule.txt;
