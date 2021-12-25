# Comandos break, continue e cláusula else

Aprenderemos algumas técnicas simples de otimização de laços **for** e **while** que quando bem usadas, podem contribuir muito para soluções de código mais enxutas e simples (menos linhas de código e menos trabalho, para você e seu pc).



## break

O comando **break**, encerra o laço de repetição atual mais interno. Podendo ser um laço **for** ou **while**.

Podemos usa-lo quando queremos interromper um loop no momento em que uma determinada condição for atendida.

1. Exemplo de laço para buscar um número específico em uma lista:

```
lista = [3, 2, 29, 88, 20, 90, 77, 20]

for num in lista:
    if num == 88:
        print(f'O número {num} foi encontrado!')
        break
```

Observe que sem o **break**, o laço iria iterar sobre a lista inteira. Isso seria inviável para uma lista muito grande.

## Uso do break com a cláusula else

Os laços podem ter uma cláusula **else** que é executada sempre que o laço itera até o fim, sem ser interrompido. Para o **for**, quando os valores do iterável acabam, já para o **while**, quando a condição se torna falsa.

O uso do **else** em um laço de repetição, é muito útil e nos permite evitar o uso de flags. Flags, na programação são variáveis booleanas que funcionam como interruptores que usamos para testar condições.

Veremos 2 exemplos, de laços, para validar se uma lista de números possui apenas números pares.

1º Não usaremos **break** nem **else**

```
lista = [10, 20, 8, 8, 6, 30, 7, 90]

# Inicializamos uma flag com valor True
ok = True

for num in lista:
    # Verifica se o número é impar
    if num % 2 != 0:
        # Altera o valor da flag
        ok = False


# Printa que todos os valores são
# pares apenas se o valor da flag for True:
if ok == True:
    print('Todos os valore são pares')

```

2º Uso de **break** e **else**:

```
lista = [10, 20, 8, 8, 6, 30, 7, 90]

for num in lista:
    # Verifica se o número é ímpar
    if num % 2 != 0:
        # Interrompe o loop
        break

# Executa apenas se o laço iterou até o fim:
else:
    print('Todos os valores são pares')

```

Podemos observar que no 2º usamos menos linhas de código que no 1º.

Veja mais informações sobre o comando **break** e a cláusula **else** no [tutorial do python](https://docs.python.org/pt-br/3/tutorial/controlflow.html#:~:text=4.4.%20Comandos%20break%20e%20continue%2C%20e%20cl%C3%A1usula%20else%2C%20nos%20la%C3%A7os%20de%20repeti%C3%A7%C3%A3o)
