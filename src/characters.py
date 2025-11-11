#Classe pai
class Character():
    def __init__(self, name, hp, strength, weapon):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.weapon = weapon

    def atack(self):
        return f"O ataque é de {self.strength + self.weapon.damage}"

    def __str__(self):
        return f"Nome: {self.name} \nPontos de vida: {self.hp} \nForça: {self.strength}"
    
    #esse foi o iter que adicionei para testar fazer o for in mas não deu certo ainda, tenho quer melhor como funciona
    def __iter__(self):
        return iter((self.name, self.hp, self.strength, self.weapon))

class Warrior(Character):
    def __init__(self, name, hp, strength, weapon, defense):
        super().__init__(name, hp, strength, weapon)
        self.defense = defense

    def __str__(self):
        char_str = super().__str__() 
        return f"{char_str} \nDefesa: {self.defense}"
    
    def __iter__(self):
        super().__init__(self.name, self.hp, self.strength, self.weapon)
        return iter((self.name, self.hp, self.strength, self.weapon.name, self.defense))

    def atack(self):
        atk = super().atack()
        return f"{atk} Espadada"

class Archer(Character):
    def __init__(self, name, hp, strength, weapon, accuracy):
        super().__init__(name, hp, strength, weapon)
        self.accuracy = accuracy

    def __str__(self):
        char_str = super().__str__() 
        return f"{char_str} \nPrecisão: {self.accuracy}"

    def atack(self):
        atk = super().atack()
        return f"{atk}, Tiro de Arco"
    
    def __iter__(self):
        super().__init__(self.name, self.hp, self.strength, self.weapon)
        return iter((self.name, self.hp, self.strength, self.weapon.name, self.accuracy))

class Mage(Character):
    def __init__(self, name, hp, strength, weapon, magicPower):
        super().__init__(name, hp, strength, weapon)
        self.magicPower = magicPower

    def __str__(self):
        char_str = super().__str__() 
        return f"{char_str} \nPoder Mágico: {self.magicPower}"

    def atack(self):
        atk = super().atack()
        return f"{atk}, Tiro de Mana"
    
    def __iter__(self):
        super().__init__(self.name, self.hp, self.strength, self.weapon)
        return iter((self.name, self.hp, self.strength, self.weapon.name, self.magicPower))

class Enemy(Character):
    def __init__(self, name, hp, strength, type):
        super().__init__(name, hp, strength)
        self.type = type

    def __str__(self):
        return f"Nome: {self.nome} \nPontos de vida: {self.hp} \nForça{self.strength} \nTipo de Monstro: {self.type}"
    
class Weapons():
   def __init__ (self, name, damage, damageType):
       self.name = name
       self.damage = damage
       self.damageType = damageType
 
class Potion():
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __str__(self):
        return f"Nome da poção: {self.name}, O efeito da poção é: {self.effect}"
    