# Problema: Camisetas da Olimpíada
# Entrada: número de premiados e seus tamanhos (1 para P, 2 para M)
#          número de camisetas disponíveis de cada tamanho
# Saída: "S" se for possível atender todos, "N" caso contrário

def main():
    n = int(input("Número de premiados: "))
    qtdp = qtdm = 0

    for _ in range(n):
        tamanho = int(input("Tamanho escolhido (1 para P, 2 para M): "))
        if tamanho == 1:
            qtdp += 1
        else:
            qtdm += 1

    p, m = map(int, input("Quantidade de camisetas P e M disponíveis: ").split())
    print("S" if p >= qtdp and m >= qtdm else "N")

if _name_ == "_main_":
    main()
