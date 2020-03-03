# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# Chris Ausbun,02.27.2020,Added code to complete assignment 5
# Chris Ausbun,03.02.2020,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority):
        """ Add a task name and priority to the list
                :param task: (string) name of the task:
                :param priority: (string) Priority of Task:
                :return: 'success'
                """
        global dicRow, lstTable
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        return 'Success'

    @staticmethod
    def remove_data_from_list(task):
        """ Remove a task name and priority to the list
                :param task: (string) name of the task:
                :return: 'success'
                """
        global lstTable
        for objRow in lstTable:
            if task.lower() in str(objRow.values()).lower():
                print("Removing the following task from the list: " + task)
                # Remove the Task Name form the ToDoList
                lstTable.remove(objRow)
        return 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write the list of TO DO task to the text file
        :param file_name: (string) name of text file:
        :param list_of_rows: (List) list of rows:
        :return: (list) of dictionaries, 'success'
        """
        file_object_write = open(file_name, "w")
        for item in lstTable:
            file_object_write.write(str(item.get("Task")) + "," + str(item.get("Priority")) + "\n")
        file_object_write.close()
        return list_of_rows, 'Success'

    @staticmethod
    def check_if_already_exists(task):
        """ Check to see if the task name already exists in the list
        :param task: (string) name of the task:
        :return: Boolean value T/F
        """
        task_exists = False
        for item in lstTable:
            if task.lower() == item.get("Task").lower():
                task_exists = True
        if task_exists is True:
            return True
        else:
            return False


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks To-Do are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Input a new task and priority, check to see if task name exists.  If true, try another task!
        :return: nothing
        """
        str_task = input("What's the New Task Name?:  ")
        if not Processor.check_if_already_exists(str_task):
            str_priority = input("What's the priority of this task?: ")
            Processor.add_data_to_list(str_task, str_priority)
        else:
            print("The task already exists. Please press 'Enter' to go back to the menu!!")
            input()

    @staticmethod
    def input_task_to_remove():
        """ Input a task name to remove, check to see if exists.  If so, delete it from the list!
        :return: nothing
        """
        str_task = input("Which task would you like to remove?:  ")
        if Processor.check_if_already_exists(str_task):
            Processor.remove_data_from_list(str_task)
        else:
            print("The given task does not exist.  Please try again!!")


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        while True:
            IO.input_new_task_and_priority()
            break

    elif strChoice == '2':  # Remove an existing Task
        while True:
            IO.input_task_to_remove()
            if "n" in IO.input_yes_no_choice("Would you like to remove another task? (y/n) - "):
                print()  # Add a line here for readability
                # Exit the loop and go to the Main Menu
            break

    elif strChoice == '3':  # Save Data to File
        # Evaluate the user choice and exit loop if "y" in response
        if "y" in IO.input_yes_no_choice("Would you like to save this data to file? (y/n) - "):
            Processor.write_data_to_file(strFileName, lstTable)
            strStatus = "Data Has Been Saved!!"
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        # Evaluate the user choice and exit loop if "y" in response, use the IO User input function
        if 'y' in IO.input_yes_no_choice("Are you sure you want to restore data from file? (y/n) -  "):
            Processor.read_data_from_file(strFileName, lstTable)  # read file data
            strStatus = "Original Data has been restored from file"
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
