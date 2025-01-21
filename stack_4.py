from typing import List
from copy import deepcopy


stack: list[str] = []


stack.append('a')
stack.append('b')
stack.append('c')


print('\nfor:')

for item in stack[::-1]:
    print(item)

stack_copy = stack.copy()

print('\nwhile:')
while stack_copy:    
    item = stack_copy.pop()
    print(item)

print('\nSua pilha:', stack)