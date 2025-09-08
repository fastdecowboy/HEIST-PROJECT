from assets.items import *
from assets.map import *


guard = { 

        "name" : "guard",

        "description" : """
        
        This is a bank guard, they are dangerous and if they see you,
        your time till being caught will go down

        """,
        "items" : [item_baton, item_guard_uniform]

}

manager = {

        "id" : "manager",

        "name" : "The Manager of the bank",

        "description" : """

        A bank manager oversees daily operations, customer service,
        and staff coordination in a bank branch. Crucially, they are one of the few with access to the vault,
        making them essential for any heist involving secure bank areas.

        """,

        "items" : [item_keycard]

}

civilian = {
    
    "id" : "civilian",

    "name" : "civilian",

    "description" :

        """they offer potential to be taken as a hostage
        yet can also backfire and cause you to be seen, caught, or die so
        be careful.
        """,

    "items" : [ ]

}