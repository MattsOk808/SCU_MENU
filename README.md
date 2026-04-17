# SCU_MENU
A web scraping tool that allows the user to view the current breakfast/lunch/dinner menu at SCU. Also allows the user to save meals into a schedule.


#SETUP
To run correctly, ensure that BeautifulSoup is installed using 

`pip install beautifulsoup4'

#RUNNING

Commands:

'menu'
This will print the current menu for breakfast/lunch/dinner

'date'
You will be prompted to enter a date in the format "YYYY-MM-DD" after which your schedule for that date will be printed out

'edit'
You will be prompted to enter a date in the format "YYYY-MM-DD". 
If you do not have a prexisting entry for that date, a new one will be created. 
Then, until you enter exit, you can enter mealtimes (breakfast/lunch/dinner), then the meal to edit your schedule for that date.
After entering exit, the changes to your schedule will be printed.

'done'
Exits the program and writes the schedule into schedule.txt;
