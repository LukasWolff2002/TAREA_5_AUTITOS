from sympy import symbols, Eq, solve
u = 30/1000


print('')
print('--------------------------')
print('PREGUNTA 1')
print('--------------------------')
print('')

T = 8 + u

#Hay dos posibles viajes
def d1 (h):
    return h + 10

def d2 (h):
    return 2*h+12

#El viaje mas barato si no hay flujo es d1

#Ahora identifico si con el total de viajes d1 sigue siendo mas barato
if d1(T) < d2(0):
    print('d1 sigue siendo mas barato')

else:
    print('es nesesario usar d2')

#Por lo tanto, hago el equilibrio

# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T)  # T = h1 + h2
equation2 = Eq(d1(h1), d2(h2))  # d1(h1) = d2(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))
print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}')

#verifico
print(f'costo 1: {d1(solution[h1])}, costo 2: {d2(solution[h2])}')

print('')
print('--------------------------')
print('PREGUNTA 2')
print('--------------------------')
print('')

T = 8 + u

#Hay dos posibles viajes
def d1 (h):
    return h + 10

def d2 (h):
    return 2*h+12

def d3 (h):
    return h+15

#Si no hay flujo, el orden de vias es
#d1, d2, d3

#Ahora identifico si con el total de viajes d1 sigue siendo mas barato
if d1(T) < d2(0):
    print('d1 sigue siendo mas barato')

else:
    print('es nesesario usar d2')

#Por lo tanto, hago el equilibrio para d1 y d2 y veo si es nesesario usar d3

# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T)  # T = h1 + h2
equation2 = Eq(d1(h1), d2(h2))  # d1(h1) = d2(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))

print(f'costo 1: {d1(solution[h1])}, costo 2: {d2(solution[h2])}, costo 3: {d3(0)}')
print('debo usar d3')
#Por lo tanto, si es conveniente usar el tramo 3

# Definir las variables
h1, h2, h3 = symbols('h1 h2 h3')

equation1 = Eq(h1 + h2 + h3, T)  # T = h1 + h2 + h3
equation2 = Eq(d1(h1), d2(h2))  # d1(h1) = d2(h2)
equation3 = Eq(d1(h1), d3(h3))  # d1(h1) = d3(h3)

# Resolver el sistema
solution = solve((equation1, equation2, equation3), (h1, h2, h3))
print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}, h3 = {solution[h3]}')

#verifico
print(f'costo 1: {d1(solution[h1])}, costo 2: {d2(solution[h2])}, costo 3: {d3(solution[h3])}')

print('')
print('--------------------------')
print('PREGUNTA 3')
print('--------------------------')
print('')

T = 4 + u

#Hay dos posibles viajes
def d1 (h):
    return h + 10

def d2 (h):
    return 2*h+12

def d3 (h):
    return h+15

#Si no hay flujo, el orden de vias es
#d1, d2, d3

#Ahora identifico si con el total de viajes d1 sigue siendo mas barato
if d1(T) < d2(0):
    print('d1 sigue siendo mas barato')

else:
    print('es nesesario usar d2')

#Por lo tanto, hago el equilibrio para d1 y d2 y veo si es nesesario usar d3

# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T)  # T = h1 + h2
equation2 = Eq(d1(h1), d2(h2))  # d1(h1) = d2(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))

print(f'costo 1: {d1(solution[h1])}, costo 2: {d2(solution[h2])}, costo 3: {d3(0)}')
print('no debo usar d3')
#Por lo tanto, no es conveniente usar el tramo 3

#por lo tanto, los flujos son:

print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}, h3 = 0')

#Verifico
print(f'costo 1: {d1(solution[h1])}, costo 2: {d2(solution[h2])}, costo 3: {d3(0)}')

print('')
print('--------------------------')
print('PREGUNTA 4')
print('--------------------------')
print('')

#Ahora tengo 2 flujos de viajes
T12 = 20+u
T21 = 10+u

#Es decir, hay viajes de ida y vuelta
#Definamos los costos de los viajes

