x =int(input("Enter multiples: "))

counter = 0
for i in range (1,11):
    correct = i * x
    user_guess = int(input(f"{i} x {x} = "))
    if user_guess == correct:
        print("Nice")
        counter+=1
    else:
        print(f"No. It is: {correct} ")

print("Your score is: ", counter)