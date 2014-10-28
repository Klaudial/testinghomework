def energy(density, coeff=1.0, temp):
    
    energysum = 0
    density = [1.0, 1.0]
    
   
    for value in density:
        energyind = value
        energyminus = value -1
        energyprod = energyind*energyminus

        energysum = (energysum + energyprod)
    energysum = energysum*coeff/2
    
    print energysum
    return energysum