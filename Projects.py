                                      #Q Static Guess gaame
print("Welcome to the Guessing Game")
win_no=6
attempt=1
chancess=5
for i in range(6):
    print("chances remaining= ",chancess)
    N=int(input("Guess the number between 1 and 10 ="))
    if N==6:
        print("Congrats!!, you guessed the rignt number")
        print(f"You took {attempt} attempts to win ")
        break
    elif N<6:
        print("You guess is low")
    elif N>=6:
        print("Your guess is  high")
    chancess=chancess-1
    attempt=attempt+1
if chancess==0:
    print(" Sorry you exceeded your guessing limits")




