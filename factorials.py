# n factorial functions
# functions to compute n!
# factIter(n) computes n! interatively
# factRecur(n) computes n! recursively

def factIter(n):
    '''
    n: int >= 1
    
    returns: int n!
    '''
    result = 1
    for terms in range(1,n+1):
        result *= terms
    return result
        
def factRecur(n):
    '''
    n: int >= 1
    
    returns: int n!
    '''
    if n == 1:
        return 1
    else:
        return n * factRecur(n-1)
        
print "Iteritive n! = %d" % factIter(15)
print "Recursive n! = %d" % factRecur(15)