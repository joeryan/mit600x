# edX MIT6.00.1x programming in python
# problem set 2, week 2, problem 2
# minumum payment to pay off debt in one year

annualInterestRate = 0.2
balance = 3926.0

monthlyInterest = annualInterestRate / 12
remainingBal = balance
monthlyPmt = 10

while (remainingBal > 0):
    for month in range(1,13):
        remainingBal -= monthlyPmt
        remainingBal += monthlyInterest * remainingBal
        
    if remainingBal > 0:
        remainingBal = balance
        monthlyPmt += 10

print "Lowest Payment: %d" % monthlyPmt