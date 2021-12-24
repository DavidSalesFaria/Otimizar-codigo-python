# Código para validar se uma lista possui domente números pares

# Lista de exemplo
lista1 = [2, 2, 6, 8, 8, 20, 32, 54, 81, 90, 23]
lista2 = [2, 2, 6, 8, 8, 20, 32, 54]


# Veremos duas formas de validar esta lista


# 1º Forma: Uso de flag ---

# Flag para verificação
ok = True 
for num in lista1:
    # Se o número for impar:
    if num % 2 != 0:
        # Altera o valor da flag para False
        ok = False


# Se o valor da flag é Verdadeiro:
if ok == True:
    print('Todos os números são pares')


# 2º Forma: Comando break ---

for num in lista1:
    # Se o número for impar:
    if num % 2 != 0:
        # Interrompe o loop
        break

# Se o loop foi concluido até o fim com sucesso:
else:
    print('Todos os números são pares')