from typing import List
from copy import deepcopy


stack: list[str] = []


stack.append('a')
stack.append('b')
stack.append('c')


print('\nWhile:')

while stack:

    item = stack.pop()
    print(item)


print('\nSua pilha:', stack)