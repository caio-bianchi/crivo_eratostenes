def crivo_de_eratostenes(n):
    # Etapa 1: Listar todos os números ímpares de 3 a n
    numeros = list(range(3, n + 1, 2))

    # Iteração a partir do primeiro número da lista
    i = 0
    while i < len(numeros):
        p = numeros[i]
        if p * p > n:
            break
        # Etapa 2 e 3: Riscamos os múltiplos de p (exceto o próprio p)
        numeros = [x for x in numeros if x == p or x % p != 0]
        i += 1

    # Adicionar 2 à lista de números primos
    primos = [2] + numeros
    return primos

# Exemplo de uso
n = 1000000
print(f"Números primos até {n}: {crivo_de_eratostenes(n)}")
#print(f"Números primos até {n}: {len(crivo_de_eratostenes(n))}")