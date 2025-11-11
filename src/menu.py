from services import Player

players = []

def create_hero():
        print(" ===== Escolha sua classe ===== ")
        print("1 - Guerreiro")
        print("2 - Arqueiro")
        print("3 - Mago")
        option = int(input("Opção: "))

        if option in (1, 2, 3):
            player = Player.create_player(option)
            
            for char in player:
                players.append(char)
            print(f"Personagem: {player} \nCriado!")

        else:
            print("Opção inválida")


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
        print("2 - Entrar no jogo")
        print("0 - Dev Tools")
        option = int(input("Opção: "))

        match option:
            case 1:
                create_hero()

            case 2:
                print("Entrando no jogo...\n")

            case 0:
                dev_tools()

            case _:
                print("Opção inválida.\n")       