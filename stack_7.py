from typing import List
from copy import deepcopy


stack: list[str] = []

try:
    stack.append('a')
    stack.append('b')
    stack.append('c')

    top_item = stack.pop() #C
    top_item = stack.pop() #B 
    top_item = stack.pop() #A
    top_item = stack.pop() #INDEX ERROR
    
except IndexError:
    print('Erro: A pilha está vazia!')

print(stack, top_item)