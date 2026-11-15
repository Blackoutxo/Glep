import random
import sys
import textwrap

# Room
ROOM = {
    "Breakroom" : dict(
        name = "The smiling friends breakroom",
        desc = "Glep is sitting on a bean bag playing with his iPad doing nothing"
               "Charlie and pim and just sitting having a coffee"
               "Alan is looking at the TV about the election of president Jimball and Mr.Frog"
               "Mr.Boss comes in shaking and shivering for being hungry and opens the fridge"
               "He find no snacks and asks glep for help to find snack as the fridge was full JUST NOW",
        exits = ["Alley", "Bus stop"],
        items = [],
        people = ["Alan", "Charlie", "Pim", "Mr.Boss"]
    ),
    "Alley" : dict(
        name = "The smiling friends alley",
        desc = "In the alley, A dumpster, A puddle that reflects a worse version of yourself"
               "And an ominously opened drain gate with a single piece of m&m in its side",
        exits = ["Sewer", "Breakroom-again"],
        items=["A cool rock", "single piece of m&ms"],
        people =["Mr.Boss"]
    ),
    "busstop": dict(
        name="The Bus Stop",
        desc="A bench, a schedule no one reads, and a bus that comes whenever it "
            "feels like it. This is your exit from the whole situation.",
        exits=["Alley", "Breakroom-again"],
        items=[],
        people=[],
    ),
    "Breakroom-again": dict(
        name="The smiling friends breakroom",
        desc="Glep and Mr.boss went back to the breakroom and suspect something is wrong with the "
             "fridge below......................"
             "They moved the fridge and saw a big gaping hole that seems to lead to a sewer"
             "with a random ancient chinese gold, Charlie's uncle's pill box",
        exits = ["Alley", "Sewer"],
        items =["A random chinese gold coin", "Charlie's uncle's pills"],
        people = ["Mr.Boss", "Charlie", "Pim"]
    ),
    "Sewer": dict(
        name="The sewer",
        desc="Knee-high water. Echo. A quarter glints on a dry ledge just past a"
             "very large rat who has clearly been doing fine down here.",
        exits= ["Breakroom-again", "Alley"],
        items=["Quarter"],
        people=["The big enormous rat"],
    ),
}

# vars
current_room = "Breakroom"
inventory = []
game_running = True

print("=== SMILING FRIENDS: THE MISSING SNACKS ===")
print("You are Glep. Help Mr. Boss find the missing snacks!")
print("Commands: go [place], take [item], talk [person], inventory, quit")
print("-" * 50)

while game_running:
    room_data = ROOM[current_room]
    
    # Show current room info
    print("\nLOCATION:", room_data["name"])
    print(room_data["desc"])
    print("Exits:", ", ".join(room_data["exits"]))
    
    if len(room_data["items"]) > 0:
        print("Items here:", ", ".join(room_data["items"]))
        
    if len(room_data["people"]) > 0:
        print("People here:", ", ".join(room_data["people"]))
        
    # Get player input
    command = input("\nWhat do you want to do? > ").strip()
    
    # Quit
    if command.lower() == "quit":
        print("Glep spits on the floor and walks away. Game Over.")
        game_running = False
        
    # Inventory
    elif command.lower() == "inventory":
        if len(inventory) == 0:
            print("You aren't carrying anything.")
        else:
            print("Your pockets:", ", ".join(inventory))

    # Move
    elif command.lower().startswith("go "):
        destination = command[3:].strip()
        
        found_exit = None
        for exit_name in room_data["exits"]:
            if destination.lower() == exit_name.lower():
                found_exit = exit_name
                
        if found_exit is not None:
            current_room = found_exit
            
            # Special ending if Glep takes the bus
            if current_room == "Bus stop":
                print("\nYou get on the bus and leave Mr. Boss to starve. Honestly, fair enough.")
                print("THE END (Coward Ending)")
                game_running = False
        else:
            print("You can't go there!")
            
    elif command.lower().startswith("take "):
        item_name = command[5:].strip()
        
        found_item = None
        for item in room_data["items"]:
            if item_name.lower() == item.lower():
                found_item = item
                
        if found_item is not None:
            inventory.append(found_item)
            room_data["items"].remove(found_item)
            print("Glep picked up:", found_item)
        else:
            print("That item isn't here.")
            
    elif command.lower().startswith("talk "):
        person_name = command[5:].strip()
        
        found_person = None
        for person in room_data["people"]:
            if person_name.lower() == person.lower():
                found_person = person
                
        if found_person is not None:
            if found_person == "Alan":
                print("Alan: 'I just wanted my cheese... and now the snacks are gone too.'")
            elif found_person == "Charlie":
                print("Charlie: 'Dude, I don't know, maybe check the alley or something. Just leave me out of it.'")
            elif found_person == "Pim":
                print("Pim: 'Ooh, a mystery! Don't worry Mr. Boss, Glep is on the case!'")
            elif found_person == "Mr.Boss":
                if "single piece of m&ms" in inventory:
                    print("Mr.Boss: 'OH BOY AN M&M!! MY BLOOD SUGAR IS SAVED!!'")
                    print("YOU WIN! You saved Mr. Boss!")
                    game_running = False
                else:
                    print("Mr.Boss: '*shivering* Glep... please... find me a snack before I turn into a demon...'")
            elif found_person == "The big enormous rat":
                if "Quarter" in inventory or "A random chinese gold coin" in inventory:
                    print("The big enormous rat: 'Nice shiny coin, little green guy. Keep it. I already ate the fridge snacks.'")
                else:
                    print("The big enormous rat: 'Squeak. (He looks way too full to move. He definitely ate the snacks.)'")
        else:
            print("Nobody by that name is here.")
    else:
        print("Glep says: 'Ashashashasha!' (Try: go [place], take [item], talk [person], inventory, or quit)")