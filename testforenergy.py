from diffusion_model import energy
def test_energy1():
    
    from nose.tools import assert_equal

    assert_equal(energy([1.0,1.0], 2.0), 0)
    
def test_energy2():
    
    from nose.tools import assert_not_equal

    assert_not_equal(energy([1.0,1.0], 2.0), 2)
    
def test_energyneg():