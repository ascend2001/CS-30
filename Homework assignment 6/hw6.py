
# the uniform function is used in the third problem
from random import uniform

# the pixel type is used in the sixth problem
from collections import namedtuple
pixel = namedtuple("pixel", "r g b")


def countPositives(l):
    s=0
    for x in l:
        if x>0:
            s+=1
    return s

def test_countPositives():
    assert(countPositives([1, -4, 0, 4, 8, 0])==3)
    assert(countPositives([0,0,0,-4,-4,-4,-1*-98])==1)
    assert(countPositives([3,-3,1,2,-9,3])==4)

def halveEvens(l):
    s=[]
    for x in l:
        if x%2==0:
            s=s+[x//2]
    return s

def test_halveEvens():
    assert(halveEvens([45,23,1,6,4,2,9,34,6765,23,68,32])==[3,2,1,17,34,16])
    assert(halveEvens([10,21,32,42,55])==[5,16,21])
    assert(halveEvens([-33,9,87,-6,12,-3,0])==[-3,6,0])

def piEstimate(n):
    s=0
    for z in range(1,n): 
        x=uniform(-1,1)
        y=uniform(-1,1)
        if (x**2)+(y**2)<=1:
            s+=1
    return (4*s)/n

def splitEveryOther(l):
    s=[[],[]]
    for x in list(range(0,len(l))):
        if x%2==0:
            s[0]=s[0]+[l[x]]
        else:
            s[1]=s[1]+[l[x]]
    return s

def test_splitEveryOther():
    assert(splitEveryOther([2,-3,4,1,0,-5])==[[2,4,0],[-3,1,-5]])
    assert(splitEveryOther([4,-2,1,0,5,12,1,4,2,6])==[[4,1,5,1,2],[-2,0,12,4,6]])
    assert(splitEveryOther([])==[[],[]])
    assert(splitEveryOther([1])==[[1],[]])

def dotProduct(x,y):
    s=0
    for z in list(range(0,len(x))):
        s=s+(x[z]*y[z])
    return s

def test_dotProduct():
    assert(dotProduct([1,2,3],[4,5,6])==32)
    assert(dotProduct([-2,0,1],[0,0,0])==0)
    assert(dotProduct([-3,2,-22],[-4,-1,-3])==76)

def negate(pixels): 
    q=[]
    for m in pixels:
        p=[]
        for n in m:
            n=pixel(255-n.r,255-n.g,255-n.b)
            p=p+[n]
        q=q+[p]
    return q

def test_negate():
    assert(negate([[pixel(0,255,34),pixel(255,255,255)],[pixel(0,0,0),pixel(125,200,35)]])==[[pixel(255,0,221),pixel(0,0,0)],[pixel(255,255,255),pixel(130,55,220)]])
    assert(negate([[pixel(90,45,199),pixel(56,99,134)],[pixel(45,254,98),pixel(244,0,12)]])==[[pixel(165,210,56),pixel(199,156,121)],[pixel(210,1,157),pixel(11,255,243)]])        

def toDigitList(n):
    a=str(n)
    s=[]
    for x in range(0,len(a)):
        s=s+[int(a[x])]
    return s

def test_toDigitList():
    assert(toDigitList(0)==[0])
    assert(toDigitList(1010)==[1,0,1,0])
    assert(toDigitList(231)==[2,3,1])

def digitalRootAndPersistence(n):
    s=[0,0]
    while len(str(n))!=1:
        n=sum(toDigitList(n))
        s[0]=n
        s[1]+=1
    return s

def test_digitalRootAndPersistence():
    assert(digitalRootAndPersistence(9879)==[6,2])
    assert(digitalRootAndPersistence(0)==[0,0])
    assert(digitalRootAndPersistence(2030102)==[8,1])
            
        
        
