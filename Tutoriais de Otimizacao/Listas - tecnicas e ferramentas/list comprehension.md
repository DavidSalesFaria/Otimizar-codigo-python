# List Comprehension

Uma compressão de lista é um recurso disponível no python que nos permite simplificar aínda mais a manipulação de dados em listas. Consiste em um par de colchetes contendo uma expressão seguida de uma cláusula **for** ou uma ou mais cláusulas **else**.

Vejamos um exemplo de código com o objetivo de extrair valores de uma lista, dobrar cada um desses valores e inseri-los em uma segunda lista, sem modificar a lista original:


## 1º Usando um laço de repetição **for**:

Listas de testes
```python
listaA = [2, 4, 20, 34, 100]
listaB = []

```

```python
for val in listaA:
    listaB.append(val * 2)
```

## 2º Usando list comprehension:

Sintaxe:
[<expressão> for **variavel** in **lista**]

[val * 2 for val in listaA]

Em que **val** é a variável que irá representar cada valor da lista, assim como no laço **for**.


```python
# Método de lista .exent()
listaB.extend([val * 2 for val in listaA])
```

Veja ver sobre métodos python [clique aqui](https://docs.python.org/pt-br/3.10/tutorial/datastructures.html#:~:text=list.extend(iterable))


## 3º Usando list comprehension com **if**:

Apenas valores ímpares serão inseridos na lista.

Listas de testes
```python
listaA = [2, 4, 20, 34, 100]
listaB = [] 
```

Sintaxe:
[<expressão> for **variavel** in **lista** if <condição>]

[val * 2 for val in listaA if val % 2 != 0]

```python
listaB.extend([val * 2 for val in listaA if val % 2 != 0])
```


Em que **val** é a variável que irá representar cada valor da lista, assim como no laço **for**.


```python
# Método de lista .exent()
listaB.extend([val * 2 for val in listaA])
```

## 4º Usando list comprehension com **if-else**:

Valores pares são inseridos na lista, já valores ímpares são substituídos por 0

Listas de testes
```python
listaA = [31, 44, 1, 3 20, 7, 88]
listaB = []
```

Sintaxe:
[<expressão> if <condição> else <expressão2> for **variavel** in **lista** ]

[val if val % 2 == 0 else 0 for val in listaA]

```python
listaB.extend([val if val % 2 == 0 else 0 for val in listaA])
```


Observe que é necessário mudar a ordem quando se insere o **else**.



Veja mais sobre list comprehension no [tutorial do python](https://docs.python.org/pt-br/3.10/tutorial/datastructures.html#:~:text=Um%20compreens%C3%A3o%20de%20lista%20consiste%20de%20um%20par%20de%20colchetes%20contendo%20uma%20express%C3%A3o%20seguida%20de%20uma%20cl%C3%A1usula)
