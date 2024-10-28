from sympy import symbols, Eq, solve

u = 30 / 1000
print(u)

def define_cost_functions():
    # Definición de funciones de costo genéricas para d1, d2, d3
    def d1(h):
        return h + 10

    def d2(h):
        return 2 * h + 12

    def d3(h):
        return h + 15

    return d1, d2, d3

def define_routes_4():
    # Definición de funciones de costo para las rutas de A a B y de B a A
    def dA3(h):
        return h + 5

    def d31(h):
        return h

    def d1B(h):
        return h + 8

    def dAB(h):
        return h + 14

    def d1A(h):
        return h + 8

    # Rutas de A a B
    def r1_AB(h):
        return dA3(h) + d31(h) + d1B(h)

    def r2_AB(h):
        return dAB(h) #+ d1B(h)

    # Ruta de B a A (actualizada)
    def r1_BA(h):
        return d1B(h) + d31(h) + d1A(h)

    return r1_AB, r2_AB, r1_BA

def evaluate_costs(solution, h_vars, routes):
    # Evaluar los costos con la solución obtenida
    return [routes[i](solution[h_vars[i]]) for i in range(len(routes))]

def solve_flow_equilibrium_4(routes, total_flow):
    # Resolver el equilibrio de flujo para una lista de rutas específicas
    num_routes = len(routes)
    
    if num_routes == 1:
        # Caso especial donde solo hay una ruta
        return {symbols('h1'): total_flow}, [symbols('h1')]

    # Definir variables para cada ruta
    h_vars = symbols(' '.join([f'h{i + 1}' for i in range(num_routes)]))

    # Definir ecuaciones de equilibrio
    equations = [Eq(sum(h_vars), total_flow)]  # Suma de flujos debe ser igual a total_flow
    for i in range(1, num_routes):
        equations.append(Eq(routes[0](h_vars[0]), routes[i](h_vars[i])))

    # Resolver el sistema de ecuaciones
    solution = solve(equations, h_vars)
    if not solution:
        return None
    return solution, h_vars

def define_cost_functions_5():
    # Definición de funciones de costo específicas para la pregunta 5
    def d0a(h):
        return 1 + (h / 10)

    def d0b(h):
        return 1 + (h / 10)

    def d02(h):
        return 2 + (h / 10)

    def dab(h):
        return 1 + (h / 10)

    def da1(h):
        return 1 + (h / 10)

    def db1(h):
        return 1 + (h / 10)

    def db2(h):
        return 1 + (h / 10)

    # Rutas posibles
    def r1_01(h):
        return d0a(h) + da1(h)

    def r2_01(h):
        return d0b(h) + db1(h)

    def r3_01(h):
        return d0a(h) + dab(h) + db1(h)

    def r1_02(h):
        return d02(h)

    def r2_02(h):
        return d0b(h) + db2(h)

    def r3_02(h):
        return d0a(h) + dab(h) + db2(h)

    return r1_01, r2_01, r3_01, r1_02, r2_02, r3_02

def solve_flow_equilibrium_5(routes, total_flow):
    # Resolver el equilibrio de flujo para una lista de rutas específicas
    num_routes = len(routes)
    if num_routes < 2:
        return None  # Necesitamos al menos dos rutas

    # Definir variables para cada ruta
    h_vars = symbols(' '.join([f'h{i + 1}' for i in range(num_routes)]))

    # Definir ecuaciones de equilibrio
    equations = [Eq(sum(h_vars), total_flow)]  # Suma de flujos debe ser igual a total_flow
    for i in range(1, num_routes):
        equations.append(Eq(routes[0](h_vars[0]), routes[i](h_vars[i])))

    # Resolver el sistema de ecuaciones
    solution = solve(equations, h_vars)
    return solution, h_vars

