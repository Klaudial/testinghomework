#initialise stuff
class MonteCarloAlgorithm(object):
#default temperature is standard lab temperature in Kelvin
    def __init__(self, temperature=295, iternumb=100):
    
        if temperature<0:
                raise ValueError("Work in Kelvin: no negative temperatures!")
    
        if temperature==0:
                raise ValueError("Temperature should not reach absolute zero!")
                
        if iternumb<=0:
                raise ValueError("Can't have zero or fewer iterations!")
        
        if iternumb != int:
                raise TypeError("Number of iterations must be an integer!") 
                
        self.temperature = temperature
    
        self.iternumb = iternumb
        
          #it would be cool to have a file (e.g energyfunctions) which contains a number of energy functions indexed by "funcitonnumber"   
   
        
    def moveparticle(self):
        from numpy.random import randint 
          #min and max particle number defined within our energy function
        particlenumb=randint(minparticlenumb -1, maxparticlenumb)
          
    def compare(energyend, energyinit):
        if energyend < energyinit:
            position=positionnew
        else: 
            p0 = exp-((energyend-energyinit)/temperature)
            p1=random.random()
            if p0>p1:
                    position=positionnew

    
  # for number in functionnumber:
   #      if type(functionnumber) !=int:
    #         raise TypeError("Function number should be an integer.")
     #    from energyfunctions import energy_"functionnumber"(density):
        
    def run(self, energy_, density):
        for number in iternumb:
        #energy obtained from "energyfunctionnumber"
            energyinit=energy(density)
            density=moveparticle
            energyend=energy(density)
            compare(energyinit, energyend)