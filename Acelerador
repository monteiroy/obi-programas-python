 Problema: Acelerador
# Entrada: número de medições e velocidades
# Saída: maior aceleração entre medições consecutivas

def main():
    n = int(input("Número de medições: "))
    velocidades = list(map(int, input("Velocidades: ").split()))
    aceleracoes = [velocidades[i+1] - velocidades[i] for i in range(n-1)]

    print(max(aceleracoes))

if _name_ == "_main_":
    main()
