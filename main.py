# To-Do List: Create a program that allows users to create a to-do list.
# Users should be able to add, remove, and view items on their list.

to_do_list = [] # initialize empty to-do list
print("Welcome to your To-Do list!")
while True:
    def add_to_list():
        item = input("What would you like to add? ")
        to_do_list.append(item)
        print(f"{item} has been added to your to-do list. ")

    def remove_from_list():
        print("Here is your current to-do list: ")
        for i, item in enumerate(to_do_list):
            print(f"{i+1}. {item}")
        number = int(input("Please enter the number of the item you wish to remove:"))
        removed_item = to_do_list.pop(number-1)
        print(f"{removed_item} has been removed from your to-do-list.")


    print("Press 1 to add an item to your list.")
    print("Press 2 to remove an item from your list.")
    print("Press 3 to view your list.")
    a = int(input("Enter your choice: "))

    if a == 1:
        add_to_list()

    elif a == 2:
        remove_from_list()

    elif a == 3:
        print("Here is your to-do list:")
        for i, item in enumerate(to_do_list):
            print(f"{i+1}. {item}")


    print("Do you wish to continue? Please enter y or n.")
    quit = input()
    if quit != 'y':
        print("Goodbye")
        break