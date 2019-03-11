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
def uniaoDisjunta(conj1, conj2):
    C = []
    D = []
    E = []
    F = []
    for a in conj1:
        C.append(a)
        D.append(C)
        C = []
    for b in conj2:
        E.append(b)
        F.append(E)
        E = []
    for c in D:
        c.append('Silva')
        C.append(c)
    for d in F:
        d.append('Souza')
        E.append(d)
    C.append(E)
    return C

    
A = {1,2,3}
B = {3,2,4}

Silva = {'Joao', 'Maria', 'Jose'}
Souza = {'Pedro', 'Ana', 'Jose'}

print('União: ',uniao(A,B))

print('Intersecção: ',interseccao(A,B))

print('Complemento: ',complemento(A,B))

print('Diferença: ',diferenca(A,B))

print('Conjunto das Partes: ',conjuntoDasPartes(A))

print('Produto Cartesiano: ')
produtoCartesiano(A,B)

print('União Disjunta: \n',uniaoDisjunta(Silva,Souza))
