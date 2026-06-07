from pathlib import Path
from assets.colors import Colors
import os



class Init:
    
    def run(self):
        diretorio = Path('.')
        if any(diretorio.glob('*.meugit')):
            print(Colors.vermelho("Projeto .meugit já inicializado."))
            return
        else:
            print(Colors.verde("Inicializando o projeto..."))
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
        