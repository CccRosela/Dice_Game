from dice import roll_dice
# Add error if cooldown is somehow < 0

class Character:
    inventory = []
    cooldown = 0
    has_rested = False
    
    def __init__(self, name, STR, INT, max_HP, END):
        self.name = name
        self.STR = STR
        self.INT = INT

        self.max_HP = max_HP
        self.HP = max_HP

        self.END = END


    def __str__(self):
        return f"\n{self.name}\n   HP: {self.HP}/{self.max_HP}\n   STR: {self.STR}\n   INT: {self.INT}\n   END: {self.END}"
    
    def is_alive(self):
        return self.HP > 0

    def attack(self):
        # Roll dice for dmg based on STR or INT, depends on subclass

    def take_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:
            self.HP = 0

    def after_combat_effects(self):
        # D4 boosts
        self.STR += roll_dice(4)
        self.INT += roll_dice(4)
        self.END += roll_dice(4)
    

class Warrior(Character):
    def __init__(self, warrior, name="N/A"):
        super().__init__(name, warrior, STR=16, END=12, INT=2, HP=100)
        self.warrior = warrior 
    
    # Special attack
    def one_shot_kill(self):
        if self.cooldown == 0:
            print(f"{self.name} uses One Shot Kill!")

            roll = roll_dice(12)
            self.cooldown = 3
        else:
            if self.cooldown != 1:
                print(f"One Shot Kill is on cooldownfor {self.cooldown} more turns.")
            else:
                print(f"One Shot Kill is on cooldown for {self.cooldown} more turn.")
        
        # Add dice rolls 



class Sage(Character):
    def __init__(self, sage, name="N/A"):
        super().__init__(name, sage, STR=2, END=12, INT=16, HP=100)
        self.sage = sage


    # Special Attack
    def shining_arrows(self):
        if self.cooldown == 0:
            print(f"{self.name} uses Shining Arrows!")

            roll = roll_dice(12)
            self.cooldown = 3

        else:
            print("Shining Arrows is on cooldown.")


C = Character("Hero", 10, 5, 100, 10)
print(C)

C.take_damage(120)
print(f"{C.name} takes 120 damage! {C.HP}/{C.max_HP} HP")


print(f"Is {C.name} alive? {C.is_alive()}")