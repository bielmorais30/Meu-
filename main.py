import sys

from commands.init import Init
from commands.add import Add


def main():
    argumentos = sys.argv[1:]

    match argumentos[0]:
        case 'init':
            init_command = Init()
            init_command.run()
        case 'add':
            add_command = Add(argumentos[1:])
            add_command.run()
        case _:
            print(f"Argumento inválido: {argumentos[0]}")
    


if __name__ == "__main__":    
    main()