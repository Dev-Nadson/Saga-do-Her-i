from characters import Warrior, Archer, Mage, Enemy, Weapons, Potions, Dados, Inventory
import time
import random

# Itens Globais
sword = Weapons("Espada Longa", 10, "Físico")
wand = Weapons("Cajado Mágico", 10, "Mágico")
bow = Weapons("Arco Curto", 8, "Físico")

class Player():
    @staticmethod
    def create_player(type_option):
        name = input("Informe o nome do personagem: ")
        while True:
            try:
                hp = int(input("Informe a quantidade de vida (HP): "))
                if hp > 0: break
            except ValueError: pass
        strength = int(input("Informe a força do personagem: "))
        
        start_potion = Potions("Poção Pequena", "Cura", 20)
        inv = Inventory([start_potion, start_potion]) 

        if type_option == 1:
            defense = int(input("Informe a defesa: "))
            return Warrior(name, hp, strength, sword, defense, inv)
        if type_option == 2:
            accuracy = int(input("Informe a precisão: "))
            return Archer(name, hp, strength, bow, accuracy, inv)
        if type_option == 3:
            magic_power = int(input("Informe o poder mágico: "))
            return Mage(name, hp, strength, wand, magic_power, inv)
            
class System():
    @staticmethod
    def create_enemy(option, name="", hp=0, strength=0, enemy_type=""):
        if option == 1: return Enemy("Goblin", 60, 15, "Monstro")
        if option == 2: return Enemy("Fantasma", 80, 20, "Espírito")
        if option == 3: return Enemy("ORC CHEFE", 150, 30, "Boss", special=True)
        else: return Enemy(name, hp, strength, enemy_type)
        
    @staticmethod
    def create_potion(option):
        if option == 1: return Potions("Poção de Cura", "Cura", 50)
        if option == 2: return Potions("Poção de Força", "Buff", 10)

class Battle():
    def __init__(self, combatants_list):
        self.combatants = combatants_list

    def get_alive_combatants(self):
        return [c for c in self.combatants if c.is_alive()]

    def start(self):
        print("\n" + "="*20)
        print("     INÍCIO DO COMBATE     ")
        print("="*20)
        
        turn_count = 1

        # O combate continua enquanto houver pelo menos 2 pessoas vivas
        while len(self.get_alive_combatants()) > 1:
            print(f"\n🔹🔹🔹 TURNO {turn_count} 🔹🔹🔹")
            time.sleep(0.5)

            # Define ordem de iniciativa
            alive_list = self.get_alive_combatants()
            initiative_order = sorted(alive_list, key=lambda x: Dados.rolar_d20(), reverse=True)

            for char in initiative_order:
                # Checa se morreu antes de chegar a vez dele
                if not char.is_alive(): continue
                
                # Checa se a batalha acabou no meio do turno
                if len(self.get_alive_combatants()) < 2: break

                print(f"\n Vez de: {char.name} (HP: {char.hp})")
                
                # === SEPARAÇÃO DE LÓGICA: PLAYER vs ENEMY ===
                if isinstance(char, Enemy):
                    self.enemy_turn_ai(char)
                else:
                    self.player_turn_menu(char)
            
            turn_count += 1

        self.announce_winner()

    def enemy_turn_ai(self, monster):
        # Lógica simples da IA: Monstros atacam Heróis
        # Filtra alvos que NÃO são Inimigos (ou seja, são Heróis)
        possible_targets = [c for c in self.get_alive_combatants() if not isinstance(c, Enemy)]
        
        if not possible_targets:
            print(f"{monster.name} ruge vitorioso, pois não há mais heróis!")
            return

        # Escolhe um herói aleatório
        target = random.choice(possible_targets)
        
        time.sleep(1)
        dmg = monster.attack()
        target.receive_damage(dmg)

    def player_turn_menu(self, hero):
        # 1. Cria lista de alvos (Todos que não são o próprio herói)
        targets = [c for c in self.get_alive_combatants() if c != hero]
        
        if not targets:
            print("Não há ninguém para atacar.")
            return

        # Seleção de Alvo
        selected_target = None
        print(f"   Selecione seu alvo:")
        for i, t in enumerate(targets):
            # Mostra: 1. Nome (Tipo) - HP
            type_str = "Inimigo" if isinstance(t, Enemy) else "Player"
            print(f"   {i+1}. {t.name} ({type_str}) - HP: {t.hp}")
        
        while True:
            try:
                idx = int(input("   Número do alvo: ")) - 1
                if 0 <= idx < len(targets):
                    selected_target = targets[idx]
                    break
                else:
                    print("   Alvo inválido.")
            except ValueError:
                print("   Digite um número válido.")

        # 2. Escolher Ação
        while True:
            print(f"   [Ação contra: {selected_target.name}]")
            print("   1. Ataque Básico")
            print("   2. Habilidade Especial")
            print("   3. Usar Poção")
            
            try:
                choice = int(input("   Sua escolha: "))
                
                if choice == 1:
                    dmg = hero.attack()
                    selected_target.receive_damage(dmg)
                    break 
                
                elif choice == 2:
                    dmg = hero.special_ability()
                    if dmg > 0: 
                        selected_target.receive_damage(dmg)
                    break 

                elif choice == 3:
                    used = hero.use_cure_potion()
                    if used: break 
                    # Se não usou (inventário vazio ou vida cheia), repete o menu

                else:
                    print("   Opção inválida!")
            except ValueError:
                print("   Digite um número válido.")

    def announce_winner(self):
        print("\n" + "="*40)
        survivors = self.get_alive_combatants()
        if survivors:
            winner = survivors[0]
            # Verifica se quem sobrou é herói ou monstro
            if isinstance(winner, Enemy):
                print(" GAME OVER! Os monstros venceram.")
            else:
                print(f" VITÓRIA! {survivors[0].name} é o último sobrevivente!")
        print("="*40)