from services import Player, System, Game, Battle

players = []
enemies = []
potions = []

def create_hero():
        print(" ===== Escolha sua classe ===== ")
        print("1 - Guerreiro")
        print("2 - Arqueiro")
        print("3 - Mago")
        option = int(input("Opção: "))

        if option in (1, 2, 3):
            player = Player.create_player(option)
            players.append(list(player))
                
            print(f"Personagem:\n{player} \nCriado!")

        else:
            print("Opção inválida")


def create_enemy():
        print(" ===== Crie um inimigo ===== ")
        print("1 - Goblin")
        print("2 - Fantasma")
        print("2 - ORC (Especial)")
        print("0 - Inimigo Custom")
        option = int(input("Opção: "))

        if option in ( 1, 2 ):
                enemy = System.create_enemy(option)
                enemies.append(list(enemy))

        if option == 0:
            print(" ===== Inimigo customizado ===== ")
            name = input("Insira o nome do inimigo: ")
            hp = int(input("Insira a vida do inimigo: "))
            strength = int(input("Insira a força do inimigo"))
            enemy_type = input("Insira o tipo no inimigo")
            enemy = System.create_enemy(option, name, hp, strength, enemy_type)

        else:
            print("Opção inválida.\n")

def create_potion():
        print(" ===== Crie uma poção ===== ")
        print("1 - Poção de Cura")
        print("2 - Poção de poder")
        option = int(input("Opção: "))

        if option in ( 1, 2 ):
                potion = System.create_potion(option)
                potions.append(list(potion))
                
        else:
            print("Opção inválida.\n")


def dev_tools():
    print("===== OPÇÕES DE DESENVOLVEDOR =====\n")
    print("1. Listar todos os players")
    option = int(input("Opção: "))
    match option:

        case 1:
            print(players)

        case _:
            print("Opção inválida.\n")



def menu():
    while True:
        print("===== MENU DO HERÓI =====\n")
        print("1 - Criar Personagem")
        print("2 - Criar Inimigo")
        print("3 - Criar Poção")
        print("4 - Entrar no jogo")
        print("0 - Dev Tools")
        option = int(input("Opção: "))

        match option:
            case 1:
                create_hero()

            case 2:
                create_enemy()

            case 3:
                create_potion()

            case 4:
                i = 1
                
                print("===== Personagens: ")
                for player in players:
                    print(f"{i}. {player}")
                
                op = int(input("Escolha o personagem 01: "))
                player01 = players[op-1]

                op = int(input("Escolha o personagem 02: "))
                player02 = players[op-1]

                print(player01, player02)
                battle = Battle(player01, player02)

                battle.battle()
            case 0:
                dev_tools()

            case _:
                print("Opção inválida.\n")       