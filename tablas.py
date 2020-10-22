booleanos = [True, False]
lista = []
d=[]
c=[]
con=[]
bcon=[]
n=[]
p = []
q = []
r = []

for x in booleanos:
    for y in booleanos:
        for z in booleanos:
            p.append(x)
            q.append(y)
            r.append(z)

print(p)
print(q)
print(r)

def disyuncion(a, b, c): # Tabla de verdad de or  
    print('p\tq\tp or q')
    print('-'*22)
    for x in range(0,8):
        print(a[x] ,b[x] ,a[x] or b[x], sep = '\t')
        c.append(a[x] or b[x])
        
    return c
    
def conjuncion(a,b,c): # Tabla de verdad de and
    print('p\tq\tp and q')
    print('-'*22)
    for x in range(0,8):
        print(a[x] ,b[x] ,a[x] and b[x], sep = '\t')
        c.append(a[x] and b[x])
        
    return c
        
def condicional(a,b,c): # Tabla de verdad de →
    print('p\tq\tp → q')
    print('-'*22)
    for x in range(0,8):
        print(a[x] ,b[x] ,not a[x] or b[x], sep = '\t')
        c.append(not a[x] or b[x])
        
    return c

def bicondicional(a,b,c): # Tabla de verdad de ↔
    print('x\ty\tx ↔ y')
    print('-'*22)
    for x in range(0,8):
        print(a[x] ,b[x] ,(not a[x] or b[x]) and (not b[x] or a[x]), sep = '\t')
        c.append((not a[x] or b[x]) and (not b[x] or a[x]))
        
    return c

def negacion(a,b): #Tabla de negacion
    print('x\t-x')
    print('-'*22)
    for x in range(0,8):
        print(a[x] ,(not a[x]), sep = '\t')
        b.append(not a[x])

    return b

print(disyuncion(p,q,d))
print(conjuncion(p,q,c))
print(condicional(p,q,con))
print(bicondicional(p,q,bcon))
print(negacion(p,n))
