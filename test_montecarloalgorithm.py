def testnegtemp():
        with assert_raises(ValueError) as exeception: MonteCarloAlgorithm(temp=-1)