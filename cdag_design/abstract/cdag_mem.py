
"""
pointer:
    - o nome dele é relativo ao atributo usado no código
    - sempre aponta ou pra outro ponteiro ou pra memória

    exemplo:
        main: adds [1 3] as v1
    - atributo v1
    - nome do pointer: main_v1

    exemplo:
        pointer = {'main_v1': 1, 'main_v2': 'main_v1'}
"""
pointer = {}

"""
mem: 
    - sempre tem uma chave incremental
    - contém o valor da variável
    
    exemplo:
        mem = {1: {'value': 4, 'type': 'integer'}}
"""
mem = {}








"""CDAGGER:

main: adds [1 3] as v1
      applies [with x: maps [v1]]
where
x: sets [*v1] as v1

"""