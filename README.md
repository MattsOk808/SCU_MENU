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

Run with 
```
python main.py
```

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

When exiting, the changes to your schedule will be printed if both the save options was at least one item was added to the schedule (in the case where a new entry was created)

<img width="371" height="87" alt="Screenshot 2026-05-16 194628" src="https://github.com/user-attachments/assets/36c6c81f-f9c9-4519-bc02-7251db174d34" />

<sub>*Changes being displayed*</sub>

```schedule```

You will be prompted to select a date or 'full'. 

<img width="306" height="152" alt="Screenshot 2026-05-16 194843" src="https://github.com/user-attachments/assets/2fde08d7-7ef6-4a83-b69f-50914ff5bf8c" />

<sub>*Options*</sub>

If a date was chosen, your schedule for that date will be printed. If 'full' was entered, all entries in your schedule are printed out. Additionally, the total cost of all meals for that day will be printed in both cases.

<img width="525" height="530" alt="Screenshot 2026-05-16 194857" src="https://github.com/user-attachments/assets/34b70367-3455-42cc-918e-c3fb912b36ea" />

<sub>*Full schedule displayed*</sub>

```ingredients```

You will be shown a list of all meals in your schedule and all meals you have seen in the menu thus far. 

<img width="457" height="198" alt="Screenshot 2026-05-16 195116" src="https://github.com/user-attachments/assets/3188dd85-85b6-476d-ba8e-9397f55f8b3f" />

<sub>*Options*</sub>

You can choose a meal after which the ingredients for that meal will be printed out.

<img width="1482" height="19" alt="Screenshot 2026-05-16 195211" src="https://github.com/user-attachments/assets/fb0a6a06-e0e8-49ea-b512-001a1c853620" />

<sub>*Example of ingredients being displayed*</sub>

```favorites```

You can choose between adding, deleting, viewing, or exiting. 

<img width="281" height="109" alt="Screenshot 2026-05-16 195400" src="https://github.com/user-attachments/assets/3a474dac-5186-4bbe-8f2e-981041732695" />

<sub>*Options*</sub>

Selecting add will prompt you for the date, time, restaurant, and item after which the selected item will be added to your list of favorites. 

<img width="308" height="200" alt="Screenshot 2026-05-16 195459" src="https://github.com/user-attachments/assets/72e3df0f-e1b0-46c1-af5b-024587d0c958" />

<sub>*Date selection*</sub>

<img width="244" height="109" alt="Screenshot 2026-05-16 195520" src="https://github.com/user-attachments/assets/0c18df80-5cf4-4abe-a344-99eb38277433" />

<sub>*Time selection*</sub>

<img width="424" height="245" alt="Screenshot 2026-05-16 195651" src="https://github.com/user-attachments/assets/d3702aca-3e49-46d9-a0db-27dc05a29a9c" />

<sub>*Restaurant selection*</sub>

<img width="363" height="112" alt="Screenshot 2026-05-16 195744" src="https://github.com/user-attachments/assets/215c630b-f7ab-4d4a-a442-c28a3f7f688b" />

<sub>*Item selection*</sub>

<img width="465" height="46" alt="Screenshot 2026-05-16 195825" src="https://github.com/user-attachments/assets/4be6e1c4-b05f-4427-ba4d-5690d6324f0f" />

<sub>*Logging change*</sub>

Selecting delete will prompt you to select an item in your favorites list or cancel after which the selected item will be deleted from the list.

<img width="393" height="138" alt="Screenshot 2026-05-16 195917" src="https://github.com/user-attachments/assets/f9d434e6-fe5d-42cc-9f67-a256ae50ca72" />

<sub>*Item selection*</sub>

<img width="569" height="44" alt="Screenshot 2026-05-16 195948" src="https://github.com/user-attachments/assets/9e63484a-b7ac-4530-baf2-5f677ed482b2" />

<sub>*Logging change*</sub>

Selecting view will display all of your current favorites.

<img width="348" height="89" alt="Screenshot 2026-05-16 200122" src="https://github.com/user-attachments/assets/57aad5d3-49cc-4f9e-bfda-a9ecf5677c09" />

<sub>*Displaying list*</sub>

```allergies/dietary restrictions```

You can choose between adding, deleting, viewing, or exiting. 

<img width="317" height="111" alt="Screenshot 2026-05-16 200304" src="https://github.com/user-attachments/assets/35195921-99ca-4a3d-8af9-ca033d3226a8" />

<sub>*Options*</sub>

Adding will prompt you to enter the name of the allergen/dietary restriction after which the specified allergen/dietary restriction will be added to the list

<img width="607" height="66" alt="Screenshot 2026-05-16 200426" src="https://github.com/user-attachments/assets/8a0c045f-7335-407f-9119-a79de18ed258" />

<sub>*Adding allergen/dietary restriction*</sub>

Deleting will prompt you to select an allergen/dietary restriction in your list or cancel after which the selected item will be deleted from the list.

<img width="460" height="166" alt="Screenshot 2026-05-16 200710" src="https://github.com/user-attachments/assets/a38811a6-40cd-408a-8074-f6c7ab11fdb0" />

<sub>*Deleting allergen/dietary restriction*</sub>

Viewing will display all of your current allergen/dietary restriction.

<img width="451" height="106" alt="Screenshot 2026-05-16 200753" src="https://github.com/user-attachments/assets/371d43ef-62b0-4071-b389-b29672b1fea6" />

<sub>*Displaying all allergies/dietary restrictions*</sub>

``` recommendation (main_ai.py only)```

You will be prompted to select a date. 

<img width="540" height="195" alt="Screenshot 2026-05-16 200913" src="https://github.com/user-attachments/assets/44593e45-119e-4669-a7a4-ab1d430e1ff9" />

<sub>*Date selection*</sub>

You can then toggle additional preferences or continue. 

<img width="647" height="462" alt="Screenshot 2026-05-16 201021" src="https://github.com/user-attachments/assets/5cdcceb6-c140-4ad8-a1e7-e0413d2645c3" />

<sub>*Preference selection*</sub>

Then, using Gemini's API, you will be recommended breakfast, lunch, and dinner for that date using the menu for that date, your list of favorite meals, the ingredients in your favorite meals, foods in your allergy/dietary restriction list, toggled preferences, and meals on the menu.

<img width="1838" height="396" alt="Screenshot 2026-05-16 201206" src="https://github.com/user-attachments/assets/00c7db01-c90b-442f-828d-ac715cc59856" />

<sub>*Gemini recommendation*</sub>

```exit```

Exits the program and writes the schedule into schedule.json, favorites into favorites.json, and ingredients into ingredients.json (for only the meals in your schedule and favorites list)

<img width="1166" height="693" alt="Screenshot 2026-05-16 201308" src="https://github.com/user-attachments/assets/5526452d-2435-4d67-bdf2-2003400535e2" />

<sub>*Example of schedule.json*</sub>
