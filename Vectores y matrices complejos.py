import math
import cmath

# Operacion de numeros imaginarios.
def suma_vectores(a,b):
    vector = []
    for i in range(len(b)):
        vector.append(suma(a,b[i]))
    return vector

def inverso_vector(b):
    vector = []
    for i in range(len(b)):
        r = ((b[i][0])*(-1),b[i][1]*(-1))
        vector.append(r)
    return vector

def product_Esc_Comp(a,b):
    matriz = []
    for i in range(len(b)):
        matriz.append(producto(a,b[i]))
    return matriz

def adicion_matrices(c):
    matriz = []
    for i in range(len(c)):
        for j in range(len(c)):
            matriz.append(suma(c[i][j],c[i][j]))
    return matriz

def esc_matriz(a,c):
    matriz = []
    for i in range(len(b)):
        for j in range(len(b)):
            matriz.append(producto(a,c[i][j]))
    return matriz

def inverso_matriz(c):
    matriz = []
    for i in range(len(c)):
        matriz.append(inverso_vector(c[i]))
    return matriz

def trans(b):
    complejo = " "
    matriz_trans = b
    for i in range(len(b)):
        for j in range(i,len(b)):
            complejo = matriz_trans[j][i]
            matriz_trans[j][i] = matriz_trans[i][j]
            matriz_trans[i][j] = complejo
    return matriz_trans

def conjugada(c):
    matriz_conjugada = []
    for i in range(len(c)):
        for j in range(len(c)):
            matriz_conjugada.append(conjugado(c[i][j]))
    return matriz_conjugada

def adjunta(c):
    trans(c)
    matriz_adjunta = []
    for i in range(len(c)):
        for j in range(len(c)):
            con = conjugado(c[i][j])
            matriz_adjunta.append(con)
    return matriz_adjunta

def productoMatrices(c,c_exp):
    result_col = []
    result = []
    r = (0,0)
    for i in range(len(c)):
        for j in range(len(c[i])):
            result_col.append(r)
        result.append(result_col)
        result_col = []
    for i in range(len(c)):
        for j in range(len(c_exp[0])):
            for k in range(len(c_exp)):
                product = producto(c[i][k],c_exp[k][j])
                result[i][j] = suma(product,result[i][j])
    return result

def accion_vector(b,c):
    c = [[(4, 5), (2, 3)], [(1, 2), (4, 3)]]
    vector_producto = []
    suma_c = (0, 0)
    suma_d = (0, 0)
    for i in range(len(b)):
        for j in range(len(b)):
            suma_d = producto(c[i][j], b[j])
            suma_c = suma(suma_c, suma_d)
        vector_producto.append(suma_c)
    return vector_producto

def producto_interno(b,b_exp):
    vector_con = []
    vector_prod = []
    for i in range(len(b)):
        c = conjugado(b[i])
        vector_con.append(c)
    for i in range(len(b)):
        p = producto(vector_con[i],b_exp[0][i])
        vector_prod.append(p)
    return vector_prod

def norm_vector(b,b_exp):
    b = [(4, -3),(6, 4),(12, 7),(0,-13)]
    b_exp = [[(4, 3),(6, -4),(12, -7),(0, 13)]]
    norma = producto_interno(b,b_exp)
    s = (0,0)
    for i in range(len(norma)):
        s = suma(s,b[i])
    return str(s)+str("**1/2")

def distancia(c):
    vect = []
    for i in range(len(c)):
        v = resta(c[0][i],c[1][i])
        vect.append(v)
    c_r = [[(2, -2), (-3, 1)]]
    dist = norm_vector(vect,c_r)
    return dist

def matriz_unitaria(u):
    matriz_adjunta = u
    matriz_adjunta = [[(0, -1), (0, 0), (0, 0)], [(0, 0), (0, -1), (0, 0)], [(0, 0), (0, 0), (0, -1)]]
    p = productoMatrices(matriz_adjunta,u)
    matriz_u = []
    for i in range(len(u)):
        matriz_u.append(p[i][i])
    for i in range(len(matriz_u)):
        if matriz_u[i] != (1,0):
            return ("No es unitaria")
    return "Es unitaria"

def matriz_hermitania(h):
    matriz_adjunta = h
    matriz_adjunta = adjunta(matriz_adjunta)
    cont = 0
    h = [[(5, 0), (4, 5), (6, -16)], [(4, -5), (13, 0), (7, 0)], [(6, 16), (7, 0), (-2.1, 0)]]
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j] != matriz_adjunta[cont]:
                return "not"
            cont = cont + 1
    return "Es hermitania"

def suma(a,b):
    cc = (a[0] + b[0])
    ci = (a[1] + b[1])
    return (cc,ci)

def resta(a,b):
    cc = (a[0] - b[0])
    ci = (a[1] - b[1])
    return (cc, ci)

def producto(a,b):
    cc = ((a[0] * b[0]) - (a[1] * b[1]))
    ci = ((a[0] * b[1]) + (b[0] * a[1]))
    return (cc, ci)

def divicion(a,b):
    cc = (((a[0] * b[0]) + (b[1] * a[1])) / (b[0] * 2 + b[1] * 2))
    ci = (((b[0] * a[1]) - (a[0] * b[1])) / (b[0] * 2 + b[1] * 2))
    return(cc,ci)


def modulo(a):
    a = (((a[0]) * 2 + (a[1])*2) * (1 / 2))
    return a

def conjugado(a):
    a = (a[0],a[1] * (-1))
    return a

def rectangular_polar(a):
    cc = math.atan2(a[1], a[0])
    ci = math.sqrt((a[0] * a[0]) + (a[1] * a[1]))
    return(cc,ci)

def complejo(a):
    cc = (a[0] * cmath.cos(a[1]))
    ci = (a[0] * cmath.sin(a[1]))
    return(cc,ci)

def prettyprinting(a):
    if type(a) == tuple:
        if a[1] < 0:
            print(a[0],a[1],"i")
        elif a[1] == 0:
            print(a[0])
        else:
            print(a[0],"+",a[1],"i")
    else:
        print(a)

a = (4,5)
b = [(3,6),(9,3)]
b_exp = [[(3,6),(9,3)]]
c = [[(4,5),(2,3)],[(1,2),(4,3)]]
c_exp = [[(4,5),(2,3)],[(1,2),(4,3)]]
h = [[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]]
u = [[(0,1),(0,0),(0,0)],[(0,0),(0,1),(0,0)],[(0,0),(0,0),(0,1)]]


print(suma_vectores(a,b))
print(inverso_vector(b))
print(product_Esc_Comp(a,b))
print(adicion_matrices(c))
print(inverso_matriz(c))
print(esc_matriz(a,c))
print(trans(c_exp))
print(conjugada(c))
print(adjunta(c))
print(productoMatrices(c,c_exp))
print(accion_vector(b,c))
print(producto_interno(b,b_exp))
print(norm_vector(b,b_exp))
print(matriz_hermitania(h))
print(matriz_unitaria(u))
