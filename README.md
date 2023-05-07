# The Get Fit! app

## Referenced Sources
Yesmin, F. (n.d.). How to Use Colorama in Python. [online] Available at: https://linuxhint.com/colorama-python/.

‌Programiz.com. (2018). Python datetime (With Examples). [online] Available at: https://www.programiz.com/python-programming/datetime.

GeeksforGeeks. (2020). Creating Tables with PrettyTable Library - Python. [online] Available at: https://www.geeksforgeeks.org/creating-tables-with-prettytable-library-python/.

‌Python.org. (2020). 8. Errors and Exceptions — Python 3.8.1 documentation. [online] Available at: https://docs.python.org/3/tutorial/errors.html.

‌Tuladhar, A. (2021). Simple BMI calculator using Python. [online] Data Insight. Available at: https://www.datainsightonline.com/post/simple-bmi-calculator-using-python#:~:text=%23Simple%20BMI%20calculator%20using%20python [Accessed 7 May 2023].

‌PythonForBeginners.com. (2022). How to Search for a String in a Text File Through Python. [online] Available at: https://www.pythonforbeginners.com/strings/how-to-search-for-a-string-in-a-text-file-through-python [Accessed 7 May 2023].

## GitHub Repository
[GitHub Repository](https://github.com/The-Programming-Mango/Fitness-App-T1A3)

## Slide Deck Video
[Youtube Slide Deck](https://youtu.be/lPIxebky9vQ)

## Code Style Guide
[PEP8 Style Guide](https://peps.python.org/pep-0008/)

## Features and Functions
1. Measurements Feature: The user will be able to store, view and retrieve their measurements.

   - Add Measurements Function: This function will allow the user to input their weight and height measurements and also the date. It will then store the information in the measurements.csv file.
  
   - View Measurements Function: This function will allow the user to view the measurements.csv file and then print the information in that csv file in an easy to read table in the terminal.
  
   - Search Measurements Function: This function will allow the user to search the measurements.csv file by date and then print the results in an easy to read table in the terminal.
  
2. Exercises feature: The user will be able to store, view and retrieve their exercise history.
   
   - Add Exercise Function: This function will allow the user to enter the exercises that they are doing as well as the sets and repetitions, the date also.
  
   - View Exercise Function: This function will print the contents of the exercise.csv file and present it in the terminal in an easy to read table.
  
   - Search Exercise Function: This will allow the user to search the exercise by name and then print the results in the terminal.
  
3. BMI Feature: The BMI feature allows the user to calculate their BMI as well as put them in the BMI category according to the user's input. They will also be able to view their BMI history.
   
   - Calculate BMI: This function will calculate the user's BMI depending on their height and weight. It will also categorise the user in one of the following categories. Underweight, healthy weight, overweight and obese.
  
   - View BMI History: This function will print the BMI history of the user into the terminal.

## Implementation Plan:

I plan to incorporate each feature through a main menu with each feature having a sub menu that the user can access from the main menu. From the sub menu the user will be able to access the different functions for that feature.

Deadline: 07/05/2023 Submission Date
Checklist:

Measurements Feature:
1. Create measurements CSV
2. Load measurements CSV
3. Add measurements to CSV
4. View measurements CSV
5. Search measurements CSV by date
   
Exercise Feature:
1. Create exercise CSV
2. Load exercise CSV
3. Add exercises to CSV
4. View exercise CSV
5. Search exercise CSV by exercise name
   
BMI Feature:
1. Create BMI CSV
2. Load BMI CSV
3. Calculate BMI
4. Categorise user BMI
5. Store user's BMI and category in CSV
6. View user's BMI and category history from CSV

Project Management Platform: Monday
![Main Table](/development_plan/main_table.jpg)
![Gantt](/development_plan/gantt.jpg)
![Kanban](/development_plan/kanban.jpg)

# Help Documentation

System Requirements:
1. Computer with VSC installed
2. VSC with Python installed
3. Have an installed Command Line Interpreter, up to the user. (I'll be using WSL)
4. Modules installed to VENV from the modules.txt file (See step 3 in application installation)

Steps to install and run the application:
1. Download file from [GitHub Repository](https://github.com/The-Programming-Mango/Fitness-App-T1A3)
2. Open the source code file in VSC
3. You can choose to use a VENV to avoid installing all the modules directly to your VSC and to isolate the modules for only this terminal application. Otherwise you can just continue on without using a VENV.
4. Create a VENV in your WSL terminal by typing "python3 -m venv venv (You can replace the last venv with whatever name you'd like for your venv)
5. Activate your VENV in your WSL terminal by typing "source venv/bin/activate"
6. You should now be in your venv. You can make sure you're there by seeing (venv) at the start of the command line.
7. You can now install the required modules to run this terminal application by typing "pip install -r modules.txt"
8. To run the terminal application, type "python run_app.py" in your terminal.
9. You should now be welcomed to the Get Fit! app and have access to the main menu.