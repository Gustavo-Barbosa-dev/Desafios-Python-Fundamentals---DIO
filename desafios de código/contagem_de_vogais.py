def conta_vogais(texto):
    #  Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    #  Defina um contador para contar as vogais:
    contador = 0
    #  Percorra o texto e verifique se cada caractere é uma vogal:
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    #  Retorne o contador:
    return contador
# Solicitamos ao usuário que insira uma string:
texto = input("Digite uma string: ")        
#  Chame a função para contar as vogais:
resultado = conta_vogais(texto)
#  Imprima o resultado:
print(f"O número de vogais na string '{texto}' é: {resultado}")