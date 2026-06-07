from pathlib import Path
from assets.colors import Colors

class Add:
    def __init__(self, args):
        self.args = args

    def run(self):
        diretorio = Path('.')
        if not any(diretorio.glob('*.meugit')):
            print(Colors.vermelho("Nenhum projeto .meugit encontrado. Por favor, inicialize um projeto primeiro."))
            return
        
        resultado = self.arquivo_existe()
        if resultado["falha"]:
            print(Colors.vermelho(f"Os seguintes arquivos não foram encontrados: \n{', '.join(resultado['falha'])}"))
        if resultado["sucesso"]:
            print(Colors.verde(f"Os seguintes arquivos foram adicionados com sucesso: \n{', '.join(resultado['sucesso'])}"))


    
    def arquivo_existe(self):
        nao_existe = []
        sucesso    = []
        for arquivo in self.args:
            if not Path(arquivo).exists():
                nao_existe.append(arquivo)
            else:
                sucesso.append(arquivo)

        return {"sucesso": sucesso, "falha": nao_existe}