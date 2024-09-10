import random

print("Enter a number.")
n=input()
print("Enter a number greater than or equal to the first number.")
m=input()

while str.isdigit(n) == False or str.isdigit(m) == False or n > m:
    print("Invalid values. Please try again.")
    print("Enter a number.")
    n=input()
    print("Enter a number greater than or equal to the first number.")
    m=input()

answer=random.randint(int(n), int(m))

for i in range(0, int(n)):
    print("Guess the number between " + n + " and " + m + ". You have " + str(int(n)-int(i)) + " attempt(s) left")
    guess=int(input())
    while str.isdigit(str(answer))==False:
        print("Invalid value. Please enter a number again.")
        guess = input()
    if answer !=  guess: print("Wrong. Please try again.") 
    if answer == guess:
        print("Correct! Congraturations!")
        break
else:
    print("Sorry, you've used all your attempts. The correct number was:", answer)
