class MonteCarloAlgorithm(object):

    def __init__(self, temperature=295, iternumb=100):
    
        if temperature<0:
                raise ValueError("Work in Kelvin: no negative temperatures!")
    
        if temperature==0:
                raise ValueError("Temperature should not reach absolute zero!")
                
        self.temperature = temperature
    
        self.iternumb = iterations