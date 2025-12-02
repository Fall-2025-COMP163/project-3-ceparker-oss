"""
COMP 163 - Project 3: Quest Chronicles
Main Game Module - Starter Code

Name: Chase Parker

AI Usage: Used to check errors on line 21 as it recommended me to import it this way

This is the main game file that ties all modules together.
Demonstrates module integration and complete game flow.
"""

# Import all our custom modules
import character_manager
import inventory_system
import quest_handler
import combat_system
import game_data
from custom_exceptions import *
#from combat_system import battle
from combat_system import SimpleBattle, get_random_enemy_for_level
# ============================================================================
# GAME STATE
# ============================================================================

# Global variables for game data
current_character = None
all_quests = {}
all_items = {}
game_running = False

# ============================================================================
# MAIN MENU
# ============================================================================
#gives the the three primary options to begin your game
def main_menu():
    """
    Display main menu and get player choice
    
    Options:
    1. New Game
    2. Load Game
    3. Exit
    
    Returns: Integer choice (1-3)
    """
    # TODO: Implement main menu display
    # Show options
    # Get user input
    # Validate input (1-3)
    # Return choice
    input_opt=int(input("1. New Game|2. Load Game|3.Exit"))
    return input_opt

    
#new game is option 1, creating you a new character 
def new_game():
    """
    Start a new game
    
    Prompts for:
    - Character name
    - Character class
    
    Creates character and starts game loop
    """
    global current_character
    
    # TODO: Implement new game creation
    # Get character name from user
    # Get character class from user
    # Try to create character with character_manager.create_character()
    # Handle InvalidCharacterClassError
    # Save character
    # Start game loop
    char_name=input("Name")
    char_class=input("Class")
    current_character=character_manager.create_character(char_name,char_class)
    character_manager.save_character(current_character)
    game_loop()
    pass
#Loads an existing hame and loads an old character
def load_game():
    """
    Load an existing saved game
    
    Shows list of saved characters
    Prompts user to select one
    """
    global current_character
    
    # TODO: Implement game loading
    # Get list of saved characters
    # Display them to user
    # Get user choice
    # Try to load character with character_manager.load_character()
    # Handle CharacterNotFoundError and SaveFileCorruptedError
    # Start game loop
    character_manager.load_character(current_character)
    character_manager.list_saved_characters()
    #explaiend below
    game_loop()
    
    pass

# ============================================================================
# GAME LOOP
# ============================================================================
#base don your choice, and the games running you can view differnt things about your character
def game_loop():
    """
    Main game loop - shows game menu and processes actions
    """
    global game_running, current_character
    
    game_running = True
    
    # TODO: Implement game loop
    # While game_running:
    #   Display game menu
    #   Get player choice
    #   Execute chosen action
    #   Save game after each action
    choice=game_menu()
    while game_running:
        if choice==1:
            view_character_stats()
        elif choice==2:
            view_inventory()
        elif choice==3:
            quest_menu()
        elif choice==4:
            explore()
        elif choice==5:
            shop()
        elif choice==6:
            break
        save_game()
    
#asks for your input_opt so "choice" in the fuction above can call differnt actions
def game_menu():
    """
    Display game menu and get player choice
    
    Options:
    1. View Character Stats
    2. View Inventory
    3. Quest Menu
    4. Explore (Find Battles)
    5. Shop
    6. Save and Quit
    
    Returns: Integer choice (1-6)
    """
    # TODO: Implement game menu
    input_opt=int(input("1. View Character Stats|2. View Inventory|3.Quest Menu| 4. Explore (Find Battles)|5. Shop|6. Save and Quit"))
    return input_opt
# ============================================================================
# GAME ACTIONS
# ============================================================================
#action 1 will use the imported display_stats to continue
def view_character_stats():
    """Display character information"""
    global current_character,all_quests
    
    # TODO: Implement stats display
    # Show: name, class, level, health, stats, gold, etc.
    # Use character_manager functions
    # Show quest progress using quest_handler
    print(current_character)
    quest_handler.display_character_quest_progress(current_character, all_quests)
    #Potential error
    pass
#action 2 will use the imported display_inventory to continue
def view_inventory():
    """Display and manage inventory"""
    global current_character, all_items
    
    # TODO: Implement inventory menu
    # Show current inventory
    # Options: Use item, Equip weapon/armor, Drop item
    # Handle exceptions from inventory_system
    print(inventory_system.display_inventory(current_character, all_items))
    