def d12 (h):
    return h + 8

def d14 (h):
    return h+8

def d23 (h):
    return h+5

def d43 (h):
    return h+5

def d24 (h):
    return h+14

def d31 (h):
    return h

#Bien, ahora puedo definir las distintas rutas posibles

#Para los viajes de 1 a 2
def r1_12 (h):
    return d12(h)

#Para los viajes de 2 a 1
def r1_21 (h):
    return d23(h) + d31(h)

def r2_21 (h):
    return d24(h) + d43(h) + d31(h)

#Por lo tanto, para el viaje de ida el flujo es
f12 = T12
print('el flujo de 1 a 2 solo usa una ruta y es: ', f12, 'donde el costo es: ', r1_12(f12))

#Para el viaje de vuelta
#primero identifico la ruta mas barata

if r1_21(0) < r2_21(0):
    print('la ruta mas barata es 1')

else:
    print('la ruta mas barata es 2')

#Ahora veo si con el flujo total, la ruta 1 sigue siendo la mas barata

if r1_21(T21) < r2_21(0):
    print('la ruta 1 sigue siendo la mas barata')
else:
    print('es nesesario usar la ruta 2')

#Por lo tanto, hago el equilibrio
# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T21)  # T = h1 + h2
equation2 = Eq(r1_21(h1), r2_21(h2))  # r1_21(h1) = r2_21(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))

print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}')
print(f'costo 1: {r1_21(solution[h1])}, costo 2: {r2_21(solution[h2])}')

print('estan mal, ya que en el tramo 3-1 pasan todos los flujos')

# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T21)  # T = h1 + h2
equation2 = Eq(d23(h1) , d24(h2)+ d43(h2))  # r1_21(h1) = r2_21(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))

print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}')
#print(f'costo 1: {r1_21(solution[h1])}, costo 2: {r2_21(solution[h2])}')













print('')
print('--------------------------')
print('PREGUNTA 5')
print('--------------------------')
print('')

#Igualmente tengo 2 flujos de viajes
T01 = 200 + 10*u
T02 = 200 + 10*u

#Defino los costos de cada arco

def d0a (h):
    return 1 + (h/10)

def d0b (h):
    return 1 + (h/10)

def d02 (h):
    return 2 + (h/10)

def dab (h):
    return 1 + (h/10)

def da1 (h):
    return 1 + (h/10)

def db1 (h):
    return 1 + (h/10)

def db2 (h):
    return 1 + (h/10)

#bien, ahora defino las posibles rutas para cada viajes
#Desde 0 a 1

def r1_01 (h):
    return d0a(h) + da1(h)

def r2_01 (h):
    return d0b(h) + db1(h)

def r3_01 (h):
    return d0a(h) + dab(h) + db1(h)

#Ahora para el viaje de 0 a 2

def r1_02 (h):
    return d02(h)

def r2_02 (h):
    return d0b(h) + db2(h)

def r3_02 (h):
    return d0a(h) + dab(h) + db2(h)

#Bien, comienzo con el viaje de 0 a 1
print('para los viajes de 0 a 1')
#Primero identifico la ruta mas barata
print(r1_01(0), r2_01(0), r3_01(0))
print('la ruta 1 y 2 tienen un costo igual con flujo 0, por lo tanto hago un equilibrio entre ellas')

# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T01)  # T = h1 + h2
equation2 = Eq(r1_01(h1), r2_01(h2))  # r1_01(h1) = r2_01(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))

h1 = solution[h1]
h2 = solution[h2]

#Verifico que no se deba usar la ruta 3
print(r1_01(h1), r2_01(h2), r3_01(0))
print('debo usar la ruta 3')

# Definir las variables
h1, h2, h3 = symbols('h1 h2 h3')

equation1 = Eq(h1 + h2 + h3, T01)  # T = h1 + h2 + h3
equation2 = Eq(r1_01(h1), r2_01(h2))  # r1_01(h1) = r2_01(h2)
equation3 = Eq(r1_01(h1), r3_01(h3))  # r1_01(h1) = r3_01(h3)

