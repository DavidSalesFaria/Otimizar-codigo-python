# Expressões lambda

São funções anônimas, ou seja, não precisam ser nomeadas como as funções comuns (funções aninhadas), também são mais simples e usam apenas 1 linha de código. Inicialmente podem parecer complexas, porém em alguns casos você vai querer usar uma dessas. Vejamos exemplos:


## Função para somar dois números

### Função aninhada:
```python
def somar(n1 + n2):
    return n1 + n2


print(somar(50, 50))
```

```
100
```

### Função lambda:
Sintaxe: 

lambda <argumentos...\>: <expressão>

```lambda arg1, arg2: arg1 + arg2```

```python
somar = lambda n1, n2: n1 + n2
print(somar(50, 50))
```

```
100
```

Expressões lambda, retornam o resultado de uma expressão como qualquer outra função. Porém podemos usar funções lambda como retorno de funções:


## Função que retorna um incrementador

```python
def criar_incrementador(n):

    # Retorna uma lambda com o valor n armazenado no x
    return lambda x: x + n
```

```python
f = criar_incrementador(50)
print(f(0))
print(f(2))
```

```python
50
52
```


## Expressões lambda como argumento de funções
Podemos usar as expressões anônimas lambda, como argumentos de funções, aproveitando que elas não precisam ser nomeadas:

### Organizar uma lista de tuplas com o método sort:
```python
numeros = [(3, 'três'), (1, 'um'), (2, 'dois')]

numeros.sort(key=lambda num: num[0])

print(numeros)
```

```
[(1, 'um'), (2, 'dois'), (3, 'três')]
```

## Manipular/alterar valores de listas
Objetivo: Passar todos os valores de uma lista chamada 'numeros' para uma lista 'dobros', porém multiplicando todos por 2.

```numeros = [3, 5, 8, 22, 1, 6, 7]```

```dobros = []```

### Usando laço **for**
```python
for num in numeros:
    dobros.append(num * 2)
```

### Usando lambda
```python
# A função map() propaga a função lambda para todos 
# os valores da lista 'numeros' e retorna um objeto 
# que pode ser convertido para uma lista.
dobros = list(map(lambda x: * 2, numeros))
```

Nos dois casos a saída será:
```
[6, 10, 16, 44, 2, 12, 14]
```
