# Problema: Bingo
# Entrada: números sorteados e números da cartela
# Saída: "S" se todos os números da cartela foram sorteados, "N" caso contrário

def main():
    n = int(input("Quantidade de números sorteados: "))
    numeros_sorteados = set(map(int, input("Números sorteados: ").split()))
    numeros_cartela = set(map(int, input("Números da cartela: ").split()))

    print("S" if numeros_cartela.issubset(numeros_sorteados) else "N")

if _name_ == "_main_":
    main()
