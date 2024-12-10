
#Defensive equipment player can find throughout the game. The user can "search" the room. 
#If the user finds the equipment they can then add the equipment in their inventory
defense_equipment = {
    "1x6 Wood": {
        "level_requirement": 1,
        "description": "A knotty piece of pine. Better than nothing.",
        "defense_value": 5,
        "attack_value": 5,
        "color": "tan",
        "weight": "heavy",
        "activation_button": "r",
        "number_of_allowed_uses": 7
    },
    "UV Light Wand": {
        "level_requirement": 3,
        "description": "Says, 'brighter than the sun' on the label. Can't catch me if they can't see me!",
        "defense_value": 5,
        "attack_value": 7,
        "color": "UV blue",
        "weight": "light",
        "activation_button": "r",
        "number_of_allowed_uses": 6
    },
    "Rusty Crowbar": {
        "level_requirement": 2,
        "description": "This thing is older than you, but it still packs a punch. Rust might be your biggest enemy.",
        "defense_value": 8,
        "attack_value": 10,
        "color": "dark red",
        "weight": "very heavy",
        "activation_button": "r",
        "number_of_allowed_uses": 10
    },
    "Iron Skillet": {
        "level_requirement": 1,
        "description": "This cast-iron skillet isn't just for breakfast. Block and bash with the best of them.",
        "defense_value": 10,
        "attack_value": 7,
        "color": "black",
        "weight": "very heavy",
        "activation_button": "r",
        "number_of_allowed_uses": 12
    },
    "Broken Mirror Shard": {
        "level_requirement": 1,
        "description": "A sharp shard of mirror glass. Looks cursed, but it's sharp as a razor.",
        "defense_value": 2,
        "attack_value": 15,
        "color": "shiny silver",
        "weight": "light",
        "activation_button": "r",
        "number_of_allowed_uses": 3
    },
    "Silver Crucifix": {
        "level_requirement": 4,
        "description": "A holy relic blessed by an unknown priest. Good for more than just scaring off vampires.",
        "defense_value": 15,
        "attack_value": 0,
        "color": "shiny silver",
        "weight": "light",
        "activation_button": "r",
        "number_of_allowed_uses": 5
    },
    "Fire Extinguisher": {
        "level_requirement": 2,
        "description": "Not just for fires. It sprays foam and doubles as a battering ram.",
        "defense_value": 12,
        "attack_value": 5,
        "color": "red",
        "weight": "very heavy",
        "activation_button": "r",
        "number_of_allowed_uses": 3
    },
    "Plague Doctor Mask": {
        "level_requirement": 5,
        "description": "An old, creepy plague doctor mask. Breathing in it isn't great, but it hides your scent from certain enemies.",
        "defense_value": 20,
        "attack_value": 0,
        "color": "black and white",
        "weight": "medium",
        "activation_button": "r",
        "number_of_allowed_uses": 99
    }
}



# There should be some items that are found that don't contribute directly to greater attack or defense, but 
# do allow for easier gameplay. The player should get rewarded for spending time exploring the game.
special_items = {
    "Radio": {
        "level_requirement": 1,
        "description": "A dusty old 'walky talky', the radio lights a little low, but it seems to work",
        "battery_level": 6,
        "special_attribute": "talks to dead people",
        "custom_values": ["grandpa", "uncle", "unknown soldier"],
        "activation_button": "e"
    },
    "Skeleton Key": {
        "level_requirement": 3,
        "description": "An ancient key that seems to open almost any lock. Feels cold to the touch.",
        "battery_level": "N/A",
        "special_attribute": "unlocks secret rooms and chests",
        "custom_values": ["chest", "hidden passage", "trapdoor"],
        "activation_button": "e"
    },
    "Flashlight": {
        "level_requirement": 1,
        "description": "Shines brightly. You don't want to be in the dark without it.",
        "battery_level": 10,
        "special_attribute": "reveals hidden items",
        "custom_values": ["hidden clue", "secret passage"],
        "activation_button": "f"
    },
    "Compass of Lies": {
        "level_requirement": 5,
        "description": "A compass that doesn't always point north. Sometimes it points to... something else.",
        "battery_level": "infinite",
        "special_attribute": "points to hidden dangers or opportunities",
        "custom_values": ["enemy", "treasure", "trap"],
        "activation_button": "c"
    },
    "Music Box": {
        "level_requirement": 2,
        "description": "A rusty music box. Play its haunting melody to entrance nearby enemies.",
        "battery_level": "wind-up",
        "special_attribute": "puts enemies to sleep",
        "custom_values": ["ghost", "phantom", "zombie"],
        "activation_button": "m"
    },
    "Ancient Amulet": {
        "level_requirement": 4,
        "description": "A mysterious amulet engraved with symbols. It hums softly in your hand.",
        "battery_level": "infinite",
        "special_attribute": "grants temporary invulnerability",
        "custom_values": ["spiritual protection", "ward against possession"],
        "activation_button": "a"
    }
}

apparel = {
    "head": {
        "bald": "no hair",
        "witch hat": "pointy purple witch hat",
        "cowboy hat": "worn-out brown cowboy hat",
        "gas mask": "old military-grade gas mask"
    },
    "camera": {
        "Nikon": "Nikon Camera",
        "Polaroid": "Polaroid instant camera",
        "Surveillance Drone": "Small surveillance drone (hands-free)"
    },
    "shirt": {
        "t-shirt": ["Metallica t-shirt", "plain white t-shirt", "polo t-shirt"],
        "jacket": ["leather jacket", "raincoat", "hooded cloak"]
    },
    "pants": {
        "jeans": ["blue jeans", "ripped jeans", "cargo pants"],
        "formal": ["slacks", "dress pants"],
        "other": ["shorts", "capris", "skirt", "athletic shorts"]
    },
    "shoes": {
        "casual": ["sneakers", "Converse", "loafers"],
        "formal": ["dress shoes", "penny loafers"],
        "fancy": ["high heels", "platform boots"],
        "outdoors": ["hiking boots", "combat boots"]
    },
    "gloves": {
        "none": "bare hands",
        "leather gloves": "black leather gloves",
        "garden gloves": "thick green garden gloves",
        "winter gloves": "fuzzy winter mittens"
    },
    "backpack": {
        "none": "no backpack",
        "standard": "worn-out school backpack",
        "military": "military-grade tactical pack",
        "satchel": "small brown leather satchel"
    }
}


