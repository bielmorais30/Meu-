
import os


os.system('color')

# Tabela de cores ANSI
RESET = "\033[0m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
ROXO = "\033[35m"

class Colors:

    @staticmethod
    def vermelho(texto):
        return f"{VERMELHO}{texto}{RESET}"
    
    @staticmethod
    def verde(texto):
        return f"{VERDE}{texto}{RESET}"
    
    @staticmethod
    def amarelo(texto):
        return f"{AMARELO}{texto}{RESET}"
    
    @staticmethod
    def azul(texto):
        return f"{AZUL}{texto}{RESET}"
    
    @staticmethod
    def roxo(texto):
        return f"{ROXO}{texto}{RESET}"