from nose.tools import assert_true, assert_equal, assert_not_equal, assert_raises
from filefortest import MonteCarloAlgorithm
    
def testnegtemp():
    with assert_raises(ValueError) as exception: MonteCarloAlgorithm(temperature=-1)
    
def testzerotemp():
    with assert_raises(ValueError) as exception: MonteCarloAlgorithm(temperature=0)
    
def itertest():
    with assert_raises(ValueError) as exception: MonteCarloAlgorithm(iternumb=0)
    with assert_raises(ValueError) as exception: MonteCarloAlgorithm(iternumb=-1)