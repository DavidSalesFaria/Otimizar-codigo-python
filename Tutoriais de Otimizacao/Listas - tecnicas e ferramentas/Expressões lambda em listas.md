# Expressões lambda em listas

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
dobros = list(map(lambda x: x * 2, numeros))
```

Nos dois casos a saída será:
```
[6, 10, 16, 44, 2, 12, 14]
```

    Veja mais sobre expressões lambda clicando [aqui](https://github.com/DavidSheltonSF/Otimizar-codigo-python/blob/main/Tutoriais%20de%20Otimizacao/Express%C3%B5es%20lambda.md)