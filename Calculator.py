def add(a, b):
    p=a+b
    print(p)

def sub(a, b):
    k=a-b
    print(k)

def mul(a, b):
    j=a*b
    print(j)

def div(a, b):
    v=a/b
    print(v)

a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=input('Enter the operator: ')

if c=='+':
    add(a, b)
elif c=='-':
    sub(a, b)
elif c=='*':
    mul(a, b)
elif c=='/':
    div(a, b)
else:
    print('Enter a valid operator')