# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá daqui a 5 anos.
idade_texto = "25"
idade_numero = int(idade_texto)
idade_em_5_anos = idade_numero + 5
print("EX1 - Daqui a 5 anos a idade será:", idade_em_5_anos)

# EX2
# Converta o número de ponto flutuante 7.999 para inteiro e observe o resultado.
valor_quebrado = 7.999
valor_inteiro = int(valor_quebrado)
print("EX2 - Transformando float em int (ele corta a parte quebrada):", valor_inteiro)

# EX3
# Converta a string "-3.14" para float e multiplique o resultado por 2.
texto_pi = "-3.14"
numero_pi = float(texto_pi)
dobro_de_pi = numero_pi * 2
print("EX3 - O dobro do número convertido é:", dobro_de_pi)

# EX4
# Tente converter a string "cento e vinte" para inteiro e observe o que acontece.
print("EX4 - Tentar converter texto escrito por extenso dá erro (ValueError):")
# int("cento e vinte")  # Deixei com '#' antes para o programa rodar sem travar

# EX5
# Converta o número 42 para string e concatene com a palavra " respostas".
num_resposta = 42
texto_junto = str(num_resposta) + " respostas"
print("EX5 - Juntando o número transformado em texto:", texto_junto)

# EX6
# Use a função complex() para criar um número complexo com parte real 3 e parte imaginária 5.
valor_complexo = complex(3, 5)
print("EX6 - Mostrando o número complexo criado:", valor_complexo)

# EX7
# Converta o número 0 para booleano e mostre o resultado.
teste_zero = bool(0)
print("EX7 - O número 0 em booleano vira:", teste_zero)

# EX8
# Converta o número -100 para booleano e mostre o resultado.
teste_negativo = bool(-100)
print("EX8 - O número -100 em booleano vira:", teste_negativo)

# EX9
# Converta o número 3.1415 para inteiro e depois para string, tudo em uma única linha.
tudo_junto_em_texto = str(int(3.1415))
print("EX9 - Convertido de uma vez só para int e depois para texto:", tudo_junto_em_texto)

# EX10
# Some um número inteiro (5) com um float (2.3) e verifique qual é o tipo do resultado.
resultado_soma = 5 + 2.3
print("EX10 - A conta deu:", resultado_soma, "| E o tipo final do resultado virou:", type(resultado_soma))
