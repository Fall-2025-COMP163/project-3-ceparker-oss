"""
COMP 163 - Project 3: Quest Chronicles
Combat System Module - Starter Code

Name: Chase Parker

AI Usage: [Document any AI assistance used]

Handles combat mechanics
"""

from custom_exceptions import (
    InvalidTargetError,
    CombatNotActiveError,
    CharacterDeadError,
    AbilityOnCooldownError
)

# ============================================================================
# ENEMY DEFINITIONS
# ============================================================================

def create_enemy(enemy_type):
    """
    Create an enemy based on type
    
    Example enemy types and stats:
    - goblin: health=50, strength=8, magic=2, xp_reward=25, gold_reward=10
    - orc: health=80, strength=12, magic=5, xp_reward=50, gold_reward=25
    - dragon: health=200, strength=25, magic=15, xp_reward=200, gold_reward=100
    
    Returns: Enemy dictionary
    Raises: InvalidTargetError if enemy_type not recognized
    """
    # TODO: Implement enemy creation
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    my_dict={}
    if enemy_type=="goblin":
        health=50
        strength=8
        magic=2
        xp_reward=25
        gold_reward=10
        
    elif enemy_type=="orc":
        health=80
        strength=12
        magic=5
        xp_reward=50
        gold_reward=25
        
    elif enemy_type=="dragon":
        health=200
        strength=25
        magic=15
        xp_reward=200
        gold_reward=100
    else:
        raise InvalidTargetError("Invalid Target")
        
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    my_dict={"name":enemy_type, 
            "health":health,
            "max_health":health, 
            "strength":strength, 
            "Magic":magic, 
            "xp_reward":xp_reward, 
            "gold_reward":gold_reward}
    return  my_dict            
        

def get_random_enemy_for_level(character_level):
    """
    Get an appropriate enemy for character's level
    
    Level 1-2: Goblins
    Level 3-5: Orcs
    Level 6+: Dragons
    
    Returns: Enemy dictionary
    """
    # TODO: Implement level-appropriate enemy selection
    # Use if/elif/else to select enemy type
    # Call create_enemy with appropriate type
    if character_level<=2:
        create_enemy("goblin")
    elif character_level<=5:
        create_enemy("orc")
    else:
        create_enemy("dragon")
    pass

# ============================================================================
# COMBAT SYSTEM
# ============================================================================

class SimpleBattle:
    """
    Simple turn-based combat system
    
    Manages combat between character and enemy
    """
    
    def __init__(self, character, enemy):
        """Initialize battle with character and enemy"""
        # TODO: Implement initialization
        # Store character and enemy
        # Set combat_active flag
        # Initialize turn counter
        self.character=character
        self.enemy=enemy
        self.turn=1
        self.combat_active=True
        pass
    
    def start_battle(self):
        """
        Start the combat loop
        
        Returns: Dictionary with battle results:
                {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
        
        Raises: CharacterDeadError if character is already dead
        """
        award_dict={}
        if self.character["health"]==0:
                raise  CharacterDeadError("CharacterDeadError")
        while self.combat_active==True:
            self.player_turn()
            if self.enemy["health"]<=0:
                reward=get_victory_rewards(self.enemy)
                award_dict["winner"]=self.check_battle_end()
                award_dict["xp_gained"]=reward["xp"]
                award_dict["gold_gained"]=reward["gold"]
                self.combat_active=False
                return award_dict

            self.enemy_turn()
            print(self.character["health"])
            print(self.enemy["health"])
            if self.character["health"]==0:
                raise  CharacterDeadError("CharacterDeadError")
       
       
        # TODO: Implement battle loop
        # Check character isn't dead
        # Loop until someone dies
        # Award XP and gold if player wins

        
    
    def player_turn(self):
        """
        Handle player's turn
        
        Displays options:
        1. Basic Attack
        2. Special Ability (if available)
        3. Try to Run
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement player turn
        # Check combat is active
        # Display options
        # Get player choice
        # Execute chosen action
        input_option=int(input())
        self.turn=1
        if self.turn==1:
            if  self.combat_active==True:
                print(" 1. Basic Attack|2. Special Ability (if available)|3. Try to Run")
                if input_option==1:
                    
                    self.apply_damage(self.enemy, self.calculate_damage(self.character, self.enemy))
                if input_option==2:
                    use_special_ability(self.character, self.enemy)

                if input_option==3:
                   self.attempt_escape()
            else:
                raise CombatNotActiveError("Combat is not active")
    
    def enemy_turn(self):
        """
        Handle enemy's turn - simple AI
        
        Enemy always attacks
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement enemy turn
        # Check combat is active
        # Calculate damage
        # Apply to character
        self.turn=2
        if  self.combat_active==True:
            if self.turn==2:
                self.apply_damage( self.character, self.calculate_damage(self.enemy, self.character))
        
        else:
            raise CombatNotActiveError("Combat is not active")
    def calculate_damage(self, attacker, defender):
        """
        Calculate damage from attack
        
        Damage formula: attacker['strength'] - (defender['strength'] // 4)
        Minimum damage: 1
        
        Returns: Integer damage amount
        """
        # TODO: Implement damage calculation
        damage=attacker['strength'] - (defender['strength'] // 4)
        if damage>=1:
            return int(damage)
        if damage<1:
            damage=1
            return int(damage)
        
    
    def apply_damage(self, target, damage):
        """
        Apply damage to a character or enemy
        
        Reduces health, prevents negative health
        """
        # TODO: Implement damage application
        if target["health"]>0:
            target["health"]-=damage
            if target["health"] < 0:
                target["health"] = 0
        
    
    def check_battle_end(self):
        """
        Check if battle is over
        
        Returns: 'player' if enemy dead, 'enemy' if character dead, None if ongoing
        """
        # TODO: Implement battle end check
        if self.character["health"]==0:
            return "enemy"
        if self.enemy["health"]==0:
            return 'player'
    
    def attempt_escape(self):
        """
        Try to escape from battle
        
        50% success chance
        
        Returns: True if escaped, False if failed
        """
        # TODO: Implement escape attempt
        # Use random number or simple calculation
        # If successful, set combat_active to False
        import random

        escape=random.randint(1,100)
        if escape>50:
            self.combat_active=False
            return True
        else:
            self.combat_active=True
            return False
        

# ============================================================================
# SPECIAL ABILITIES
# ============================================================================

def use_special_ability(character, enemy):
    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)

    if character["class"]=="Warrior":
        warrior_power_strike(character, enemy)
        print("Warrior Cast Power Strike!!!!!!")
    if character["class"]=="Mage":
        mage_fireball(character, enemy)
        print("Mage Cast Firball !!!")
    if character["class"]=="Rogue":
        rogue_critical_strike(character, enemy)
        print("Rogue Cast Critical Strike !!!!")
    if character["class"]=="Cleric":
        cleric_heal(character)
        print("Rogue Cast Heal!")


    

