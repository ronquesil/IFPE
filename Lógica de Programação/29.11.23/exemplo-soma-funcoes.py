#definição das funções
def soma(a,b):
    print(a+b)

def mult(a,b):
    print(a*b)

def sub():
    x = int(input())
    y = int(input())
    print(x-y)

def duasOperaoes():
    x = int(input())
    y = int(input())
    soma(x,y)
    mult(x,y)

#chamada as funções
##soma(2,9)
##soma(7,5)
##soma(18,30)
##
##mult(int(input()), int(input()))
##x = int(input())
##y = int(input())
##mult(x,y)

##sub()

duasOperaoes()