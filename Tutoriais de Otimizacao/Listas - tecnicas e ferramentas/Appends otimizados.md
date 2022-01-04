# Appends Otimizados

Quando estamos aprendendo a programar e aprendemos sobre listas, fazemos vários testes, com os métodos append, insert, pop, etc. 

O método **append**, é o mais simples método de adição de valores em listas, ele adiciona um valor no final de uma lista. 

```python
lista = [2, 3, 5, 33]
lista.append(200)

print(lista)
```
Saída:
```
[2, 3, 5, 33, 200]
```

Mas e se quisermos inserir um valor no início da lista usamos o método .insert(index, value).

```python
lista = [2, 3, 5, 33, 200]
lista.insert(0, 80)

print(lista)
```
Saída:
```
[80, 2, 3, 5, 33]
```

Quando inserimos um valor no início de uma lista, todos os outros valores, são movidos para a direita ->, e se removemos, todos sã omovidos para a esquerda <-. Não teremos problemas caso a lista contenha poucos valores, porém, se fizermos isso em uma lista muito grande, poderemos obter lendidão.


## Classe collections.deque

Para resolver este problema de inserção de valores no início de uma lista grande, existe a classe collections.deque do python, projetada para permitir aplicar appends de ambos os lados de uma lista de forma rápida. Vamos veer como essa classe funciona:



### list.append x deque.appendleft

Agora, iremos comparar a eficiencia do método de lista **append**, com a do método da classe deque, **appendleft**.

**Primeiro vamos criar uma lista bem grande:**

```python
# Lista MUITO grande
big_list = [2, 3, 3, 7, 7, 7, 7, 7] * 200000
print(f'A lista contêm {len(big_list) valores}')
```
Saída:

```
A lista contêm 1600000 valores
```

Agora, vamos criar 2 funções que usam loops para inserir um valor no início de uma lista várias vezes. Elas não terão retorno aqui, porém, o objeto **deque** que veremos a seguir pode ser convertido em lista e retornado por uma função.

Sintaxe das funções:

*func(list, val, loops)*

```python
## Inserção comum
def func1(lista, val=0, loops=12):
    for c in range(loops):
        lista.insert(val, 60)


# Inserção com a collections.deque
def func2(lista, val=0, loops=12):

    # Classe para inserts e pops adequados 
    # para listas grandes
    from collections import deque

    # Coverte a lista em um objeto deque
    lista_aux = deque(lista)
    
    for c in range(loops):
        lista_aux.appendleft(val)
```

Para testarmos o tempo de execução das duas funções acima, usaremos a função test_speed que criamos [nesse tutorial](https://github.com/DavidSheltonSF/Otimizar-codigo-python/blob/main/Tutoriais%20de%20Otimizacao/Medir%20o%20tempo%20de%20execucao%20do%20seu%20codigo.md).

Sintaxe da função:

*test_speed(func, \*args)*

```python
# Tempo de duração das duas funções:
time_func1 = test_speed(func1, big_list, 0, 2000)
time_func2 = test_speed(func2, big_list, 0, 2000)

print(f'A função1 demorou {time_func1}s para rodar.')
print(f'A função2 demorou {time_func2}s para rodar.')
```
Saída (pode variar):
```python
A função1 demorou 9.918472051620483 segundos para rodar.
A função2 demorou 0.07604408264160156 segundos para rodar.
```

Referências do [tutorial do python](https://docs.python.org/pt-br/3.10/tutorial/datastructures.html#:~:text=stack%0A%5B3%2C%204%5D-,5.1.2.%20Usando%20listas%20como%20filas).