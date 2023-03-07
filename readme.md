## To-Do List
This program allows users to create a to-do list, add, remove, and view items on the list.

## Usage
* Run the program.
* Follow the prompt to select an action:
* Press 1 to add an item to the list.
* Press 2 to remove an item from the list.
* Press 3 to view the list.
* If you choose to add an item, enter the item to add when prompted.
* If you choose to remove an item, the current list will be displayed, and you will be prompted to enter the number of the item you want to remove.
* If you choose to view the list, the current list will be displayed.
* After each action, the program will prompt if you want to continue or exit. Enter 'y' to continue, and any other input to exit the program.
## Code 
The code initializes an empty to-do list, then prompts the user for an action using an infinite while loop. It includes three functions:

* `add_to_list()` prompts the user for an item to add to the list and adds it to the end of the list.
* `remove_from_list()` displays the current list, prompts the user for the number of the item to remove, removes the item, and displays a message confirming the removal.
* `view_list()` displays the current list, with each item numbered.

The program uses a switch case structure to select the appropriate function based on the user's input. After each action, the program prompts the user to continue or exit. If the user enters 'y', the program continues; otherwise, it exits the loop and prints "Goodbye."