# Resolver el sistema
solution = solve((equation1, equation2, equation3), (h1, h2, h3))
print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}, h3 = {solution[h3]}')

#Verifico
print(f'costo 1: {r1_01(solution[h1])}, costo 2: {r2_01(solution[h2])}, costo 3: {r3_01(solution[h3])}')

print('')
print('para los viajes de 0 a 2')

#Primero identifico la ruta mas barata
print(r1_02(0), r2_02(0), r3_02(0))
print('la ruta 1 y 2 tienen un costo igual con flujo 0, por lo tanto hago un equilibrio entre ellas')

# Definir las variables
h1, h2 = symbols('h1 h2')

equation1 = Eq(h1 + h2, T02)  # T = h1 + h2
equation2 = Eq(r1_02(h1), r2_02(h2))  # r1_02(h1) = r2_02(h2)

# Resolver el sistema
solution = solve((equation1, equation2), (h1, h2))

h1 = solution[h1]
h2 = solution[h2]

#Verifico que no se deba usar la ruta 3
print(r1_02(h1), r2_02(h2), r3_02(0))
print('debo usar la ruta 3')

# Definir las variables
h1, h2, h3 = symbols('h1 h2 h3')

equation1 = Eq(h1 + h2 + h3, T02)  # T = h1 + h2 + h3
equation2 = Eq(r1_02(h1), r2_02(h2))  # r1_02(h1) = r2_02(h2)
equation3 = Eq(r1_02(h1), r3_02(h3))  # r1_02(h1) = r3_02(h3)

# Resolver el sistema
solution = solve((equation1, equation2, equation3), (h1, h2, h3))

print(f'Solución: h1 = {solution[h1]}, h2 = {solution[h2]}, h3 = {solution[h3]}')

#Verifico
print(f'costo 1: {r1_02(solution[h1])}, costo 2: {r2_02(solution[h2])}, costo 3: {r3_02(solution[h3])}')

#Pero surge un problema, las rutas se usan simultaneamente, por lo tanto, debo hacer un equilibrio entre los dos viajes
print('')
print('Las rutas se usan simultaneamente')

# Definir las variables
h1_1, h2_1, h3_1, h1_2, h2_2, h3_2 = symbols('h1_1 h2_1 h3_1 h1_2 h2_2 h3_2')

equation1 = Eq(h1_1 + h2_1 + h3_1, T01)  # T = h1 + h2 + h3
equation2 = Eq(h1_2 + h2_2 + h3_2, T02)  # T = h1 + h2 + h3

equation3 = Eq(d0a(h1_1 + h3_1 + h3_2) + da1(h1_1), d0b(h2_1 + h2_2) + db1(h2_1 + h3_1))  # r1_01(h1) = r2_01(h2)
equation4 = Eq(d0a(h1_1 + h3_1 + h3_2) + da1(h1_1), d0a(h1_1 + h3_1 + h3_2) + dab(h3_1 + h3_2) + db1(h2_1 + h3_1))  # r1_01(h1) = r3_01(h2)

equation5 = Eq(d02(h1_2), d0b(h2_1 + h2_2) + db2(h2_2+h3_2))  # r1_02(h1) = r2_02(h2)
equation6 = Eq(d02(h1_2), d0a(h1_1 + h3_1 + h3_2) + dab(h3_1 + h3_2) + db2(h2_2+h3_2))  # r1_02(h1) = r3_02(h2)

# Resolver el sistema
solution = solve((equation1, equation2, equation3, equation4, equation5, equation6), (h1_1, h2_1, h3_1, h1_2, h2_2, h3_2))
print(solution)
print(f'Solución: h1_1 = {solution[h1_1]}, h2_1 = {solution[h2_1]}, h3_1 = {solution[h3_1]}, h1_2 = {solution[h1_2]}, h2_2 = {solution[h2_2]}, h3_2 = {solution[h3_2]}')