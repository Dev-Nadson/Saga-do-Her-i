#Classe pai
import random

class Dados():
    pass

    def rolar_d20():
        return random.randint(1,20)
    def rolar_d6():
        return random.randint(1,6)


class Character():

    def __init__(self, name, hp, strength, weapon, potion, inventory):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.strength = strength
        self.weapon = weapon
        self.potions = potion
        self.inventory = inventory

    def __str__(self):
        return f"Nome: {self.name} \nPontos de vida: {self.hp} \nForça: {self.strength}"
    
    #esse foi o iter que adicionei para testar fazer o for in mas não deu certo ainda, tenho quer melhor como funciona
    def __iter__(self):
        return iter((self.name, self.hp, self.strength, self.weapon, self.inventory.items))

    def atack(self):
        print(f"O ataque é de {self.strength + self.weapon.damage} ")
        return self.strength + self.weapon.damage
    
    def receive_damage(self, damage):
        self.hp = (self.hp - damage)
        return "Morto" if self.hp <= 0 else self.hp
    
    def specialAbilty(self, atk):
        if Dados.rolar_d20 > 15:
            print("HABLIDADE ESPECIAL!")
            return atk
        else:
            print("Habilidade especial falhou!")
            return False
        
    def useCurePotion(self, potion): 
        if self.hp <= 0:
            return "Poção não eficaz"
        
        if self.hp + potion.atribute >= self.max_hp:
            return self.max_hp
        
        return self.hp + potion.atribute

        
class Inventory():
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return self.items

class Warrior(Character):
    def __init__(self, name, hp, strength, weapon, defense, inventory):
        super().__init__(name, hp, strength, weapon, inventory)
        self.defense = defense

    def __str__(self):
        char_str = super().__str__() 
        return f"{char_str} \nDefesa: {self.defense}"
    
    def __iter__(self):
        super().__init__(self.name, self.hp, self.strength, self.weapon)
        return iter((self.name, self.hp, self.strength, self.weapon.name, self.defense, self.inventory.items))

    def atack(self):
        atk = self.strength + self.weapon.damage
        print(f"{atk}, Ataque físico")
        return atk
    
    def specialAbilty(self):
        atk = super().specialAbilty()
        if atk:
            print(f"{self.name} usou Ataque Forte!")
            return self.strength + self.weapon.damage + Dados.rolar_d6 + Dados.rolar_d6
        
class Archer(Character):
    def __init__(self, name, hp, strength, weapon, accuracy, inventory):
        super().__init__(name, hp, strength, weapon, inventory)
        self.accuracy = accuracy

    def __str__(self):
        char_str = super().__str__() 
        return f"{char_str} \nPrecisão: {self.accuracy}"

    def __iter__(self):
        super().__init__(self.name, self.hp, self.strength, self.weapon)
        return iter((self.name, self.hp, self.strength, self.weapon.name, self.accuracy, self.inventory.items))
    
    def atack(self):
       atk = self.accuracy + self.weapon.damage
       print(f"{atk}, Ataque a distância")
       return atk
    
    def specialAbilty(self):
        atk = super().specialAbilty()
        if atk:
            print(f"{self.name} usou Tiro taque Forte!")
            return self.strength + self.weapon.damage + Dados.rolar_d6 + Dados.rolar_d6

    
class Mage(Character):
    def __init__(self, name, hp, strength, weapon, magicPower, inventory):
        super().__init__(name, hp, strength, weapon, inventory)
        self.magicPower = magicPower

    def __str__(self):
        char_str = super().__str__() 
        return f"{char_str} \nPoder Mágico: {self.magicPower}"

    def __iter__(self):
        super().__init__(self.name, self.hp, self.strength, self.weapon)
        return iter((self.name, self.hp, self.strength, self.weapon.name, self.magicPower, self.inventory.items))
    
    def atack(self):
        atk = self.magicPower + self.weapon.damage
        print(f"{atk}, Ataque Mágico")
        return atk 
    
    def specialAbilty(self):
        atk = super().specialAbilty()
        if atk:
            print(f"{self.name} usou Bola de Fogo")
            return self.strength + self.weapon.damage + Dados.rolar_d6 + Dados.rolar_d6

class Enemy(Character):
    def __init__(self, name, hp, strength, enemy_type, special=False):
        super().__init__(name, hp, strength)
        self.type = enemy_type
        self.special = special

    def __str__(self):
        return f"Nome: {self.nome} \nPontos de vida: {self.hp} \nForça{self.strength} \nTipo de Monstro: {self.enemy_type}"
    
    def atack(self): 
        if Dados.rolar_d20 == 20 and self.special == True:
            return (self.strength * 2) 
        else:
            return self.strength
    
class Weapons():
   def __init__ (self, name, damage, damageType):
       self.name = name
       self.damage = damage
       self.damageType = damageType
 
class Potions():
    def __init__(self, name, effect, atribute):
        self.name = name 
        self.effect = effect 
        self.atribute = atribute

    def __str__(self):
        return f"Nome da poção: {self.name}, O efeito da poção é: {self.effect}"
    
