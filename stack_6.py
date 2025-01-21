from typing import List
from copy import deepcopy


stack: list[str] = []


stack.append('a')
stack.append('b')
stack.append('c')

top_item = stack.pop() #C
top_item = stack.pop() #B 
top_item = stack.pop() #A
top_item = stack.pop() #INDEX ERROR


print(stack, top_item)