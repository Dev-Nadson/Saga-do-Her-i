import services

class Menu():
    charactersList = {}
    sistema = services.Player()
    def menuPrincipal():
        while True:
            print("===== MENU DO HERÓI =====\n")
            print("1 - Criar Personagem")
            print("2 - Entrar no jogo")
            opcao = int(input("Opção: "))

            match(opcao):
                case 1:
                    print(" ===== Escolha sua classe ===== ")
                    print("1 - Guerreiro")
                    print("2 - Arqueiro")
                    print("3 - Mago")
                    opcao = int(input("Opção: "))

                    if opcao in (1, 2, 3):
                        player = services.Player.create_player(opcao)
                        print(player)

                    else:
                        print("Opção inválida")
                        break
                    

Menu.menuPrincipal()