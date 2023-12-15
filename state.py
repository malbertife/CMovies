from typing import NamedTuple


class Variable (NamedTuple):
        address:int
        value:str|int
        
class Frame (NamedTuple):
        variables: list[Variable]

        
a=Variable(address=120,value="Pippo")
b=Variable(address=12,value=12)
f=Frame(variables=[a,b])

print(f)

class Point (NamedTuple):
        x:int
        y:int=1
        
class Pippo():
        x:int
        y:int=1

def sum(a: int, b:int) -> int:
 return a +b

a = Point(3)
b = Point(3)

print(a == b)

c= Pippo()
c.x=2
d=Pippo()
d.x =2
print(c==d)
