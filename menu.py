from items import all_items
from map import *

# def intel_menu(intel: dict | None = ...,
#                 intel_list: dict | None = ...):
#     '''This function is for the intel menu, it takes 2 arguments.
#     The first argument is "intel", this allows us to remember user choices from a previous run of the loop and allow us to not delete choices when the user wants to recheck the intel menu
#     The second argument is "intel_list", this is for the dictionary of all the intel choices available and will be a global variable defined in the file assets/intels.py.
#     For testing, intel_list is defined as {"Test1":test1,"Test2":test2,"Test 3":test3,"Nointel":no_intel} and intel is defined as an empty string
    
#     >>> intel_menu()
#     You have currently selected: No intel
#     1. Test1
#     2. Test2
#     3. Test3
#     3. No Intel
#     4. Exit
#     What intel would you like to use? 
    

#     '''
#     if intel == None or intel == "":
#         return TypeError("intel is defined as None or an empty string")
#     flag = True
#     length_of_choices = len(intel_list)
#     while flag:
#         print(f"You have currently selected: {intel["name"]}")
#         items = []
#         for i, item in enumerate(intel_list.items(), start=0):
#             item = item[1]
#             items.append(item["id"])
#             print(f"{i+1}. {item["name"]}")
#         print(f"{length_of_choices+1}. Exit")
#         menu_choice = input("What intel would you like to use? ")
#         if int(menu_choice)-1 < length_of_choices:
#             intel = intel_list[items[int(menu_choice)-1]]
#         elif int(menu_choice) == length_of_choices+1:
#             flag = False
#         else:
#             print("That is not an option")
#     return intel

def item_menu(selected: list | None=[],
                item_list: dict | None = all_items):
    if selected == None or selected == "":
        return TypeError("selected is defined as None or an empty string")
    flag = True
    length_of_choices = len(item_list)
    while flag:
        print(f"You have currently selected:")
        for item in selected:
            print(f"{item["name"]}")
        items = []
        for i, item in enumerate(item_list.items(), start=0):
            item = item[1]
            items.append(item["id"])
            print(f"{i+1}. {item["name"]}")
        print(f"{length_of_choices+1}. Exit")
        menu_choice = input("What exit would you like to use? ")
        try:
            int(menu_choice)
            if int(menu_choice)-1 < length_of_choices:
                if item_list[items[int(menu_choice)-1]] not in selected:
                    selected.append(item_list[items[int(menu_choice)-1]])
                else:
                    selected.pop(item_list[items[int(menu_choice)-1]])
            elif int(menu_choice) == length_of_choices+1:
                if len(selected) <= 3:
                    flag = False
                else:
                    print(f"You have too many items selected, unselect {len(selected)-3} items to be able to start.")
            else:
                print("That is not an option")
        except ValueError:
            print("Invalid choice")
    return selected

def exit_menu(selected: dict | None = None):
    if selected == None or selected == "":
        return TypeError("sel_exit is defined as None or an empty string")
    flag = True
    while flag:
        print(f"You have currently selected: {selected["name"]}")
        print("""
              1. Backdoor
              2. Roof
              3. Sewers""")
        menu_choice = input("What exit would you like to use? ")
        try:
            int(menu_choice)
            if int(menu_choice) == 1:
                selected = rooms["Back"]
                return selected
            elif int(menu_choice) == 2:
                selected = rooms["Roof"]
                return selected
            elif int(menu_choice) == 3:
                selected = rooms["Sewers"]
                return selected
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")
    return selected

def entry_menu(selected: dict | None = None):
    if selected == None or selected == "":
        return TypeError("sel_entrance is defined as None or an empty string")
    flag = True
    while flag:
        print(f"You have currently selected: {selected["name"]}")
        print("""
              1. Front
              2. Roof
              3. Backdoor""")
        menu_choice = input("What entrance would you like to use? ")
        try:
            int(menu_choice)
            if int(menu_choice) == 1:
                selected = rooms["Lobby"]
                return selected
            elif int(menu_choice) == 2:
                selected = rooms["Roof"]
                return selected
            elif int(menu_choice) == 3:
                selected = rooms["Back"]
                return selected
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")
    return selected
    


def start_menu():
    items = []
    planned_exit = rooms["Back"]
    entry = rooms["Lobby"]
    while True:
        print("""Heist Planning
              1. Items
              2. Exits
              3. Entry point
              4. Start Heist
""")
        menu_choice = input("What Menu do you wish to access? ")
        try:
            int(menu_choice)
            if menu_choice == "1":
                items = item_menu(items)
            elif menu_choice == "2":
                planned_exit = exit_menu(planned_exit)
            elif menu_choice == "3":
                entry = entry_menu(entry)
            elif menu_choice == "4":
                items = [item["id"] for item in items]
                return items, planned_exit, entry
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")

if __name__ == "__main__":
    start_menu()