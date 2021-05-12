                                                                          #Assignment 1 (python problem set 1)
                                                                          #Name: Avnish Sengupta
# we use the isclose function from the math library to test your functions.
# see the "test" functions below for examples.
from math import isclose

def arithMean(x,y,z):
    '''Compute the arithmetic mean of three numbers.'''
    return ((x+y+z)/3)

def test_arithMean():
    # add more tests!  consider 'corner cases' like 0, negative numbers, etc.
    assert isclose(arithMean(3,3,3),3)
    assert isclose(arithMean(3.1, 3.3, 3.5),3.3)
    assert isclose(arithMean(-1, 2, -16),-5 )
    assert isclose(arithMean(0,24,78),34)


def geoMean(x,y,z):
    '''Compute the geometric mean of three numbers.'''
    return ((x*y*z)**(1/3))

def test_geoMean():
    # add more tests!
    assert isclose(geoMean(2, 4, 8),4)
    assert isclose(geoMean(0, 1, 2),0)

def variance(x,y,z):
    '''Compute the variance of three numbers.'''
    a=(x- arithMean(x,y,z))**2
    b=(y- arithMean(x,y,z))**2
    c=(z- arithMean(x,y,z))**2
    d= arithMean(a,b,c)
    return d

def test_variance():
    # add more tests!
    assert isclose(variance(3, 4, 5),2/3)
    assert isclose(variance(-1, -2, -3),2/3) 
    assert isclose(variance(56, 80, 98),296)
    assert isclose(variance(-13, 0, 67),1228.6666666666667)

def stdDev(x,y,z):
    '''Compute the standard deviation of three numbers.'''
    e= (variance(x,y,z))**(1/2)
    return e

def test_stdDev():
    # add more tests!
    assert isclose(stdDev(3, 4, 5),0.816496580927726)
    assert isclose(stdDev(-13, 0, 67),35.05234181430203)
    assert isclose(stdDev(56, 80, 98),17.20465053)
    assert isclose(stdDev(-1, -2, -3),0.816496580927726)
        
