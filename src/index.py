from services import Player
class Menu():
    def __init__(self):
        self.players = []

    def mainMenu(self):
        while True:
            print("===== MENU DO HERÓI =====\n")
            print("1 - Criar Personagem")
            print("2 - Entrar no jogo")
            opcao = int(input("Opção: "))

            match opcao:
                case 1:
                    self.create_hero()

                case 2:
                    print("Entrando no jogo...\n")

                case _:
                    print("Opção inválida.\n")

    def create_hero(self):
            print(" ===== Escolha sua classe ===== ")
            print("1 - Guerreiro")
            print("2 - Arqueiro")
            print("3 - Mago")
            opcao = int(input("Opção: "))

            if opcao in (1, 2, 3):
                player = Player.create_player(opcao)
                self.players.append(player)
                print(f"Personagem: {player} criado!")

            else:
                print("Opção inválida")