from services import Player

players = []
#excluí a classe Menu para deixar em funções porque fica mais simples, e abstrai nesse arquivo para modularizar mesmo

def create_hero():
        print(" ===== Escolha sua classe ===== ")
        print("1 - Guerreiro")
        print("2 - Arqueiro")
        print("3 - Mago")
        option = int(input("Opção: "))

        if option in (1, 2, 3):
            player = Player.create_player(option)

            #tava dando erro na hora de adicionar na lista, aparecia todo bugado, aí adicionei
            #a propriedade iter nos objetos para poder adicionar
            #list transforma a instância em um array, e o iter faz isso possível
            players.append(list(player))
                
            print(f"Personagem:\n{player} \nCriado!")

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