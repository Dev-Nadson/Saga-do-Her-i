from characters import Warrior
from characters import Archer
from characters import Mage
from characters import Enemy
from characters import Weapons
from characters import Potions

sword = Weapons("Espada longa", 10, "Fisico")
wand = Weapons("Cajado Mágico", 10, "Mágico")
bow = Weapons("Arco", 8, "Físico")

class Player():
    def create_player(type):
        name = input("Informe o nome do personagem: ")
        hp = int(input("Informe a quantidade de vida do personagem: "))

        while hp < 0:
            print("Vida inválida, digite um valor positivo")
            hp = int(input("Informe uma quantidade válida de vida pro personagem: "))

        strength = int(input("Informe a força do personagem: "))

        if type == 1:
            defense = int(input("Informe o defesa do personagem: "))
            return Warrior(name, hp, strength, sword, defense)

        if type == 2:
            accuracy = int(input("Insira o modificador de acerto: "))
            return Archer(name, hp, strength, wand, accuracy)

        if type == 3:
            magicPower = int(input("Insira o poder mágico:"))
            return Mage(name, hp, strength, bow, magicPower)
            
class System():
    def create_enemy(option, name="", hp="", strength="", enemy_type=""):
        if option == 1:
            return Enemy("Goblin", 100, 100, "Monster")
        
        if option == 2:
            return Enemy("Fantasma", 200, 50, "Ghost")
        
        if option == 2:
            return Enemy("ORC", 300, 200, "Boss", special=True)
        
        else:
            return Enemy(name, hp, strength, enemy_type)
        
    def create_potion(option, name="", effect=""):
        if option == 1:
            return Potions("Poção de cura", "Cura a vida do herói")
        
        if option == 2:
            return Potions("Poção de poder", "Aumenta a força do herói")
        
        else:
            return Potions(name, effect)    
    
        
class Game():
    pass

    def isAlive(object):
        if object.hp <= 0: 
            return "Personagem está morto" 
        else: 
            return "Persnoagem está vivo" 

