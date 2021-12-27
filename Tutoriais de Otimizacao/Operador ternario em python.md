# Operadores ternários em python

Diferentemente de outras linguagens, no python essa funcionalidade é chamada de Expressão Condicional. Este recurso, em alguns casos, pode ser usado para substituir uma Estrutura Condicional **if** ou **if-else**, reduzindo assim, o número de linhas do nosso código e o simplificando.

## Estrutura Condicional x Expressão Condicional

Vejamos um exemplo de uma estrutura condicional com o objetivo de calcular o bônus de um vendedor que receberá 20% de bônus caso tenha batido a meta de vendas, caso não a tenha batido, não recebe bônus:

```python
# Teste o código na sua máquina, e mude os valores.

meta = 200
vendas = 301

# Se o número de vendas 
# for maior ou igual a meta
if vendas >= meta:
    bonus = 0.20

# Senão:
else:
    bonus = 0
```

Agora vamos substituir esse código  de 6 linhas por um operador ternário:

Sintaxe:
<expressão1> if <condição>  else <expressão2>

Primeiramente é avaliada a condição, e se for verdadeira, é executada a 1ª expressão, senão, será executada a 2ª expressão.

```python
bonus = 0.20 if vendas >= meta else 0
```

Note que reduzimos nosso código em 5 linhas.


## Expressão Condicional (Casos de "ou"/"e")

Podemos usar uma Expressão Condicional que use os operadores **end** e **or**.

Vamos criar uma função  ganhou_bonus() que retorna True caso o funcionário tenha batido a méta (o funcionário recebe bônus caso bata a méta), senão, retona quantas unidades faltavem para bater a  meta e ganhar o bônus. Caso não conheça funções leia o ~~tutorial sobre funções~~ deste repositório.

```python
def ganhou_bonus(vendas, meta):
    if vendas >= meta:
        return True
    else: return f'Faltavam {meta - vendas} unidades para bater a meta'
```

Agora veremos uma função com uma Expressão Condicional para substituir essas 4 linhas de código.

Sintaxe:
<expressão booleana> or <expressão>

É avaliado se a expressão booleana é verdadeira, e se for, retorna True, caso não, retorna a 2ª Expressão

Experimente usar **end** no lugar de **or** e veja o que acontece.

```python
def ganhou_bonus(vendas, meta):
    return vendas >= meta or f'Faltavam {metas - vendas} unidades para bater a meta'
```
