from services import Player, System, Battle

players = []
enemies = []
potions_list = []

class Menu():
    
    @staticmethod
    def create_hero():
        print("\n===== Novo Herói =====")
        print("1 - Guerreiro")
        print("2 - Arqueiro")
        print("3 - Mago")
        try:
            option = int(input("Opção: "))
            if option in (1, 2, 3):
                player = Player.create_player(option)
                players.append(player)
                print(f" {player.name} criado!")
            else:
                print("Opção inválida")
        except ValueError: pass

    @staticmethod
    def create_enemy():
        print("\n===== Novo Inimigo =====")
        print("1 - Goblin")
        print("2 - Fantasma")
        print("3 - ORC BOSS")
        try:
            option = int(input("Opção: "))
            if option in (1, 2, 3):
                enemy = System.create_enemy(option)
                enemies.append(enemy)
                print(" Inimigo criado!")
        except ValueError: pass

    @staticmethod
    def start_battle_check():
        # Junta todos os combatentes
        all_fighters = players + enemies
        
        # Condição 1: Pelo menos 2 personagens no total
        if len(all_fighters) < 2:
            print(" Atenção: Para iniciar uma batalha, você precisa de pelo menos 2 personagens criados.")
            return

        # Condição 2: Pelo menos 1 Herói (para ter quem controlar)
        if len(players) < 1:
            print(" Você precisa de pelo menos 1 Herói para jogar.")
            return

        # Se passou nas condições, inicia a batalha com TODOS
        battle_system = Battle(all_fighters)
        battle_system.start()
        
        # Pós-batalha: Remover os mortos das listas globais
        Menu.remove_dead()

    @staticmethod
    def remove_dead():
        # Remove da lista de players
        for i in range(len(players)-1, -1, -1):
            if not players[i].is_alive():
                print(f" {players[i].name} (Herói) caiu em batalha e foi removido.")
                players.pop(i)
        
        # Remove da lista de inimigos
        for i in range(len(enemies)-1, -1, -1):
            if not enemies[i].is_alive():
                print(f" {enemies[i].name} (Inimigo) foi derrotado e removido.")
                enemies.pop(i)

    @staticmethod
    def main_menu():
        while True:
            print("\n===== RPG DE TEXTO =====")
            print(f"Status: {len(players)} Heróis | {len(enemies)} Inimigos.")
            print("1 - Criar Herói")
            print("2 - Criar Inimigo")
            print("3 - INICIAR BATALHA")
            print("4 - Ver Personagens")
            print("0 - Sair")
            
            try:
                option = int(input("Opção: "))
                
                if option == 1:
                    Menu.create_hero()
                elif option == 2:
                    Menu.create_enemy()
                elif option == 3:
                    Menu.start_battle_check()
                elif option == 4:
                    print("\n--- Heróis ---")
                    for p in players: print(p)
                    print("\n--- Inimigos ---")
                    for e in enemies: print(e)
                elif option == 0:
                    break
            except ValueError:
                print("Opção inválida.")