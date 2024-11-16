# Função principal
def verifica_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Entrada do número inteiro
numero = int(input())

# Chamada da função e impressão do resultado
print(verifica_paridade(numero))