#action 3 will use the imported quest handlers askign for input to check the quest you can acces
#abandon,accept,etc
def quest_menu():
    """Quest management menu"""
    global current_character, all_quests
    
    # TODO: Implement quest menu
    # Show:
    #   1. View Active Quests
    #   2. View Available Quests
    #   3. View Completed Quests
    #   4. Accept Quest
    #   5. Abandon Quest
    #   6. Complete Quest (for testing)
    #   7. Back
    # Handle exceptions from quest_handler
    
    input_opt=int(input("1. View Active Quests|2. View Available Quests|3. View Completed Quests|4. Accept Quest| 5. Abandon Quest|6. Complete Quest (for testing)| 7. Back"))
    if input_opt==1:
        print(quest_handler.get_active_quests(current_character, all_quests))
    elif input_opt==2:
       print(quest_handler.get_available_quests(current_character, all_quests))
    elif input_opt==3:
        print(quest_handler.get_completed_quests(current_character, all_quests))
    elif input_opt==4:
        print(quest_handler.accept_quest(current_character,"first_quest", all_quests))
    elif input_opt==5:
        print(quest_handler.abandon_quest(current_character, all_quests))
    elif input_opt==6:
        print(quest_handler.complete_quest(current_character,"first_quest", all_quests))
    
# action 4 explore will acces the combat system module and starst a battle base don your class
def explore():
    """Find and fight random enemies"""
    global current_character
    
    # TODO: Implement exploration
    # Generate random enemy based on character level
    # Start combat with combat_system.SimpleBattle
    # Handle combat results (XP, gold, death)
    # Handle exceptions

    enemy = combat_system.get_random_enemy_for_level(current_character["level"])
    fight = combat_system.SimpleBattle(current_character, enemy)
    result = fight.start_battle()
    print(result)
#action 5, will acces all items avalabel to buy and will ask if you want to buy an item
def shop():
    """Shop menu for buying/selling items"""
    global current_character, all_items
    
    # TODO: Implement shop
    # Show available items for purchase
    # Show current gold
    # Options: Buy item, Sell item, Back
    # Handle exceptions from inventory_system
    print(all_items)
    print(current_character["gold"])
    input_opt=int(input("1.Buy item, 2.Sell item, 3.Back"))
    int_item=input()
    if input_opt==1:
        inventory_system.purchase_item(current_character, int_item, all_items)
    
    elif input_opt==2:
        inventory_system.sell_item(current_character, int_item, all_items)

    elif input_opt==3:
        return None
# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
#will use the charcter_manager to save your current character
def save_game():
    """Save current game state"""
    global current_character
    
    # TODO: Implement save
    # Use character_manager.save_character()
    # Handle any file I/O exceptions
    character_manager.save_character(current_character)
    pass
#will load the needed items and quest, and like said, if not found, it create a default set of quest and items
def load_game_data():
    """Load all quest and item data from files"""
    global all_quests, all_items
    
    # TODO: Implement data loading
    # Try to load quests with game_data.load_quests()
    # Try to load items with game_data.load_items()
    # Handle MissingDataFileError, InvalidDataFormatError
    # If files missing, create defaults with game_data.create_default_data_files()
    try:
        game_data.load_quests()
        game_data.load_items()
    except:
        game_data.create_default_data_files()
    pass
#handles what to do if the charcter dies, as you can choose if you want to revive your charcter at the cost of gold
def handle_character_death():
    """Handle character death"""
    global current_character, game_running
    
    # TODO: Implement death handling
    # Display death message
    # Offer: Revive (costs gold) or Quit
    # If revive: use character_manager.revive_character()
    # If quit: set game_running = False
    if character_manager.is_character_dead(current_character)==True:
        print("Character is dead, you can revive..for a price")
    input_choice=input("Offer: Revive (costs gold) or Quit")
    if input_choice=="revive" or input_choice=="revive":
        character_manager.revive_character()
    elif quit:
        game_running = False

def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("     QUEST CHRONICLES - A MODULAR RPG ADVENTURE")
    print("=" * 50)
    print("\nWelcome to Quest Chronicles!")
    print("Build your character, complete quests, and become a legend!")
    print()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main game execution function"""
    
    # Display welcome message
    display_welcome()
    
    # Load game data
    try:
        load_game_data()
        print("Game data loaded successfully!")
    except MissingDataFileError:
        print("Creating default game data...")
        game_data.create_default_data_files()
        load_game_data()
    except InvalidDataFormatError as e:
        print(f"Error loading game data: {e}")
        print("Please check data files for errors.")
        return
    
    # Main menu loop
    while True:
        choice = main_menu()
        
        if choice == 1:
            new_game()
        elif choice == 2:
            load_game()
        elif choice == 3:
            print("\nThanks for playing Quest Chronicles!")
            break
        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()

