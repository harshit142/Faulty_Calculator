# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 26
no_of_guesses = 1
print("no of guesses is limited to only 10 times: ")
while (no_of_guesses <=10):
    guess_number = int(input("Guess the no.: "))
    if (guess_number >26):
        print("Enter the smaller  no.: ")
    elif (guess_number <26):
        print("Enter the  greater no.: ")
    else:
        print("you won\n")
        print(no_of_guesses ,"no. of guesses took to finish")
        break
    print(10 - no_of_guesses , "no. of guesses left")
    no_of_guesses  = no_of_guesses  + 1

if (no_of_guesses >10):
    print("Game Over")