# Problem set 1, Week 2 Problem 1
# Year payment calculator based on making only the minimum monthly payment

balance = 4213.0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
remainingBal = balance
totalPaid = 0

for month in range(1,13):
    minMonthlyPayment = round((remainingBal * monthlyPaymentRate), 2) 
    remainingBal = remainingBal - minMonthlyPayment
    remainingBal += round((remainingBal * monthlyInterestRate), 2)
    totalPaid += minMonthlyPayment
    print "Month: %d" % month
    print "Minimum monthly payment: %.2f" % round(minMonthlyPayment, 2) 
    print "Remaining balance: %.2f" % round(remainingBal, 2) 
    
print "Total paid: %.2f" % totalPaid
print "Remaining balance: %.2f" % remainingBal