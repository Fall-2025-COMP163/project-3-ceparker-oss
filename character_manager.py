"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: Chase Parker

AI Usage: [Document any AI assistance used]
USED IT TO FIX save_character --> delete chaarcter, mainly to bette rundetsatnd directories and os
This module handles character creation, loading, and saving.
"""

import os
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    level=1
    experience=0
    gold=100
    inventory=[]
    active_quests=[]
    completed_quests=[]
    if character_class=="Warrior":
        health=120
        strength=15
        magic=5
    elif character_class=="Mage":
        health=80
        strength=8
        magic=20
    elif character_class=="Rogue":
        health=90
        strength=12
        magic=10
    elif character_class=="Cleric":
        health=100
        strength=10
        magic=15
    else:
        raise InvalidCharacterClassError("Invalid Class")
    my_dict={"name":name,
            "class":character_class,
            "level":level,
            "health":health,
            "max_health":health,
            "strength":strength,
            "magic":magic,
            "experience":experience,
            "gold":gold,
            "inventory":inventory,
            "active_quests":active_quests,
            "completed_quests":completed_quests}
    return my_dict
    pass

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    #Possibly error in error placement
    if not os.path.exists(save_directory):
        raise IOError("Save directory does not exist")
    
    filename = f"{character['name']}_save.txt"
    filepath = os.path.join(save_directory, filename)
    inventory = ",".join(character["inventory"])
    active_quests = ",".join(character["active_quests"])
    completed_quests = ",".join(character["completed_quests"])
    with open(filepath,"w") as file:
        file.write(f"NAME: {character['name']}\n")
        file.write(f"CLASS: {character['class']}\n")
        file.write(f"LEVEL: {character['level']}\n")
        file.write(f"HEALTH: {character['health']}\n")
        file.write(f"MAX_HEALTH: {character['max_health']}\n")
        file.write(f"STRENGTH: {character['strength']}\n")
        file.write(f"MAGIC: {character['magic']}\n")
        file.write(f"EXPERIENCE: {character['experience']}\n")
        file.write(f"GOLD: {character['gold']}\n")
        file.write(f"INVENTORY: {inventory}\n")
        file.write(f"ACTIVE_QUESTS: {active_quests}\n")
        file.write(f"COMPLETED_QUESTS: {completed_quests}")

    if os.path.isfile(filepath):
        return True
    #Possibly error in error placement
    else:
        raise PermissionError("Permission Error")
    

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    filename = f"{character_name}_save.txt"
    filepath = os.path.join(save_directory, filename)
    with open(filepath,'r') as file:
        chr_dict={}
        file_read=file.readlines()
        for i in file_read:
            t=i.split(":")
            key=t[0]
            val=t[1].strip()
            if key=="NAME":
               chr_dict['name']=val
            elif key=="CLASS":
               chr_dict["class"]=val
            elif key=="LEVEL":
               chr_dict["level"]=int(val)
            elif key=="HEALTH":
               chr_dict["health"]=int(val)
            elif key=="MAX_HEALTH":
               chr_dict["max_health"]=int(val)   
            elif key=="STRENGTH":
               chr_dict["strength"]=int(val)
            elif key=="MAGIC":
               chr_dict["magic"]=int(val)
            elif key=="EXPERIENCE":
               chr_dict["experience"]=int(val)
            elif key=="GOLD":
               chr_dict["gold"]=int(val)
            elif key=="INVENTORY":
               chr_dict["inventory"]=val
            elif key=="ACTIVE_QUESTS":
               chr_dict["active_quests"]=val
            elif key=="COMPLETED_QUESTS":
               chr_dict["completed_quests"]=val
        return chr_dict 

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    if not os.path.exists(save_directory):
        return []
    my_list=[]
    for dirname, subdirs, files in os.walk(save_directory):
        for filename in files:
            if len(filename) > 9:
                if filename[-9:] == "_save.txt":
                    char_name = filename[:-9]
                    my_list.append(char_name)

    return my_list
    pass

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion

    filename = f"{character_name}_save.txt"
    filepath = os.path.join(save_directory, filename)
    if not os.path.isfile(filepath):
        raise CharacterNotFoundError("CharacterNotFoundError")
    try:
        os.remove(filepath)
        return True
    except:
        raise
    
    pass

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    if character["health"]==0:
        raise CharacterDeadError("CharacterDeadError")
    #AI Recomended
    character["experience"] += xp_amount
    while character["experience"] >= character["level"] * 100:
        character["level"] += 1
        character["max_health"] += 10
        character["strength"] += 2
        character["magic"] += 2
        character["health"] = character["max_health"]
    pass

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    if character["gold"]+amount<0:
        raise ValueError("Value Error")
    else:
        char=character["gold"]+amount
        character["gold"]=char
        return char
    

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    if amount<character["max_health"]:
       if amount+ character["health"] < character["max_health"]:
            amt=character["health"]+amount
            character["health"]=amt
            return amt
    

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    if character["health"]==0:
        return True
    else:
        return False
    

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    if character["health"] <= 0:
        character["health"] = character["max_health"] // 2
        return True
    return False
    

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    required_feild=["name", "class", "level", "health", "max_health", 
                    "strength", "magic", "experience", "gold", "inventory",
                    "active_quests", "completed_quests"]

    for feild in required_feild:
        if feild not in character:
            raise InvalidSaveDataError("InvalidSaveDataError")
    numeric_feild=["level", "health", "max_health",
        "strength", "magic", "experience", "gold"]
    for field in numeric_feild:
        if not isinstance(character[field],int):
            raise InvalidSaveDataError("InvalidSaveDataError for numeric_feild")
    list_feild=["inventory", "active_quests", "completed_quests"]
    for feild in list_feild:
        if not isinstance(character[field],list):
            raise InvalidSaveDataError("InvalidSaveDataError for list_feild")
    return True

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    try:
        char = create_character("TestHero", "Warrior")
        print(char["name"])
        print(f"Created: {char['name']} the {char['class']}")
        print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    except InvalidCharacterClassError as e:
        print(f"Invalid class: {e}")
    
    # Test saving
    try:
         save_character(char)
         print("Character saved successfully")
    except Exception as e:
         print(f"Save error: {e}")
    
    # Test loading
    try:
         loaded = load_character("TestHero")
         print(f"Loaded: {loaded['name']}")
    except CharacterNotFoundError:
         print("Character not found")
    except SaveFileCorruptedError:
        print("Save file corrupted")

