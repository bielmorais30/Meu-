import sys

from commands.init import Init


def main():
    argumentos = sys.argv[1:]

    match argumentos[0]:
        case 'init':
            init_command = Init(argumentos[1:])
            init_command.run()
        case _:
            print(f"Argumento inválido: {argumentos[0]}")
    print(f"Lista de argumentos recebidos: {argumentos}")

    # if len(argumentos) >= 1:
    #     print(f"Primeiro argumento: {argumentos[0]}")


if __name__ == "__main__":    
    main()