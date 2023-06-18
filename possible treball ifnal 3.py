import random
import math

# Constants Lennard-Jones
EPSILON = 1.0   
SIGMA = 1.0  

# Parametres simulacio MC
PASOS_MC = 1000  # Numero de passos de la simulacio
PARTICULES_GAS = 40  # Numero inicial de particules de gas
PARTICULES_LIQUID = 40  # Numero inicial de particules de líquid


particules_gas = []
particules_liquid = []

# Funcions d'energía
def ini_gas(particules):
    # Calcula l'energía de la caixa "gas", originalment la poso a 0 per calcular-la amb LJ
    
    
    for step in range(PARTICULES_GAS):
        # Poso particules gas en posicions aleatories (capsa 10x10x10)
        x=random.uniform(0, 10)
        y=random.uniform(0, 10)
        z=random.uniform(0, 10)
        particules_gas.append((x, y, z))
def  energia_gas(particules):
    energia_gas = 0.0
        # Calcula las interaccions Lennard-Jones de cada parella
    for triplet in particules_gas:
        for triplet2 in particules_gas:
            if triplet != triplet2:
                temp=[
                triplet2[0] - triplet[0],
                triplet2[1] - triplet[1],
                triplet2[2] - triplet[2]]
                r_2 = temp[0]**2 + temp[1]**2 + temp[2]**2
                r_6 = r_2**3
                r_12 = r_6**2
                energia_gas += 4 * EPSILON * ((SIGMA**12 / r_12) - (SIGMA**6 / r_6))
    return energia_gas


def ini_liquid(particules):

    for step2 in range(PARTICULES_LIQUID):
        x=random.uniform(0, 10)
        y=random.uniform(0, 10)
        z=random.uniform(0, 10)
        particules_liquid.append((x, y, z))

def energia_liquid(particules):
    energia_liquid = 0.0
    for triplet in particules_liquid:
         for triplet2 in particules_liquid:
            if triplet != triplet2:
                temp=[
                triplet2[0] - triplet[0],
                triplet2[1] - triplet[1],
                triplet2[2] - triplet[2]]
                r_2 = temp[0]**2 + temp[1]**2 + temp[2]**2
                r_6 = r_2**3
                r_12 = r_6**2
                energia_liquid += 4 * EPSILON * ((SIGMA**12 / r_12) - (SIGMA**6 / r_6))
    return energia_liquid


    
def montecarlo(particules_gas, particules_liquid, energia_total):
    # Fer Monte Carlo
    for pas in range(PASOS_MC):
        # Selecciono aleatoriament si canvio un gas o un liquid de capsa, si al generar numero aleatori (0 o 1) dona 0 faig gas a liquid si dona 1 faig liquid a gas
        if random.random() < 0.5:  # Gas a liquid
            if len(particules_gas) > 0:
                particules_gas.pop(random.randint(0, len(particules_gas) - 1))
                particules_liquid.append((random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)))
        else:  # Liquid a gas
            if len(particules_liquid) > 0:
                particules_liquid.pop(random.randint(0, len(particules_liquid) - 1))
                particules_gas.append((random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)))

        energia_temp=energia_gas(particules_gas)+energia_liquid(particules_liquid)
        if energia_temp < energia_total:
            energia_total=energia_temp
        if pas%100 == 0:
            print("L'energia del pas " + str(pas)+" és "+str (energia_total))


        
    # Imprimir el estado de equilibrio
    print("Partícules de gas:", len(particules_gas))
    print("Partícules de líquid:", len(particules_liquid))
    return energia_total


if __name__ == '__main__':
    ini_gas(particules_gas)
    ini_liquid(particules_liquid)
    energia_gas_total = energia_gas(particules_gas)
    energia_liquid_total = energia_liquid(particules_liquid)
    energia_total = energia_gas_total+energia_liquid_total
    print("L'energia total inicial serà de :" + str(energia_total)) #str es per fer que els dos siguin del mateix tipus i poder concatenarlos
    energia_montecarlo=montecarlo(particules_gas, particules_liquid, energia_total)
    print("L'energia de l'estat d'equilibri serà de:" +str(energia_montecarlo))





