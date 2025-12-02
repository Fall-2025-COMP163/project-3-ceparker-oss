[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wnCpjX4n)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21847120&assignment_repo_type=AssignmentRepo)
# COMP 163: Project 3 - Quest Chronicles

**AI Usage: Free Use (with explanation requirement)**

## Overview

Build a complete modular RPG adventure game demonstrating mastery of **exceptions and modules**.

## Getting Started

### Step 1: Accept Assignment
1. Click the assignment link provided in Blackboard
2. Accept the assignment - this creates your personal repository
3. Clone your repository to your local machine:
```bash
git clone [your-personal-repo-url]
cd [repository-name]
```

### Step 2: Understand the Project Structure

Your repository contains:

```
quest_chronicles/
├── main.py                     # Game launcher (COMPLETE THIS)
├── character_manager.py        # Character creation/management (COMPLETE THIS)
├── inventory_system.py         # Item and equipment management (COMPLETE THIS)
├── quest_handler.py            # Quest system (COMPLETE THIS)
├── combat_system.py            # Battle mechanics (COMPLETE THIS)
├── game_data.py                # Data loading and validation (COMPLETE THIS)
├── custom_exceptions.py        # Exception definitions (PROVIDED)
├── data/
│   ├── quests.txt             # Quest definitions (PROVIDED)
│   ├── items.txt              # Item database (PROVIDED)
│   └── save_games/            # Player save files (created automatically)
├── tests/
│   ├── test_module_structure.py       # Module organization tests
│   ├── test_exception_handling.py     # Exception handling tests
│   └── test_game_integration.py       # Integration tests
└── README.md                   # This file
```

### Step 3: Development Workflow

```bash
# Work on one module at a time
# Test your code frequently

# Commit and push to see test results
git add .
git commit -m "Implement character_manager module"
git push origin main

# Check GitHub for test results (green checkmarks = passed!, red xs = at least 1 failed test case. Click the checkmark or x and then "Details" to see what test cases passed/failed)
```

## Core Requirements (60 Points)

### Critical Constraint
You may **only** use concepts covered through the **Exceptions and Modules** chapters. 

### 🎨 Creativity and Customization

This project encourages creativity! Here's what you can customize:

**✅ FULLY CUSTOMIZABLE:**
- **Character stats** - Adjust health, strength, magic for balance
- **Enemy stats** - Make enemies easier or harder
- **Special abilities** - Design unique abilities for each class
- **Additional enemies** - Add your own enemy types beyond the required three
- **Game mechanics** - Add status effects, combos, critical hits, etc.
- **Quest rewards** - Adjust XP and gold amounts
- **Item effects** - Create unique items with creative effects

**⚠️ REQUIRED (for testing):**
- **4 Character classes:** Warrior, Mage, Rogue, Cleric (names must match exactly)
- **3 Enemy types:** "goblin", "orc", "dragon" (must exist, stats flexible)
- **All module functions** - Must have the specified function signatures
- **Exception handling** - Must raise appropriate exceptions

**💡 CREATIVITY TIPS:**
1. Start with required features working
2. Add creative elements incrementally
3. Test after each addition
4. Be ready to explain your design choices in the interview
5. Bonus interview points for thoughtful, balanced customization!

**Example Creative Additions:**
- Vampire enemy that heals when attacking
- Warrior "Last Stand" ability that activates when health is low
- Poison status effect that deals damage over time
- Critical hit system based on character stats
- Rare "legendary" weapons with special effects

### Module 1: custom_exceptions.py (PROVIDED - 0 points to implement)

**This module is provided complete.** It defines all custom exceptions you'll use throughout the project.

### Module 2: game_data.py (10 points)

### Module 3: character_manager.py (15 points)

### Module 4: inventory_system.py (10 points)

### Module 5: quest_handler.py (10 points)

### Module 6: combat_system.py (10 points)

### Module 7: main.py (5 points)

## Automated Testing & Validation (60 Points)

## Interview Component (40 Points)

