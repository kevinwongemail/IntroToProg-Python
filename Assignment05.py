# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
#
#              The "ToDo" file will contain two columns of data,
#              "Task" and "Priority." Load the columns into a 
#              Python Dictionary object. Each dictionary object represents
#              one row of data, and these rows must be added to a 
#              Python List object to create a table of data. 
#
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kevin Wong, 11/05/2019, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None              # An object that represents a file
textfile = "ToDoList.txt"   # text file
strData = ""                # A row of text data from the file
dicRow = {}                 # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []               # A dictionary that acts as a 'table' of rows
lstRow = []                 # A dictionary that acts as a row of list
strMenu = ""                # A menu of user options
strChoice = ""              # A Capture the user option selection
var = ""

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a textfile called ToDoList.txt into a python Dictionary.
objFile = open(textfile, "a")   # "w" does not work a sit destroys the existing file
objFile.close()

objFile = open(textfile, "r")   # past: "r"
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
     
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
     
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
     
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for objRow in lstTable:
            print(objRow)
        
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        
        strTask = input("Enter an task: ")
        strPriority = input("Enter an priority: ") 
        dicRow = {"Task":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        continue
    
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(textfile, "w")
        #for objRow in lstTable:
        for objRow in lstTable:
            objFile.write(objRow["Task"] + "," + objRow["Priority"] + "\n")
        objFile.close()
        print("Data Saved!")
        continue
    
    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        strTask = input("Enter an task you would like to remove: ")
        for var in range(len(lstTable) -1, -1, -1):
            if lstTable[var]["Task"] == strTask:
                lstTable.pop(var)
        continue
      
    # Step 7 - Exit program
    elif strChoice.strip() =='5':
        break
    
    else:
        print("Please only select options from the menu")
        continue
    

        