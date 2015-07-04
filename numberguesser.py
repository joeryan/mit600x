# Number guessing game.  Computer will guess the number you are thinking of
# use h to indicate too high
# use l to indicate too low and 
# use c to indicate the computer guessed correctly

print "Please think of a number between 0 and 100!"


highnum = 100
lownum = 0
guess = (hignum + lownum) / 2
guess_text = "Enter 'h' to indicate the the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
print "Is your secret number %d?" % guess
answer = raw_input(guess_text)
while (answer != 'c'):
    if answer == 'h':
        highnum = guess
    elif answer == 'l':
        lownum = guess 
    else:
        answer = raw_input(guess_text)
        next
    
    guess = (highnum + lownum)/2
    print "Is your secret number %d?" % guess
    answer = raw_input(guess_text)
    
print "Game over. Your secret number was: %d" % guess