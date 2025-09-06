# Problema: Diferença de idade entre irmãos
# Entrada: duas idades inteiras
# Saída: diferença absoluta entre elas

def main():
    a, b = map(int, input("Digite as idades dos dois irmãos: ").split())
    print(abs(a - b))

if _name_ == "_main_":
    main()
