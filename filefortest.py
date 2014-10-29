class MonteCarloAlgorithm(object):

    def __init__(self, temperature=295, iternumb=100):
    
        if temperature<0:
                raise ValueError("Work in Kelvin: no negative temperatures!")
    
    
        self.temperature = temperature
    
        self.iternumb = iterations