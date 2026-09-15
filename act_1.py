import random

#Algoritmo Genético de Optimización Numérica
# Parámetros del Algoritmo Genético
LONGITUD_CROMOSOMA = 5  # 5 bits permiten representar números del 0 al 31
TAMANO_POBLACION = 10
TASA_MUTACION = 0.1
GENERACIONES = 15

def crear_individuo():
    # Genera una lista de 5 bits aleatorios (0 o 1)
    return [random.randint(0, 1) for _ in range(LONGITUD_CROMOSOMA)]

def binario_a_decimal(individuo):
    # Convierte la lista de bits a un número entero decimal
    cadena = "".join(str(bit) for bit in individuo)
    return int(cadena, 2)

def fitness(individuo):
    # Queremos maximizar la función f(x) = x^2
    x = binario_a_decimal(individuo)
    return x ** 2

def seleccion_ruleta(poblacion):
    # Selecciona un padre basado en su proporción de fitness (método de la ruleta)
    fitnesses = [fitness(ind) for ind in poblacion]
    total_fitness = sum(fitnesses)
    
    if total_fitness == 0:
        return random.choice(poblacion)
    
    punto = random.uniform(0, total_fitness)
    actual = 0
    for ind, fit in zip(poblacion, fitnesses):
        actual += fit
        if actual >= punto:
            return ind
    return poblacion[-1]

def cruce(padre1, padre2):
    # Cruce de un solo punto
    punto = random.randint(1, LONGITUD_CROMOSOMA - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

def mutar(individuo):
    # Invierte un bit (0 a 1 o 1 a 0) según la probabilidad de mutación
    for i in range(LONGITUD_CROMOSOMA):
        if random.random() < TASA_MUTACION:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico():
    # 1. Crear población inicial
    poblacion = [crear_individuo() for _ in range(TAMANO_POBLACION)]
    
    print("--- INICIANDO OPTIMIZACIÓN GENÉTICA ---")
    
    for gen in range(GENERACIONES):
        # 2. Ordenar de mayor a menor según el fitness
        poblacion = sorted(poblacion, key=fitness, reverse=True)
        mejor = poblacion[0]
        x_val = binario_a_decimal(mejor)
        
        print(f"Gen {gen + 1:2d} | Bits: {''.join(str(b) for b in mejor)} | x = {x_val:2d} | Fitness (x^2) = {fitness(mejor)}")
        
        # 3. Elitismo: pasamos al mejor directamente a la siguiente generación
        nueva_poblacion = [mejor[:]] 
        
        # 4. Crear el resto de la nueva población por selección, cruce y mutación
        while len(nueva_poblacion) < TAMANO_POBLACION:
            p1 = seleccion_ruleta(poblacion)
            p2 = seleccion_ruleta(poblacion)
            h1, h2 = cruce(p1, p2)
            
            nueva_poblacion.append(mutar(h1))
            if len(nueva_poblacion) < TAMANO_POBLACION:
                nueva_poblacion.append(mutar(h2))
                
        poblacion = nueva_poblacion

algoritmo_genetico()