def warrior_power_strike(character, enemy):
    """Warrior special ability"""
    # TODO: Implement power strike
    # Double strength damage
    check=SimpleBattle(character,enemy)
    damage=character["strength"]*2
    check.apply_damage(enemy, damage)
    
    

def mage_fireball(character, enemy):
    """Mage special ability"""
    # TODO: Implement fireball
    # Double magic damage
    check=SimpleBattle(character,enemy)
    damage=character["magic"]*2
    check.apply_damage(enemy, damage)

def rogue_critical_strike(character, enemy):
    """Rogue special ability"""
    # TODO: Implement critical strike
    # 50% chance for triple damage
    import random
    check=SimpleBattle(character,enemy)
    dam_chance= random.randint(1,100)
    if dam_chance>50:   
        damage=character["strength"]*dam_chance
        check.apply_damage(enemy, damage)


    else:
        damage=character["strength"]
        check.apply_damage(enemy, damage)
    

def cleric_heal(character):
    """Cleric special ability"""
    # TODO: Implement healing
    # Restore 30 HP (not exceeding max_health)
    hp=30
    if (hp+character["health"])<= character["max_health"]:
        character["health"]+=hp
    

# ============================================================================
# COMBAT UTILITIES
# ============================================================================

def can_character_fight(character):
    """
    Check if character is in condition to fight
    
    Returns: True if health > 0 and not in battle
    """
    # TODO: Implement fight check
    check=SimpleBattle(character)
    if character["health"]>0 and check.combat_active==False:
        return True
    else:
        return False
    

def get_victory_rewards(enemy):
    """
    Calculate rewards for defeating enemy
    
    Returns: Dictionary with 'xp' and 'gold'
    """
    # TODO: Implement reward calculation
    vic_dict={
    }
    vic_dict["gold"]=enemy["gold_reward"]
    vic_dict["xp"]=enemy["xp_reward"]
    return vic_dict
def display_combat_stats(character, enemy):
    """
    Display current combat status
    
    Shows both character and enemy health/stats
    """
    # TODO: Implement status display
    print(f"\n{character['name']}: HP={character['health']}/{character['max_health']}")
    print(f"{enemy['name']}: HP={enemy['health']}/{enemy['max_health']}")
    pass

def display_battle_log(message):
    """
    Display a formatted battle message
    """
    # TODO: Implement battle log display
    print(f">>> {message}")
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== COMBAT SYSTEM TEST ===")
    
    # Test enemy creation
    try:
         goblin = create_enemy("goblin")
         print(f"Created {goblin['name']}")
    except InvalidTargetError as e:
         print(f"Invalid enemy: {e}")
    
    # Test battle
    test_char = {
         'name': 'Hero',
         'class': 'Warrior',
        'health': 120,
        'max_health': 120,
         'strength': 15,
         'magic': 5
     }
    #
    battle = SimpleBattle(test_char, goblin)
    try:
         result = battle.start_battle()
         print(f"Battle result: {result}")
    except CharacterDeadError:
         print("Character is dead!")

