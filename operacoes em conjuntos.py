#União
def uniao(conj1,conj2):
    C = set()
    for a in conj1:
        C.add(a)
    for b in conj2:
        if b not in C:
            C.add(b)
    return C

#Intersecção
def interseccao(conj1,conj2):
    C = set()
    for a in conj1:
        for b in conj2:
            if a == b:
                C.add(a)
    return C

#Complemento
def complemento(conj1,conj2):
    C = set()
    for b in conj2:
        if b not in conj1:
            C.add(b)
    return C

#Diferença
def diferenca(conj1, conj2):
    C = set()
    for a in conj1:
        if a not in conj2:
            C.add(a)
    return C

#Conjunto das Partes (não finalizado)
def conjuntoDasPartes(conj1):
    C = []
    D = []
    for a in conj1:
        C.append(a)
        D.append(C)
        C = []
    C = D
    for b in range(len(conj1)-1):
        C[b].append(D[b+1])
        D.append(C)
    return D

#ProdutoCartesiano
def produtoCartesiano(conj1, conj2):
    for a in conj1:
        for b in conj2:
            print('(a:{0} b:{1})'.format(a,b))


#União Disjunta
def uniaoDisjunta(conjunto1, conjunto2):
    C = []
    D = []
    E = []
    for a in conjunto1:
        C.append(a)
        C.append('conjunto1')
        D.append(C)
        C = []
    for b in conjunto2:
        E.append(b)
        E.append('conjunto2')
        D.append(E)
        E = []
    return D

    
A = {1,2,3}
B = {3,2,4}

conjunto1 = {'Joao', 'Maria', 'Jose'}
conjunto2 = {'Pedro', 'Ana', 'Jose'}

print('União: ',uniao(A,B))

print('Intersecção: ',interseccao(A,B))

print('Complemento: ',complemento(A,B))

print('Diferença: ',diferenca(A,B))

print('Conjunto das Partes: ',conjuntoDasPartes(A))

print('Produto Cartesiano: ')

produtoCartesiano(A,B)

print('União Disjunta: \n',uniaoDisjunta(conjunto1,conjunto2))
