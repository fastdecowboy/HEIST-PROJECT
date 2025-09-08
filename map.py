from assets.items import *
from assets.npc_list import *

room_vault = {
    "name": "Vault",

    "description": 
    """As the door creaked open, a waft of cold, stale air rushed into 
    your nostrils. The silence inside was palpable, broken only by the 
    echoing of your footsteps. Inside you see rows of security boxes, 
     cash, and more importantly, bars of gold. However, the door slams 
     behind you, causing you to panick. Luckily, you notice a vent on 
     north side of the room.""",

    "exits": {"north": "Maintenance"},
    "items": [],
    "type": "room",
    "locked": {"north": False},
    "npcs": []
}

room_security = {
    "name": "Security Room",
    
    "description":
    """You are in the main security room, in front of you is a security guard 
    who's taking his afternoon nap. Inside is a row of cameras, spanning the entire
    building. You notice a keycard on the desk. To the south is the managers office, 
    however there is also an exit to the north which leads to the roof.""",

    "exits": {"north": "Roof", "south": "Managers"},
    "items": [item_keycard, item_baton],
    "type": "room",
    "locked": {"north": True, "south": False},
    "npcs": [guard]
}

room_clerk = {
    "name": "Clerk Office",
    
    "description": 
    """You are in the clerks' office, the room is filled with folders and the faint 
    scent of paper and ink. On the desks you see an overwhelming quantity of paper stacks,
     as well some cheques. To the west is the lobby, to the north is the vault, and to 
     the east is the exit to the sewers.""",
     
    "exits": {"west": "Lobby", "north": "Vault", "east": "Sewers"},
    "items": [item_gun],
    "type": "room",
    "locked": {"west": False, "north": False, "east": False},
    "npcs": [civilian]
}

room_lobby = {
    "name": "Lobby",

    "description": 
    """You are in the main bank lobby, the grand open space is flooded with natural light
    streaming through the tall, arched windows. The air was crispy and cool, with the faint 
    scent of polished marble and leather. To the north is an elevator, to the east is the
     clerk's office and the west leads to the break room.""",

    "exits": {"north": "Elevator", "east": "Clerks", "west": "Break"},
    "items": [],
    "type": "room",
    "locked": {"north": False, "east": False, "west": False},
    "npcs": [civilian]
}

room_maintenance = {
    "name": "Maintenance Room",

    "description":
    """You are in the maintenance room, it is dimly lit by a single overhead bulb. The walls
     are bare concrete, and the floor is scuffed from years of work. There is a cleaning kart, 
      as well as a set of tools. You can go north to the stairway.""",

    "exits": {"north", "Stairs"},
    "items": [item_grappler],
    "type": "room",
    "locked": {"north": False},
    "npcs": []
}

room_manager = {
    "name": "Manager's Office",

    "description":
    """You are in the manager's office, on his large mahogany desk are countless miscellaneous 
    objects, including a bobblehead of Darth Vader and Buzz Lightyear. Also on the wall is a 
    framed degree certifiate in Computer Science graduating from Cardiff University! You can go
    north to the security room, and south to teh break room.""",

    "exits": {"north": "Security", "south": "Break"},
    "items": [item_lock_pick],
    "type": "room",
    "locked": {"north": True, "south": False},
    "npcs": [manager]
}

room_break = {
    "name": "Break Room",

    "description":
    """You are in the break room, the wallpapers are monochromatic, creating a very gloomy
    and uninspiring vibe. You can go east to the lobby, or north to the managers office. You 
    also notice a backdoor exit at the western edge of the room.""",

    "exits": {"west": "Back", "north": "Managers", "east": "Lobby"},
    "items": [item_crowbar],
    "type": "room",
    "locked": {"west": False, "north": False, "east": False},
    "npcs": []
}

room_elevator = {
    "name": "Elevator",

    "description": """You are in the elevator, the music playing is "Fein" by Travis Scott. 
    You can go north to the maintenance room.""",

    "exits": {"north", "Maintenance"},
    "items": [item_blowtorch],
    "type": "room",
    "locked": {"north": False},
    "npcs": []
}

room_stairs = {
    "name": "Stairway",

    "description": """You are in the stairway, make sure not to slip... the only exit is west
    towards the security room.""",

    "exits": {"west", "Security"},
    "items": [],
    "type": "room",
    "locked": {"west": True},
    "npcs": []
}

room_roof = {
    "name": "Roof",

    "description": """You are on the roof, the murky grey clouds in the sky reflect your mood.""",

    "exits": {"south", "Security"},
    "items": [],
    "type": "exit",
    "locked": {"south": False},
    "npcs": []
} 

room_back = {
    "name": "Back Room",

    "description": """You are in the backroom, at the edge of the room is a security exit.""",
    
    "exits": {"east", "Break"},
    "items": [item_guard_uniform],
    "type": "exit",
    "locked": {"east": False},
    "npcs": []
}

room_sewers = {
    "name": "Sewers",

    "description": """You are in the sewers. You're surrounded by a flowing stream of sewage, 
    noticing countless gross articles of waste. The tight enclosed space makes you feel
    claustrophobic, and the sound of ravenous rats doesn't help ease your fears.""",

    "exits": {"west", "Clerks"},
    "items": [],
    "type": "exit",
    "locked": {"west": False},
    "npcs": []
}


#git add, commit, push

rooms = {
        "Lobby": room_lobby,
        "Vault": room_vault,
        "Clerks": room_clerk,
        "Security": room_security,
        "Maintenance": room_maintenance,
        "Managers": room_manager,
        "Break": room_break,
        "Elevator": room_elevator,
        "Stairs": room_stairs,
        "Roof": room_roof,
        "Back": room_back,
        "Sewers": room_sewers
}