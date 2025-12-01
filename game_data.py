"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: Chase Parker

AI Usage: I used ai to help remidn me on how to validate and structure the various dictionaries, 
as I had mutliple errors due to "Key_error" related issues

This module handles loading and validating game data from text files.
"""

import os
from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================
#This will load the quest file in the data directory striping it of any newlines
#and then creating a new dictionary with these quest
def load_quests(filename="data/quests.txt"):
    """
    Load quest data from file
    
    Expected format per quest (separated by blank lines):
    QUEST_ID: unique_quest_name
    TITLE: Quest Display Title
    DESCRIPTION: Quest description text
    REWARD_XP: 100
    REWARD_GOLD: 50
    REQUIRED_LEVEL: 1
    PREREQUISITE: previous_quest_id (or NONE)
    
    Returns: Dictionary of quests {quest_id: quest_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle:
    # - FileNotFoundError → raise MissingDataFileError
    # - Invalid format → raise InvalidDataFormatError
    # - Corrupted/unreadable data → raise CorruptedDataError
   #AI AID
    
    try:
        quests = {}
        current = {}
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    if "quest_id" in current:
                        quests[current["quest_id"]] = current
                    current = {}
                    continue
                
                t = line.split(":", 1)
                if len(t) != 2:
                    raise InvalidDataFormatError("InvalidDataFormatError")
                key = t[0].strip()
                val = t[1].strip()
                if key == "QUEST_ID":
                    current["quest_id"] = val
                elif key == "TITLE":
                    current["title"] = val
                elif key == "DESCRIPTION":
                    current["description"] = val
                elif key == "REWARD_XP":
                    current["reward_xp"] = int(val)
                elif key == "REWARD_GOLD":
                    current["reward_gold"] = int(val)
                elif key == "REQUIRED_LEVEL":
                    current["required_level"] = int(val)
                elif key == "PREREQUISITE":
                    current["prerequisite"] = val
        if "quest_id" in current:
            quests[current["quest_id"]] = current

        return quests

    except FileNotFoundError:
        raise MissingDataFileError("File not found: ")
    except InvalidDataFormatError:
        raise
    except Exception:
        raise CorruptedDataError("CorruptedDataError")
#This will load the items file in the data directory striping it of any newlines
#and then creating a new dictionary with these items
def load_items(filename="data/items.txt"):
    """
    Load item data from file
    
    Expected format per item (separated by blank lines):
    ITEM_ID: unique_item_name
    NAME: Item Display Name
    TYPE: weapon|armor|consumable
    EFFECT: stat_name:value (e.g., strength:5 or health:20)
    COST: 100
    DESCRIPTION: Item description
    
    Returns: Dictionary of items {item_id: item_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle same exceptions as load_quests
    
    try:
            items = {}
            current = {}
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line == "":
                        if "item_id" in current:
                            items[current["item_id"]] = current
                        current = {}
                        continue
                    t = line.split(":", 1)
                    if len(t) != 2:
                        raise InvalidDataFormatError("InvalidDataFormatError")
                    key = t[0].strip()
                    val = t[1].strip()
                    if key == "ITEM_ID":
                        current["item_id"] = val
                    elif key == "NAME":
                        current["name"] = val
                    elif key == "TYPE":
                        current["type"] = val
                    elif key == "EFFECT":
                        parts = val.split(":", 1)
                        if len(parts) != 2:
                            raise InvalidDataFormatError("Invalid EFFECT")
                
                        current["effect"] = {parts[0].strip(): int(parts[1].strip())} 
                    elif key == "COST":
                        current["cost"] = int(val)
                    elif key == "DESCRIPTION":
                        current["description"] = val

                    else:
                        raise InvalidDataFormatError("Unknown field error")
            if "item_id" in current:
                items[current["item_id"]] = current
            return items
    except FileNotFoundError:
            raise MissingDataFileError("File not found")
    except InvalidDataFormatError:
            raise
    except Exception as e:
            raise CorruptedDataError("CorruptedDataError")
#ensures that the quest loaded, has all mathcing requirments to be loaded in
def validate_quest_data(quest_dict):
    """
    Validate that quest dictionary has all required fields
    
    Required fields: quest_id, title, description, reward_xp, 
                    reward_gold, required_level, prerequisite
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields
    """
    # TODO: Implement validation
    # Check that all required keys exist
    # Check that numeric values are actually numbers
    required_fields = [
        "quest_id",
        "title",
        "description",
        "reward_xp",
        "reward_gold",
        "required_level",
        "prerequisite"
    ]
    for field in required_fields:
        if field not in quest_dict:
            raise InvalidDataFormatError("InvalidDataFormatError Valadate Quest")
    numeric_fields = ["reward_xp", "reward_gold", "required_level"]
    for field in numeric_fields:
        value = quest_dict[field]
        if not isinstance(value, int):
            try:
                int(value)
            except:
                raise InvalidDataFormatError("Invalid number feild")
    
    return True
#ensures that the items loaded, has all mathcing requirments to be loaded in
def validate_item_data(item_dict):
    """
    Validate that item dictionary has all required fields
    
    Required fields: item_id, name, type, effect, cost, description
    Valid types: weapon, armor, consumable
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields or invalid type
    """
    # TODO: Implement validation
    required_fields = [
        "item_id",
        "name",
        "type",
        "effect",
        "cost",
        "description"
    ]
    for field in required_fields:
        if field not in item_dict:
            raise InvalidDataFormatError("Missing required field")
    valid_types = {"weapon", "armor", "consumable"}
    if item_dict["type"] not in valid_types:
        raise InvalidDataFormatError(f"Invalid item type: {item_dict['type']}")
    #Might be EFFECT
    effect = item_dict["effect"]
    if ":" not in effect:
        raise InvalidDataFormatError("Invalid effect format")
    parts = effect.split(":")
    if len(parts) != 2:
        raise InvalidDataFormatError("Invalid effect format Length")
    stat_name = parts[0].strip()
    stat_value = parts[1].strip()
    if len(stat_name)==0:
        raise InvalidDataFormatError("Cannot be empty.")
    try:
        int(stat_value)
    except:
        raise InvalidDataFormatError("Must be numeric")
    return True
#if not created, we create our own files just in case the files not found
def create_default_data_files():
    """
    Create default data files if they don't exist
    This helps with initial setup and testing
    """
    # TODO: Implement this function
    # Create data/ directory if it doesn't exist
    # Create default quests.txt and items.txt files
    # Handle any file permission errors appropriately

    if not os.path.exists("data/quests.txt"):
        with open("data/quests.txt","w") as file:
            file.write("QUEST_ID: first_steps\n")
            file.write("TITLE: First Steps\n")
            file.write("DESCRIPTION: Begin your adventure.\n")
            file.write("REWARD_XP: 50\n")       
            file.write("REWARD_GOLD: 25\n")          
            file.write("REQUIRED_LEVEL: 1\n")    
            file.write("PREREQUISITE: NONE")          
    if not os.path.exists("data/items.txt"):
        with open("data/items.txt","w") as file:
            file.write("ITEM_ID: health_potion\n")
            file.write("NAME: Health Potion\n")
            file.write("TYPE: consumable\n")
            file.write("EFFECT: health:20\n")       
            file.write("COST: 25\n")          
            file.write("DESCRIPTION: Restores 20 health points")    
        





    

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
#checks for errors and creates another dicitonary with thes quest in place
def parse_quest_block(lines):
    """
    Parse a block of lines into a quest dictionary
    
    Args:
        lines: List of strings representing one quest
    
    Returns: Dictionary with quest data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    # Split each line on ": " to get key-value pairs
    # Convert numeric strings to integers
    # Handle parsing errors gracefully
    
    if len(lines) == 0:
        raise InvalidDataFormatError("Empty quest block")
    quest = {}
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(":", 1)
        if len(parts) != 2:
            raise InvalidDataFormatError("Invalid line format: " + line)
        key = parts[0].strip()
        val = parts[1].strip()
        try:
            if key == "QUEST_ID":
                quest["quest_id"] = val
            elif key == "TITLE":
                quest["title"] = val
            elif key == "DESCRIPTION":
                quest["description"] = val
            elif key == "REWARD_XP":
                quest["reward_xp"] = int(val)
            elif key == "REWARD_GOLD":
                quest["reward_gold"] = int(val)
            elif key == "REQUIRED_LEVEL":
                quest["required_level"] = int(val)
            elif key == "PREREQUISITE":
                quest["prerequisite"] = val
            else:
                raise InvalidDataFormatError("Unknown field: ")
        except ValueError:
            raise InvalidDataFormatError("Invalid numeric value: ")

    return quest
#checks for errors and creates another dicitonary with thes items in place
def parse_item_block(lines):
    """
    Parse a block of lines into an item dictionary
    
    Args:
        lines: List of strings representing one item
    
    Returns: Dictionary with item data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic

    if len(lines) == 0:
        raise InvalidDataFormatError("Empty quest block")
    line_dict = {}
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(":", 1)
        if len(parts) != 2:
            raise InvalidDataFormatError("Invalid line format: " + line)
        key = parts[0].strip()
        val = parts[1].strip()
        try:
            if key == "ITEM_ID":
                line_dict["item_id"] = val
            elif key == "NAME":
                line_dict["name"] = val
            elif key == "TYPE":
                line_dict["type"] = val
            elif key == "EFFECT":
                line_dict["effect"] = val
            elif key == "COST":
                line_dict["cost"] = int(val)
            elif key == "DESCRIPTION":
                line_dict["description"] =val
            
            else:
                raise InvalidDataFormatError("Unknown field: ")
        except ValueError:
            raise InvalidDataFormatError("Invalid numeric value: ")

    return line_dict
    
    

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")
    
    # Test creating default files
    # create_default_data_files()
    
    # Test loading quests
    try:
         quests = load_quests()
         print(f"Loaded {len(quests)} quests")
    except MissingDataFileError:
         print("Quest file not found")
    except InvalidDataFormatError as e:
         print(f"Invalid quest format: {e}")
    
    # Test loading items
    try:
        items = load_items()
        print(f"Loaded {len(items)} items")
    except MissingDataFileError:
         print("Item file not found")
    except InvalidDataFormatError as e:
         print(f"Invalid item format: {e}")

