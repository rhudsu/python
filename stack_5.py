from typing import List
from copy import deepcopy


stack: list[str] = []


stack.append('a')
stack.append('b')
stack.append('c')


##NAO FAÇA ISSO 
first_stack = stack.pop(0)

print(stack, first_stack)