**Creativity Bonus** (up to 5 extra points on interview):
- Added 2+ custom enemy types beyond required three
- Designed unique and balanced special abilities
- Implemented creative game mechanics (status effects, advanced combat, etc.)
- Thoughtful stat balancing with clear reasoning

**Note:** Creativity is encouraged, but functionality comes first! A working game with required features scores higher than a broken game with lots of extras.

### Update README.md

Document your project with:

1. **Module Architecture:** Explain your module organization
2. **Exception Strategy:** Describe when/why you raise specific exceptions
3. **Design Choices:** Justify major decisions
4. **AI Usage:** Detail what AI assistance you used
5. **How to Play:** Instructions for running the game

### What to Submit:

1. **GitHub Repository:** Your completed multi-module project
2. **Interview:** Complete 10-minute explanation session
3. **README:** Updated documentation

## Protected Files Warning

⚠️ **IMPORTANT: Test Integrity**

Test files are provided for your learning but are protected. Modifying test files constitutes academic dishonesty and will result in:

- Automatic zero on the project
- Academic integrity investigation

You can view tests to understand requirements, but any modifications will be automatically detected.
-MY READ_ME_
Module Architecture

Game_data-
Loads in quest data and items from their respective files to display to the user
Character_manager-
Creates your character and you choose a class, giving you options to save it,load it, and options based on if your character dies, your character's achievements, etc.
Inventory_system-
This will check your character's inventory,with options to use items within it, equip or unequip them, add them, remove them, all ensuring that it does not exceed its maximum of 20 items.

Quest_handler-
This will allow you to access different given quests, allowing you to accept them, drop them, see requirements for the quest, which will add to “completed_quest” if completed or “active_quest” if currently achieved, all being changed depending on how you complete these quests.
Combat_system-
This creates an enemy and puts you through a battle loop within the module, with you having special abilities based on your class, this loop will end once you or the enemy dies.
main-
This combines all functions to create a full menu of options, compiling to start or load a new file with characters, implementing every module based on your choices.

Except Strategy: 
Using try, any possible errors are caught, aligned with raise being used based on potential errors. 

EX:
t=line.split(“:”,1)
	If len(t) !=2:
		Raise InvalidDataFormatError(“Invalid Format”)
Checks that lines in the file in game_data has two parts when split 
These exceptions are used when a citation regarding the errors, like how this one is used when a invalid file formats used

Many other exceptions follow this with CombatNotActivEerror taking place if the corresponding action occurs where “self.combat” is not active in combat_system

Design Choices: 
I kept things simple, as I completed this based on the structure of the last two projects, with many of the personal choices coming from combat_system as I referred back to these projects to give the game an announcer-like presence when battling.

AI(chat.gpt): 
combat_system-AI Usage: Ai was used to check for errors, along with helping structure SimpleBattle and how to loop
and properly ensure when it was the player and enemy's turn in the game, the main errors were trying to regulate special abilities

character_manager-AI Usage: [Document any AI assistance used]
USED IT TO FIX save_character --> delete character, mainly to better understand directories and os
This module handles character creation, loading, and saving.

game_data-AI Usage: I used ai to help remind me on how to validate and structure the various dictionaries,
as I had multiple errors due to "Key_error" related issues



Inventory_system-AI Usage: Needed help on how to count on display_inventory with touch up issues based in adding items,
and checking items



main-AI Usage: Used to check errors on line 21 as it recommended me to import it this way

quest_handler-AI Usage: This was use for clean up purposes, along with checking for errors in getting the types of quest
Ai also help me again, as it also gave me a format for these types of functions
MAIN HELP: Prerequisite, as I needed to be informed how to gain a list backwards
This module handles quest management, dependencies, and completion.

How To play:
Hello Traveller! Like the rest this game is simple as when you go to the “main” file you're presented with the options: New Game,Load Game, and Exit.

This will present you with different ways to explore as it you select the following:

New_Game-
A new game will start with you creating a new character and a battle commencing based on your level, choose your name and class and battle forth
Load_game-
You already have a file? Great! You can commence there! And throughout commence your battles

Exit-
Boo! you simply just left, but at least you get a fair goodbye
