# EX1 - Idade e tipo
idade = 10
print("EX1 - Idade:", idade, "| Tipo:", type(idade))

# EX2 - Temperatura e tipo
temperatura = 23.5
print("EX2 - Temp:", temperatura, "| Tipo:", type(temperatura))

# EX3 - Número complexo (Parte Real)
impedancia = 5 + 8j
print("EX3 - Parte Real:", impedancia.real)

# EX4 - Parte Imaginária
print("EX4 - Parte Imaginária:", impedancia.imag)

# EX5 - População (8 bilhões)
populacao = 8_000_000_000
print("EX5 - População tipo:", type(populacao))

# EX6 - Verificar tipo do número 7
print("EX6 - O tipo do número 7 é:", type(7))

# EX7 - Booleano aprovado
aprovado = True
print("EX7 - Aprovado tipo:", type(aprovado))

# EX8 - Somar True e False
soma = True + False
print(f"EX8 - Resultado da soma: {soma} | Tipo: {type(soma)}")

# EX9 - Valor máximo de um inteiro (usando sys)
import sys
print("EX9 - O valor máximo de referência é:", sys.maxsize)

# EX10 - Binário de 10
print("EX10 - Representação binária de 10:", bin(10))
