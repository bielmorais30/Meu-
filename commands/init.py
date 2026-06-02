from pathlib import Path
import os

os.system('color')

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
            print(f"{VERMELHO}Projeto .meugit já inicializado.{RESET}")
            return
        else:
            print(f"{VERDE}Inicializando o projeto...{RESET}")
            dir_meugit = Path(".meugit")
            dir_meugit_commits = Path(".meugit/commits")
            dir_meugit_objects = Path(".meugit/objects")
            dir_meugit_branches = Path(".meugit/branches")
            dir_meugit_head = Path(".meugit/HEAD")


            dir_meugit.mkdir(exist_ok=True)
            dir_meugit_commits.mkdir(exist_ok=True)
            dir_meugit_objects.mkdir(exist_ok=True)
            dir_meugit_branches.mkdir(exist_ok=True)
            dir_meugit_head.mkdir(exist_ok=True)
        