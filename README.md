🎮 Meu Portfólio de Jogos com Pygame

Bem-vindo ao meu repositório de desenvolvimento de jogos! Este projeto é um diário da minha jornada aprendendo a criar jogos 2D com a biblioteca Pygame em Python.

Aqui você encontrará desde conceitos básicos até implementações mais completas, começando com dois jogos clássicos.

👾 Os Jogos

Atualmente, o repositório contém os seguintes projetos:

🎯 Acerte o Alvo: Um jogo simples e rápido, ótimo para entender os fundamentos do Pygame, como a captura de eventos de mouse e a renderização de objetos na tela.

🏓 Pong Clássico: Uma implementação mais robusta do icônico jogo de arcade. Este projeto explora conceitos mais complexos, como detecção de colisão, física básica da bola, controle de paletas (IA simples e/ou jogador) e sistema de pontuação.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3

Biblioteca: Pygame

🚀 Como Executar os Jogos

Para rodar qualquer um dos jogos em sua máquina local, siga estes passos:

1. Pré-requisitos

Você precisa ter o Python 3 instalado.

Você precisará do pip (gerenciador de pacotes do Python) para instalar o Pygame.

2. Instalação

Passo 1: Clone o repositório

git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/G648/GameDevelopment_Pygame.git)
cd SEU_REPOSITORIO

Passo 2: Crie um Ambiente Virtual (Recomendado)
Isso mantém as dependências do projeto isoladas.

# No Windows
python -m venv venv
.\venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate


Passo 3: Instale o Pygame

pip install pygame


3. Iniciando os Jogos

Com tudo pronto, basta executar o arquivo Python correspondente ao jogo que você quer jogar:

Para jogar "Acerte o Alvo":

# Substitua 'acerte_o_alvo.py' pelo nome exato do seu arquivo
python acerte_o_alvo.py


Para jogar "Pong":

# Substitua 'pong.py' pelo nome exato do seu arquivo
python pong.py


Pong


💡 Conceitos Praticados

Este repositório não é apenas sobre os jogos finalizados, mas sobre o aprendizado adquirido:

Em "Acerte o Alvo" (Básico):

Inicialização e configuração da janela do Pygame.

Loop principal do jogo (Game Loop).

Renderização de formas simples (círculos, retângulos).

Captura de eventos do mouse (cliques).

Uso de cores (RGB).

Posicionamento aleatório de objetos.

Em "Pong" (Complexo):

Tudo do jogo básico, e mais:

Captura de eventos do teclado (movimentação das paletas).

Detecção de colisão precisa (bola com paredes, bola com paletas).

Lógica de física simples (mudança de direção da bola).

Renderização de texto (placar).

Estrutura de jogo mais organizada (funções, classes).

Lógica de pontuação e reinício de rodada.

🤝 Contribuições

Este é um projeto de portfólio pessoal, mas sinta-se à vontade para abrir uma Issue se encontrar algum bug ou tiver sugestões de melhoria!
