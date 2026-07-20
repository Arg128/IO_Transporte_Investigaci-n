from pyomo.environ import *

# ---------------------------------------------------------
# Modelo de transporte con penalizacion por riesgo de accidentes
# Agroexportadora Valle Majes S.A.C. (caso ilustrativo, Arequipa)
# ---------------------------------------------------------

origenes = ['Majes', 'Camana', 'LaJoya']
destinos = ['Matarani', 'Lima', 'Cusco', 'Puno']

oferta = {'Majes': 1100, 'Camana': 700, 'LaJoya': 500}
demanda = {'Matarani': 900, 'Lima': 800, 'Cusco': 350, 'Puno': 250}

costo_flete = {  # S/. por tonelada
    ('Majes','Matarani'): 45, ('Majes','Lima'): 390, ('Majes','Cusco'): 220, ('Majes','Puno'): 135,
    ('Camana','Matarani'): 78, ('Camana','Lima'): 350, ('Camana','Cusco'): 250, ('Camana','Puno'): 160,
    ('LaJoya','Matarani'): 55, ('LaJoya','Lima'): 405, ('LaJoya','Cusco'): 210, ('LaJoya','Puno'): 125,
}

indice_riesgo = {  # escala 0-10, segun siniestralidad de la ruta (ONSV / PNP)
    ('Majes','Matarani'): 3, ('Majes','Lima'): 8, ('Majes','Cusco'): 7, ('Majes','Puno'): 6,
    ('Camana','Matarani'): 3, ('Camana','Lima'): 8, ('Camana','Cusco'): 8, ('Camana','Puno'): 7,
    ('LaJoya','Matarani'): 3, ('LaJoya','Lima'): 8, ('LaJoya','Cusco'): 6, ('LaJoya','Puno'): 5,
}

LAMBDA = 10  # S/. por punto de riesgo (costo social/seguro internalizado)

modelo = ConcreteModel(name="Transporte_AgroValleMajes")
modelo.I = Set(initialize=origenes)
modelo.J = Set(initialize=destinos)
modelo.x = Var(modelo.I, modelo.J, domain=NonNegativeReals)

def costo_total_rule(m):
    return sum((costo_flete[i,j] + LAMBDA*indice_riesgo[i,j]) * m.x[i,j]
               for i in m.I for j in m.J)
modelo.obj = Objective(rule=costo_total_rule, sense=minimize)

def oferta_rule(m, i):
    return sum(m.x[i,j] for j in m.J) == oferta[i]
modelo.r_oferta = Constraint(modelo.I, rule=oferta_rule)

def demanda_rule(m, j):
    return sum(m.x[i,j] for i in m.I) == demanda[j]
modelo.r_demanda = Constraint(modelo.J, rule=demanda_rule)

solver = SolverFactory('glpk')
resultado = solver.solve(modelo)

print("Estado del solver:", resultado.solver.status, "-", resultado.solver.termination_condition)
print(f"\nValor optimo de la funcion objetivo: S/. {value(modelo.obj):,.2f}\n")
print(f"{'Origen':<10}{'Destino':<10}{'Toneladas':>12}")
for i in modelo.I:
    for j in modelo.J:
        v = value(modelo.x[i,j])
        if v > 1e-6:
            print(f"{i:<10}{j:<10}{v:>12.1f}")
