#Name: Avnish Sengupta
#Discussion: 1A

from turtle import forward, left
def intRange(low,high):
    if low>high:
        return []
    elif low==high:
        return [low]
    else:
        l=[low]
        k=[high]
        return l+intRange(low+1,high-1)+k

def test_intRange():
    assert(intRange(2,5)==[2,3,4,5])
    assert(intRange(-30,-28)== [-30,-29,-28])
    assert(intRange(20,4)== [])
    assert(intRange(-2,2)==[-2,-1,0,1,2])
    assert(intRange(1,2)==[1,2])
    assert(intRange(1,4)==[1,2,3,4])
    

def positiveRanges(l):
    if l==[]:
        return []
    else:
        e=l[0]
        tail=l[1:]
        a=intRange(1,e)
        return [a]+ positiveRanges(tail)

def test_positiveRanges():
    assert(positiveRanges([2, 5, 0, 1])==[[1,2], [1,2,3,4,5], [], [1]])
    assert(positiveRanges([-3,-4,0,4])==[[],[],[],[1,2,3,4]])
    assert(positiveRanges([1,1,1,2])==[[1],[1],[1],[1,2]])
    assert(positiveRanges([3])==[[1,2,3]])
    assert(positiveRanges([])==[])

def threshold(l,n):
    if l==[]:
        return []
    else:
        head=l[0]
        tail=l[1:]
        if head>=n:
            return [head]+threshold(tail,n)
        else:
            return threshold(tail,n)
        
def test_threshold():
    assert(threshold([1, -4, 0, 4, 8, -3], 1)==[1,4,8])
    assert(threshold([2],2)==[2])
    assert(threshold([2,3],3)==[3])
    assert(threshold([3,4,5],6)==[])
    assert(threshold([-2,-3,-12],-4)==[-2,-3])
    assert(threshold([-2],-2)==[-2])
    
def insert(n,l):
    if l==[]:
        return [n]
    else:
        head=l[0]
        tail=l[1:]
        if n>head:
            return [head]+ insert(n,tail)
        else:
            head=l[0:len(l)-1]
            tail=l[len(l)-1]
            return insert(n,head)+[tail]

def test_insert():
    assert(insert(-4,[-6,-4,0,3,5,7,9])==[-6,-4,-4,0,3,5,7,9])
    assert(insert(0,[0,0,0,0])==[0,0,0,0,0])
    assert(insert(-3,[0,3,4,5,6])==[-3,0,3,4,5,6])
    assert(insert(9,[-1,2,4,5,6])==[-1,2,4,5,6,9])

def insertionSort(l):
    if l==[]:
        return []
    else:
        head=l[0]
        tail=l[1:]
        return insert(head,insertionSort(tail))
    
def test_insertionSort():
    assert(insertionSort([3,6,2,8,1,7,-3,-1,-34])==[-34,-3,-1,1,2,3,6,7,8])
    assert(insertionSort([-3,0,4,1,6,2,9])==[-3,0,1,2,4,6,9])
    
def archSpiral(length,increment,angle,n):
    if n==0:
        return
    else:
        newLength=length+increment
        forward(length)
        left(angle)
        forward(newLength)
        left(angle)
        archSpiral(newLength,increment,angle,n-1)


def logSpiral(length,percentIncrease,angle,n):
    if n==0:
        return
    else:
        newLength=length+(length*(percentIncrease/100))
        forward(length)
        left(angle)
        forward(newLength)
        left(angle)
        logSpiral(newLength,percentIncrease,angle,n-1)

            
        


