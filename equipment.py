
#Defensive equipment player can find throughout the game. The user can "search" the room. 
#If the user finds the equipment they can then add the equipment in their inventory
defense_equipment = {
                     "1x6 Wood" : {"level_requirement": 1,
                                   "description": "A knotty piece of pine. Better than nothing.",
                                   "defense_value": 5,
                                   "attack_value": 5,
                                   "color": "tan",
                                   "weight": "heavy",
                                   "activation_button": "r",
                                   "number_of_allowed_uses": 7},

                     "UV Light Wand": {"level requirement": 3,
                                       "description": "Says, 'brighter than the sun' on the label. Can't catch me if they can't see me!",
                                       "defense_value": 5,
                                       "attack_value": 7,
                                       "color": "UV blue",
                                       "weight": "light",
                                       "activation_button" : "r",
                                       "number_of_allowed_uses" : 6}
}



# There should be some items that are found that don't contribute directly to greater attack or defense, but 
# do allow for easier gameplay. The player should get rewarded for spending time exploring the game.
special_items = {
                 "radio": {"level_requirement": 1,
                           "description": "A dusty old 'walky talky', the radio lights a little low, but it seems to work",
                           "battery_level": 6,
                           "special_attribute": "talks to dead people",
                           "custom_values": ["grandpa", "uncle", "unknown soldier"],
                           "activation_button": "e"}

}



apparel = {
           "head": {"bald": "no hair"},
           "camera": {"Nikon": "Nikon Camera"},
           "shirt": {"t-shirt": ["metallica t-shirt", "white t-shirt", "polo t-shirt"]},
           "pants": {"pants" : ["blue jeans, shorts, slacks, skirt, dress, capris"]},
           "shoes": {"shoes": ["high tops", "sneakers", "converse", "flats", "high heels"]}

}

