# src/main.py

from src.core.superia import SuperIA

def main():
    ia = SuperIA()
    print("\nSuperIA iniciada! Digite uma entrada e veja a resposta.\n(Digite 'sair' para encerrar)\n")

    while True:
        entrada = input("Entrada: ")
        if entrada.lower() == "sair":
            print("Encerrando SuperIA...")
            break
        resposta = ia.run(entrada)
        print(f"Decisão: {resposta}\n")

if __name__ == "__main__":
    main()
