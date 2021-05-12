# Follow the rules in hw4.html very carefully!
#Homework Assignment 4
#Name: Avnish Sengupta

def positiveRanges(l):
    return list(map(lambda n:list(range(1,n+1)), l))

def test_positiveRanges():
    assert(positiveRanges([2, 5, 0, 1])==[[1,2], [1,2,3,4,5], [], [1]])
    assert(positiveRanges([-3,-1,0,2,4])==[[],[],[],[1,2],[1,2,3,4]])
    assert(positiveRanges([-3,-3,-3,0,2,2,1])==[[],[],[],[],[1,2],[1,2],[1]])
    assert(positiveRanges([7,3,5,2,9,1,-6])==[[1,2,3,4,5,6,7],[1,2,3],[1,2,3,4,5],[1,2],[1,2,3,4,5,6,7,8,9],[1],[]])

def threshold(l,x):
    return list(filter(lambda n:n>=x, l))

def test_threshold():
    assert(threshold([-3,5,3,-6,5,1,-7,25],5)==[5,5,25])
    assert(threshold([4,6,1,2,3,98,21,54,3,67],4)==[4,6,98,21,54,67])
    assert(threshold([-3,-1,7,3,-5,0,6],-1)==[-1,7,3,0,6])
    assert(threshold([-3,1,-9,4,-2,-4,-1],-2)==[1,4,-2,-1])

def halveEvens(l):
    a=list(filter(lambda m: m if m%2==0 else [], l))
    if 0 in l:
        a=a+[0]
    else:
        a=a
    return list(map(lambda n: n//2, a))
    
def test_halveEvens():
    assert(halveEvens([24,1,5,0,-3,11])==[12,0])
    assert(halveEvens([3])==[])
    assert(halveEvens([1,34,-2,19,-3,-6])==[17,-1,-3])
    assert(halveEvens([10,13,9,1,24,31])==[5,12])
    assert(halveEvens([-3,12,-31,12,9,98])==[6,6,49])

def highValueAccounts(l):
    return list(filter(lambda n: n if (n[0]+n[1])>=1000000 else [],l))

def test_highValueAccounts():
    assert(highValueAccounts([[100000,400000], [400000, 700000], [2, 20000000], [2, 20000]])==[[400000, 700000], [2, 20000000]])
    assert(highValueAccounts([[-34,-32324221],[23212321,0],[0,3224532235],[-321,1234343234]])==[[23212321,0],[0,3224532235],[-321,1234343234]])
    assert(highValueAccounts([[0,0],[999999,1],[1000000,-2],[500000,500000]])==[[999999,1],[500000,500000]])

def addMonthlyInterest(l):
    return list(map(lambda n: [n[0],(n[1]+0.02*n[1])] if n[1]>=250 else n,l))

def test_addMonthlyInterest():
    assert(addMonthlyInterest([[1000, 20], [20, 1000], [500, 500]])==[[1000, 20], [20, 1020.0], [500, 510.0]])
    assert(addMonthlyInterest([[543,250],[250,-250],[0,249],[249,0],[90,251],[260,91]])==[[543,255],[250,-250],[0,249],[249,0],[90,256.02],[260,91]])
    

def convertCS31Accounts(l):
    return list(map(lambda n:[n[1],n[0]],l))

def test_convertCS31Accounts():
    assert(convertCS31Accounts([[300, 200], [0, 400], [250, 250]])==[[200, 300], [400, 0], [250, 250]])
    assert(convertCS31Accounts([[0,0],[-370,-73],[-343,21],[999,-890],[123,0],[0,321],[-234,0],[0,-989]])==[[0,0],[-73,-370],[21,-343],[-890,999],[0,123],[321,0],[0,-234],[-989,0]])
    


