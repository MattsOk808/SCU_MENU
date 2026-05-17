# SCU_MENU

A web scraping tool that allows the user to view the current breakfast/lunch/dinner menu at SCU. Also allows the user to save meals into a schedule, keep track of favorites, and view the ingredients used in a specified meal.

# SETUP

To run correctly, ensure that all libraries are installed using 

```
pip install -r requirements.txt
```

You also must have a gemini api key and create a .env file that contains

```
API_KEY="YOUR_API_KEY"
```
without the quotations and with your api key

# RUNNING

Run with ```python main.py```

Commands:

Commands and all other choices are selected by entering the number next to the option (unless specified otherwise)

<img width="486" height="175" alt="Screenshot 2026-05-16 193108" src="https://github.com/user-attachments/assets/8c5db468-f86e-4c3f-9e67-aca15073891e" />

<sub>*Example of user interface*</sub>

```menu```

You will be prompted to select a date after which the menu for breakfast/lunch/dinner for that day will be printed. Items in your list of favorites wil be highlighted yellow and items that contain ingredients mentioned in your allergy/dietary restriction list will be highlighted red.

<img width="501" height="198" alt="Screenshot 2026-05-16 193439" src="https://github.com/user-attachments/assets/1679744d-0c3d-48fa-9033-94e64ead8569" />

<sub>*Date selection*</sub>

<img width="1197" height="987" alt="Screenshot 2026-05-16 193912" src="https://github.com/user-attachments/assets/5e13d4de-3b99-4b26-a4cf-75922b02de2e" />

<sub>*Example menu display with favorited highlighted yellow*</sub>

```edit```

You will be prompted to select a date. 
If you do not have a prexisting entry for that date, a new one will be created. The new entry will not be saved if no edits are made to it.

<img width="310" height="200" alt="Screenshot 2026-05-16 193641" src="https://github.com/user-attachments/assets/333263ca-af28-4d2d-8e69-0d2c955f754f" />

<sub>*Date selection*</sub>

You will then be able to choose between viewing the menu for that date, editing your meal for breakfast/lunch/dinner, or exiting the editor via saving or not saving the changes.

<img width="340" height="157" alt="Screenshot 2026-05-16 193704" src="https://github.com/user-attachments/assets/159bad10-b18c-4fbb-97dc-361c2426cda5" />

<sub>*User interface*</sub>

When choosing to edit the meal, you will be given two prompts, the first to select the restaurant and the second to select the meal.

<img width="346" height="245" alt="Screenshot 2026-05-16 194125" src="https://github.com/user-attachments/assets/70dbaf30-a97b-42eb-a9c4-2214509e025e" />

<sub>*Restaurant selection*</sub>

<img width="430" height="91" alt="Screenshot 2026-05-16 194056" src="https://github.com/user-attachments/assets/808f8178-1bdd-4fcc-897d-cc72da613fe6" />

<sub>*Meal selection*</sub>

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
