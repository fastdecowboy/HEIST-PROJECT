from random import randint, choice
from time import sleep

from items import *
from menu import *
from police import *
from map import *
from parser import *
from npc_list import *
from player import inventory, current_room

def list_of_items(items):
    item_list = []
    print("Item list", items)

    all_items_keys = all_items.keys()

    for item in items:
        if item in all_items_keys:
            item_list.append[all_items(item)]

    # for item in items:
    #     print(type(item))
    #     if isinstance(item, dict):# and "name" in item:
    #         if items[item]["type"] == "valuable":
    #             pass
    #         else:
    #             item_print = items[item]["name"]
    #             item_list.append(item_print)
    #     else:
    #         print("Invalid item format:", item)
    return item_list


def print_room_items(room):
    item_list = list_of_items(room["items"])
    if item_list != "":
        print(f"There is {', '.join(item_list)} here.\n")


def print_inventory_items(items):
    
    item_list = list_of_items(items)
    total_items = "You have "
    if item_list != "":
        #print(f"You have {', '.join(item_list)}.\n")
        print(f"You have {item_list}.\n")

        #for i in len(item_list):
        #   for i in range(0, len(items)):
            #total_items += items[i]["name"] + ", "
        #total_items = total_items[0:len(total_items) -2]
        #print(f"You have {total_items}.\n")


def print_room(room):
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display room NPCs
    for npc in room["npcs"]:
        print(f"In the room there is a {npc["name"]}")
    # Display room items
    print_room_items(room)

def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, locked, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        if locked[direction]:
            print(f"{direction.upper()} is locked.")
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print(f"TAKE {item["id"].upper()} to take {item["name"]}.")
    
    for item in inv_items:
        print(f"DROP {item["id"].upper()} to drop {item["name"]}.")
    
    for item in inv_items:
        if item["useable"]:
                print(f"USE {item["id"].upper()} on TARGET to use {item["name"]} on a specified target.")

    if current_room == room_vault:
        print("UNLOCK VAULT to unlock the vault.")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def unlock_room(direction):
    current_room["locked"][direction] = False

def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"],direction):
        current_room = move(current_room["exits"], direction)

    else:
        print("You cannot go there.")

    return current_room


def execute_take(item_id):
    item_list = current_room["items"]
    for item in item_list:
        if item["id"] == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
        else:
            print("You cannot take that.")
    

def execute_drop(item_id):
    item_list = inventory
    for item in item_list:
        if item["id"] == item_id:
            current_room["items"].append(item)
            inventory.remove(item)
        else:
            print("You cannot drop that.")
    
def execute_use(item_id, target):
    global police
    global current_room
    if item_id == "crowbar" | item_id == "lockpick":
        if item_crowbar in inventory or item_lock_pick in inventory:
            if len(current_room["locked_paths"]) == 0:
                print("There are no locked rooms.")
            else:
                unlock_room(target)
    elif item_id == "gun" & inventory.__contains__(item_gun):
        if target == "guard" & current_room["npcs"].__contains__(guard):
            roll = randint(1,100)
            if roll > 75:
                print("The guard has been eliminated.")
            elif roll > 70:
                inventory.remove(item_gun)
                print("The guard has been eliminated, but your gun takes damage, forcing you to leave it behind.")
                current_room["npcs"].pop(guard)
            elif roll > 30:
                print("The guard takes cover and exits the room, taking no damage.")
                random_room = choice(current_room["exits"])
                random_room["npcs"].append(current_room["npcs"].pop(guard))
            else:
                print("The guard stands firm, forcing you to leave through the nearest door.")
                current_room = choice(current_room["exits"])
            print("hearing shots, a police unit moves into the building.")
            police.append(new_police())
        elif target == "civilian" & current_room["npcs"].__contains__(civilian):
            current_room["npcs"].pop(civilian)
            print("You shoot the civilian, the blood seeps into your boots as you walk forward.")
            print("hearing shots, a police unit moves into the building.")
            police.append(new_police())
        else:
            print("You shoot wildly into the air at an invisible target, anyone watching would consider you crazy.")
    elif item_id == "baton":
        if target == "guard" & current_room["npcs"].__contains__(guard):
            roll = randint(1,100)
            if roll > 85:
                print("The civilian has been eliminated.")
            elif roll > 70:
                print("The guard has been eliminated, but your baton takes damage, forcing you to leave it behind.")
                current_room["npcs"].pop(guard)
            elif roll > 30:
                print("The guard takes cover and exits the room, taking no damage.")
                random_room = choice(current_room["exits"])
                random_room["npcs"].append(current_room["npcs"].pop(guard))
            else:
                print("The guard stands firm, forcing you to leave through the nearest door.")
                current_room = choice(current_room["exits"])


def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1], command[2])
        else:
            print("use what?")
    elif command[0] == "unlock" & command[1] == "vault":
        if current_room == room_vault:
            vault_unlock()
        else:
            print("There is no vault to unlock.")
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]


def vault_unlock(item_id):
    if item_id == "blowtorch":
        print("You use your blowtorch to unlock the vault.")
        current_room["items"].append(item_gold_bar)
        current_room["items"].append(item_silver_necklace)
        new_police(current_room)

    elif item_id == "keycard":
        print("You use the keycard to unlock the vault.")
    else:
        print("You cannot unlock the vault with that.")
        



def victory_condition(planned_exit):
    if current_room["type"] == "exit" and current_room["name"] == planned_exit:
        for item in inventory:
            if item["type"] == "valuable":
                win = True
            else:
                win = False
        if win:
            score = 0
            for item in inventory:
                if item["type"] == "valuable":
                    score += 1
                    print(f"You collected: {item["name"]}")
                    sleep(1)
            print(f"The bank has been robbed, with you claiming: {score} points.\nWith this, you can start a new life.")
            sleep(3)
            print("Right?")


# This is the entry point of our program
def main():
    new_items, planned_exit, current_room = start_menu()
    inventory = new_items
    police = []
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        #Check victory condition
        victory = victory_condition(planned_exit)
        if victory:
            break
        police = police_movement(police)
        if len(police) > 0:
            if current_room in police:
                print("The police have caught you.")
                break
            print("The police are closing in on you.")
            for officer in police:
                print(f"Officer {police.index(officer)} is in {officer["current"]}")

if __name__ == "__main__":
    main()