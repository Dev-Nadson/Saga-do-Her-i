from characters import Warrior
from characters import Archer
from characters import Mage
from characters import Enemy
from characters import Weapons

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
            