import random

class Character:
    def __init__(self, name, STR, INT, max_HP, END):
        self.name = name
        self.STR = STR
        self.INT = INT

        self.max_HP = max_HP
        self.HP = max_HP

        self.END = END

        self.inventory = []


    def __str__(self):
        return f"\n{self.name}\n   HP: {self.HP}/{self.max_HP}\n   STR: {self.STR}\n   INT: {self.INT}\n   END: {self.END}"
    
    def is_alive(self):
        return self.HP > 0

    def take_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:
            self.HP = 0

    def after_combat_effects(self):
        self.STR += random.randint(1, 3)
        self.INT += random.randint(1, 3)
        self.END += random.randint(1, 5)


        
C = Character("Hero", 10, 5, 100, 10)
print(C)


C.take_damage(120)
print(f"{C.name} takes 120 damage! {C.HP}/{C.max_HP} HP")


print(f"Is {C.name} alive? {C.is_alive()}")

class Warrior(Character):
    pass