# edx MIT 6.00.1x week 2, set 2, problem 3
# more accurate minimum payment to pay off debt in a year

annualInterestRate = 0.2
balance = 320000

monthlyInterest = annualInterestRate / 12
monthlyPmtLower = balance / 12
monthlyPmtUpper = (balance * (1+monthlyInterest)**12)/12
MAXITER = 20
iterNum = 1
midpoint = (monthlyPmtLower + monthlyPmtUpper)/2
print midpoint

def payoff(monthPmt, bal, monthInt):
    for month in range(1,13):
        bal = bal - monthPmt
        bal += round((bal * monthInt), 2)
    return bal
    
while (iterNum < MAXITER):
    yearEndBal = payoff(midpoint, balance, monthlyInterest)
    print "Year end bal: %f" % yearEndBal
    if  yearEndBal <= 0.0 and yearEndBal >= -0.01:
        break
    else:
        iterNum += 1
        if yearEndBal > 0:
            montlyPmtLower = midpoint
        else:
            monthlyPmtUpper = midpoint
    midpoint = (monthlyPmtLower + monthlyPmtUpper)/2
    print midpoint

print "Lowest payment: %.2f" % midpoint
