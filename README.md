# Jogo de Xadrez com Pygame

Este é um projeto simples de jogo de xadrez desenvolvido com Python e a biblioteca Pygame. O objetivo é permitir que dois jogadores joguem uma partida completa de xadrez em um tabuleiro interativo com interface gráfica.

## 🎮 Funcionalidades

- Tabuleiro de xadrez interativo em 2D
- Movimento de peças com regras oficiais de xadrez
- Reinício de partida

## 🛠️ Tecnologias Utilizadas

- Python 
- Pygame

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chess-pygame.git
cd chess-pygame
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

Basta rodar o arquivo principal do projeto:

```bash
python main.py
```

## 📁 Estrutura do Projeto

```
chess-pygame/
│
├── assets/              # Imagens das peças
│── main.py              # Arquivo principal
│── board.py             # Lógica do tabuleiro
│── move.py              # Classe de movimento
│── moves_possibles.py   # Controle da lógica de movimentação
├── requirements.txt     # Dependências
└── README.md            # Este arquivo
```
