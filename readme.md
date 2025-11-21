⚔️ RPG de Texto em Python

Um jogo de RPG baseado em turnos desenvolvido em Python, focado na aplicação de conceitos de Programação Orientada a Objetos (POO). O projeto apresenta um sistema de batalha tático, múltiplas classes de heróis, inimigos com IA básica e gerenciamento de inventário.

📋 Sobre o Projeto

Este projeto foi estruturado em módulos para garantir organização e escalabilidade. O jogo simula um combate onde o jogador pode controlar heróis (Guerreiro, Arqueiro, Mago) contra monstros ou até mesmo contra outros jogadores em um sistema de alvos livres.

O código abrange desde conceitos básicos de classes e objetos até tópicos avançados como polimorfismo, métodos estáticos, encapsulamento e lógica de turnos complexa.

🚀 Funcionalidades

    Classes de Heróis:

        🛡️ Guerreiro: Foco em defesa e dano físico.

        🏹 Arqueiro: Foco em precisão e ataques à distância.

        🔮 Mago: Foco em alto poder mágico.

    Sistema de Inimigos:

        Criação de monstros (Goblin, Fantasma) e Chefes (Orc Boss com mecânica de crítico).

        IA simples que ataca heróis aleatoriamente.

    Sistema de Combate:

        Turnos: Baseado em iniciativa (rolagem de d20).

        Seleção de Alvo: O jogador escolhe livremente quem atacar (outro monstro ou outro jogador).

        Ações: Ataque Básico, Habilidade Especial (com chance de falha/sucesso) e Uso de Poções.

    Inventário e Itens:

        Gerenciamento de poções de cura.

        Armas com atributos específicos.

    Aleatoriedade:

        Sistema de dados (Dados.rolar_d20, Dados.rolar_d6) para definir dano extra e iniciativa.

📂 Estrutura de Arquivos

O projeto está dividido em 4 módulos principais:

    main.py: O ponto de entrada da aplicação. Apenas inicia o Menu.

    menu.py: Gerencia a interface de usuário (CLI), criação de personagens e configuração da batalha.

    services.py: Contém a lógica pesada do jogo:

        Battle: Gerencia o loop de turnos, checagem de vida e condições de vitória.

        System: Fábrica (Factory) para criar inimigos e itens.

        Player: Fábrica para criar heróis.

    characters.py: Contém todas as classes de modelo (Character, Warrior, Enemy, Inventory, etc.).

🛠️ Como Rodar o Jogo

Pré-requisitos

    Python 3.x instalado.

Passo a Passo

    Clone este repositório ou baixe os arquivos.

    Certifique-se de que os 4 arquivos (main.py, menu.py, services.py, characters.py) estão na mesma pasta.

    Abra o terminal na pasta do projeto.

    Execute o comando:

Bash

python main.py

🎮 Guia de Gameplay

    Criação: Ao iniciar, use as opções 1 e 2 para criar pelo menos 1 Herói e 1 Outro Personagem (pode ser monstro ou outro herói).

    Batalha: Selecione a opção 3 para iniciar.

        O sistema verificará se há combatentes suficientes (mínimo 2).

    Combate:

        A cada turno, se for a vez de um Herói, você verá uma lista de alvos vivos.

        Escolha o número do alvo.

        Escolha a ação (Ataque, Especial ou Poção).

        A habilidade especial requer uma rolagem de sorte > 12 no d20 para funcionar.

    Vitória: O jogo termina quando restar apenas 1 sobrevivente (ou um time de monstros/heróis).
