my_num = 18563
my_num_length = len(str(my_num))

attempt_count = 0

while True:
    user_guess = input("Enter your guess. For I have chosen a number: ")

    if len(user_guess) < my_num_length:
        print("You are very low.")
        attempt_count += 1

    elif len(user_guess) > my_num_length:
        print("You are very high.")
        attempt_count += 1

    else:
        if int(user_guess) == my_num:
            print("Correct.")
            attempt_count += 1
            break

        elif int(user_guess) < my_num:
            print("Low but you are getting there.")
            attempt_count += 1

        else:
            print("High. You gotta lower it a bit.")
            attempt_count += 1

print(f"It took you {attempt_count} attempts.")


