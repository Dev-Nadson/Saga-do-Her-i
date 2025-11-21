import random

class Dados():
    @staticmethod
    def rolar_d20():
        return random.randint(1, 20)
    
    @staticmethod
    def rolar_d6():
        return random.randint(1, 6)

class Character():
    def __init__(self, name, hp, strength, weapon, inventory=None):
        self.name = name
        self.max_hp = hp
        self._hp = hp 
        self.strength = strength
        self.weapon = weapon
        self.inventory = inventory if inventory else Inventory([])

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp} | Força: {self.strength} | Arma: {self.weapon.name})"

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        base_damage = self.strength + self.weapon.damage
        return base_damage
    
    def receive_damage(self, damage):
        old_hp = self.hp
        self.hp -= damage
        real_damage = old_hp - self.hp
        print(f" {self.name} recebeu {real_damage} de dano. Vida restante: {self.hp}")
        if not self.is_alive():
            print(f" {self.name} morreu!")

    def special_ability(self):
        roll = Dados.rolar_d20()
        print(f"  Rolagem de Sorte: {roll} (Precisa > 12)")
        if roll > 12: 
            return True
        else:
            return False
        
    def use_cure_potion(self): 
        potion = None
        for item in self.inventory.items:
            if isinstance(item, Potions) and item.effect == "Cura":
                potion = item
                break
        
        if potion:
            if self.hp >= self.max_hp:
                print("   Sua vida já está cheia!")
                return False
            
            cura = potion.attribute
            self.hp = min(self.max_hp, self.hp + cura)
            self.inventory.items.remove(potion)
            print(f"  {self.name} usou {potion.name} e recuperou {cura} de vida. HP: {self.hp}")
            return True
        else:
            print("  Nenhuma poção de cura no inventário!")
            return False

class Inventory():
    def __init__(self, items):
        self.items = items

    def __str__(self):
        names = [item.name for item in self.items]
        return ", ".join(names) if names else "Vazio"

class Warrior(Character):
    def __init__(self, name, hp, strength, weapon, defense, inventory=None):
        super().__init__(name, hp, strength, weapon, inventory)
        self.defense = defense

    def __str__(self):
        return super().__str__() + f" | Defesa: {self.defense}"

    def attack(self):
        dmg = super().attack()
        print(f"⚔️ {self.name} desfere um golpe de espada! Dano: {dmg}")
        return dmg
    
    def special_ability(self):
        print(f"   Tentando usar: GOLPE ESMAGADOR...")
        if super().special_ability():
            bonus = Dados.rolar_d6() + Dados.rolar_d6()
            dmg = self.attack() + bonus
            print(f" SUCESSO! O golpe foi brutal! (+{bonus} dano extra)")
            return dmg
        print("  Falhou! O personagem tropeçou.")
        return 0
        
class Archer(Character):
    def __init__(self, name, hp, strength, weapon, accuracy, inventory=None):
        super().__init__(name, hp, strength, weapon, inventory)
        self.accuracy = accuracy

    def __str__(self):
        return super().__str__() + f" | Precisão: {self.accuracy}"
    
    def attack(self):
       dmg = self.accuracy + self.weapon.damage
       print(f" {self.name} dispara uma flecha rápida! Dano: {dmg}")
       return dmg
    
    def special_ability(self):
        print(f"   Tentando usar: TIRO NA CABEÇA...")
        if super().special_ability():
            bonus = Dados.rolar_d6() + Dados.rolar_d6()
            dmg = self.attack() + bonus
            print(f"  HEADSHOT! Dano massivo! (+{bonus} dano extra)")
            return dmg
        print("  Falhou! A flecha passou longe.")
        return 0

class Mage(Character):
    def __init__(self, name, hp, strength, weapon, magic_power, inventory=None):
        super().__init__(name, hp, strength, weapon, inventory)
        self.magic_power = magic_power

    def __str__(self):
        return super().__str__() + f" | Poder Mágico: {self.magic_power}"
    
    def attack(self):
        dmg = self.magic_power + self.weapon.damage
        print(f" {self.name} lança uma orbe de energia! Dano: {dmg}")
        return dmg 
    
    def special_ability(self):
        print(f"   Tentando usar: BOLA DE FOGO...")
        if super().special_ability():
            bonus = Dados.rolar_d6() + Dados.rolar_d6()
            dmg = self.attack() + bonus
            print(f" QUEIMADURA! O inimigo está em chamas! (+{bonus} dano extra)")
            return dmg
        print("  Falhou! A magia falhou.")
        return 0

class Enemy(Character):
    def __init__(self, name, hp, strength, enemy_type, special=False):
        default_weapon = Weapons("Ataque Básico", 0, "Físico") 
        super().__init__(name, hp, strength, default_weapon)
        self.type = enemy_type
        self.special = special

    def __str__(self):
        return f"[INIMIGO] {self.name} | HP: {self.hp} | Tipo: {self.type}"
    
    def attack(self): 
        base_dmg = self.strength
        if self.special:
            roll = Dados.rolar_d20()
            if roll >= 18:
                print(f"{self.name} enfurece e dá DANO DOBRADO!")
                return base_dmg * 2
        
        print(f" {self.name} ataca violentamente! Dano: {base_dmg}")
        return base_dmg

class Weapons():
   def __init__ (self, name, damage, damage_type):
       self.name = name
       self.damage = damage
       self.damage_type = damage_type
 
class Potions():
    def __init__(self, name, effect, attribute):
        self.name = name 
        self.effect = effect 
        self.attribute = attribute

    def __str__(self):
        return f"{self.name} ({self.effect}: {self.attribute})"