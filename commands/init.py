from pathlib import Path

# Tabela de cores ANSI
RESET = "\033[0m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
ROXO = "\033[35m"

class Init:
    def __init__(self, args):
        self.args = args

    def run(self):
        diretorio = Path('.')
        if any(diretorio.glob('*.meugit')):
            print(f"{VERMELHO}Project already initialized.{RESET}")
            return
        else:
            print(f"{VERDE}Inicializando o projeto...{RESET}")
        