def solve_flow_equilibrium(cost_functions, total_flow):
    # Resolver el equilibrio de flujo para una lista de funciones de costo
    num_routes = len(cost_functions)
    if num_routes < 2:
        return None  # Necesitamos al menos dos rutas

    # Definir variables para cada ruta
    h_vars = symbols(' '.join([f'h{i + 1}' for i in range(num_routes)]))

    # Definir ecuaciones de equilibrio
    equations = [Eq(sum(h_vars), total_flow)]  # Suma de flujos debe ser igual a total_flow
    for i in range(1, num_routes):
        equations.append(Eq(cost_functions[0](h_vars[0]), cost_functions[i](h_vars[i])))

    # Resolver el sistema de ecuaciones
    solution = solve(equations, h_vars)
    return solution, h_vars

def evaluate_costs(solution, h_vars, cost_functions):
    # Evaluar los costos con la solución obtenida
    return [cost_functions[i](solution[h_vars[i]]) for i in range(len(cost_functions))]

def main():
    print('\n--------------------------')
    print('PREGUNTA 1')
    print('--------------------------\n')

    T = 8 + u
    d1, d2, _ = define_cost_functions()

    # Comparación inicial sin flujo
    if d1(T) < d2(0):
        print('d1 sigue siendo más barato')
    else:
        print('Es necesario usar d2')

    # Resolver equilibrio entre d1 y d2
    solution, h_vars = solve_flow_equilibrium([d1, d2], T)
    print(f'Solución: {solution}')
    print(f'Costos: {evaluate_costs(solution, h_vars, [d1, d2])}\n')

    print('\n--------------------------')
    print('PREGUNTA 2')
    print('--------------------------\n')

    T = 8 + u
    d1, d2, d3 = define_cost_functions()

    # Comparación inicial sin flujo
    if d1(T) < d2(0):
        print('d1 sigue siendo más barato')
    else:
        print('Es necesario usar d2')

    # Resolver equilibrio para d1 y d2
    solution, h_vars = solve_flow_equilibrium([d1, d2], T)
    costos = evaluate_costs(solution, h_vars, [d1, d2])
    print(f'Costos: {costos}, Costo d3: {d3(0)}')

    # Evaluar si es necesario usar d3
    if costos[0] > d3(0):
        print('Debo usar d3')

        # Resolver equilibrio para d1, d2 y d3
        solution, h_vars = solve_flow_equilibrium([d1, d2, d3], T)
        print(f'Solución: {solution}')
        print(f'Costos: {evaluate_costs(solution, h_vars, [d1, d2, d3])}\n')

    print('\n--------------------------')
    print('PREGUNTA 3')
    print('--------------------------\n')

    T = 4 + u
    d1, d2, d3 = define_cost_functions()

    # Comparación inicial sin flujo
    if d1(T) < d2(0):
        print('d1 sigue siendo más barato')
    else:
        print('Es necesario usar d2')

    # Resolver equilibrio para d1 y d2
    solution, h_vars = solve_flow_equilibrium([d1, d2], T)
    costos = evaluate_costs(solution, h_vars, [d1, d2])
    print(f'Costos: {costos}, Costo d3: {d3(0)}')

    # Evaluar si es necesario usar d3
    if costos[0] <= d3(0):
        print('No debo usar d3')
        print(f'Solución: {solution}, h3 = 0\n')

    #Donde los costos son:
    costos = [d1(solution[h_vars[0]]), d2(solution[h_vars[1]]), d3(0)]
    print(f'Costos: {costos}\n')

    print('\n--------------------------')
    print('PREGUNTA 4')
    print('--------------------------\n')

    TAB = 20 + u
    TBA = 10 + u

    # Definir las rutas
    r1_AB, r2_AB, r1_BA = define_routes_4()

    # Flujo de A a B
    print('Para el flujo de A a B')
    
        
    solution, h_vars = solve_flow_equilibrium_4([r1_AB, r2_AB], TAB)
    print(f'Solución para equilibrio A-B: {solution}')
    print(f'Costos: {evaluate_costs(solution, h_vars, [r1_AB, r2_AB])}\n')

    # Flujo de B a A (solo una ruta)
    print('Para el flujo de B a A')
    flujo_BA = TBA
    print(f'El flujo de B a A usa la única ruta disponible con un costo de {r1_BA(flujo_BA)}\n')
    print(flujo_BA)
    print('\n--------------------------')
    print('PREGUNTA 5')
    print('--------------------------\n')

    T01 = 200 + 10 * u
    T02 = 200 + 10 * u

    # Definir las rutas
    r1_01, r2_01, r3_01, r1_02, r2_02, r3_02 = define_cost_functions_5()

    # Para viajes de 0 a 1
    print('Para los viajes de 0 a 1')
    if r1_01(0) == r2_01(0):
        print('La ruta 1 y 2 tienen un costo igual con flujo 0, por lo tanto hago un equilibrio entre ellas')
        solution, h_vars = solve_flow_equilibrium_5([r1_01, r2_01], T01)
        print(f'Solución: {solution}')

        # Verificar si es necesario usar la ruta 3
        if r1_01(solution[h_vars[0]]) > r3_01(0):
            print('Debo usar la ruta 3')
            solution, h_vars = solve_flow_equilibrium_5([r1_01, r2_01, r3_01], T01)
            print(f'Solución completa: {solution}')
            costos = evaluate_costs(solution, h_vars, [r1_01, r2_01, r3_01])
            print(f'Costos: {costos}\n')
        else:
            costos = evaluate_costs(solution, h_vars, [r1_01, r2_01])
            print(f'Costos: {costos}\n')

    # Para viajes de 0 a 2
    print('Para los viajes de 0 a 2')
    if r1_02(0) == r2_02(0):
        print('La ruta 1 y 2 tienen un costo igual con flujo 0, por lo tanto hago un equilibrio entre ellas')
        solution, h_vars = solve_flow_equilibrium_5([r1_02, r2_02], T02)
        print(f'Solución: {solution}')

        # Verificar si es necesario usar la ruta 3
        if r1_02(solution[h_vars[0]]) > r3_02(0):
            print('Debo usar la ruta 3')
            solution, h_vars = solve_flow_equilibrium_5([r1_02, r2_02, r3_02], T02)
            print(f'Solución completa: {solution}')
            costos = evaluate_costs(solution, h_vars, [r1_02, r2_02, r3_02])
            print(f'Costos: {costos}\n')
        else:
            costos = evaluate_costs(solution, h_vars, [r1_02, r2_02])
            print(f'Costos: {costos}\n')

    # Equilibrio simultáneo entre dos viajes
    print('Las rutas se usan simultáneamente')
    h1_1, h2_1, h3_1, h1_2, h2_2, h3_2 = symbols('h1_1 h2_1 h3_1 h1_2 h2_2 h3_2')

    equation1 = Eq(h1_1 + h2_1 + h3_1, T01)  # T01 para viaje de 0 a 1
    equation2 = Eq(h1_2 + h2_2 + h3_2, T02)  # T02 para viaje de 0 a 2

    # Definición de ecuaciones para equilibrio simultáneo
    equation3 = Eq(r1_01(h1_1), r2_01(h2_1))  # Equilibrio entre rutas 0 a 1
    equation4 = Eq(r1_01(h1_1), r3_01(h3_1))  # Equilibrio entre ruta 1 y 3 (0 a 1)
    equation5 = Eq(r1_02(h1_2), r2_02(h2_2))  # Equilibrio entre rutas 0 a 2
    equation6 = Eq(r1_02(h1_2), r3_02(h3_2))  # Equilibrio entre ruta 1 y 3 (0 a 2)

    # Resolver el sistema de ecuaciones simultáneas
    solution = solve((equation1, equation2, equation3, equation4, equation5, equation6), 
                     (h1_1, h2_1, h3_1, h1_2, h2_2, h3_2))
    print(f'Solución completa: {solution}')
    #Donde los costos son:

    costos = [r1_01(solution[h1_1]), r2_01(solution[h2_1]), r3_01(solution[h3_1]),r1_02(solution[h1_2]), r2_02(solution[h2_2]), r3_02(solution[h3_2])]
    print(f'Costos: {costos}\n')
if __name__ == "__main__":
    main()
