# towers of Hanoi problem
# demonstrate more complicated recursion problem

def printMove(fr, to):
    print ("move from " +str(fr) + " to " + str(to))
    
def towers(n, fr, to, spare):
    '''
    n: int > 0 for size of plate stack
    fr: designates tower plates are moved from
    to: designates tower plates are moved to
    spare: designates the spare stack
    '''
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)
        

towers(3, "Center", "Left", "Right")
