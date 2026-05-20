# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá daqui a 5 anos.
idade_str = "25"
idade_int = int(idade_str)
idade_futura = idade_int + 5
print("EX1 - Idade daqui a 5 anos:", idade_futura)

# EX2
# Converta o número de ponto flutuante 7.999 para inteiro e observe o resultado.
num_float = 7.999
num_int = int(num_float)
print("EX2 - Float para int (trunca o valor):", num_int)

# EX3
# Converta a string "-3.14" para float e multiplique o resultado por 2.
str_pi = "-3.14"
float_pi = float(str_pi)
resultado_pi = float_pi * 2
print("EX3 - String para float multiplicado por 2:", resultado_pi)

# EX4
# Tente converter a string "cento e vinte" para inteiro e observe o que acontece.
print("EX4 - Isso vai gerar um erro do tipo ValueError:")
# int("cento e vinte")  # Comentado para o código não travar na execução

# EX5
# Converta o número 42 para string e concatene com a palavra " respostas".
numero = 42
texto = str(numero) + " respostas"
print("EX5 - Número para string concatenado:", texto)

# EX6
# Use a função complex() para criar um número complexo com parte real 3 e parte imaginária 5.
num_complexo = complex(3, 5)
print("EX6 - Número complexo criado:", num_complexo)

# EX7
# Converta o número 0 para booleano e mostre o resultado.
bool_zero = bool(0)
print("EX7 - Booleano de 0:", bool_zero)

# EX8
# Converta o número -100 para booleano e mostre o resultado.
bool_negativo = bool(-100)
print("EX8 - Booleano de -100:", bool_negativo)

# EX9
# Converta o número 3.1415 para inteiro e depois para string, tudo em uma única linha.
resultado_linha = str(int(3.1415))
print("EX9 - Convertido em uma única linha:", resultado_linha)

# EX10
# Some um número inteiro (5) com um float (2.3) e verifique qual é o tipo do resultado.
soma = 5 + 2.3
print("EX10 - Resultado da soma:", soma, "| Tipo do resultado:", type(soma))