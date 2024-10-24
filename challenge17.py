while True:
    print("Rock(R) Paper(P) Scissors(S)")

    round_count = 1
    player1_win = 0
    player2_win = 0

    while player1_win < 4 and player2_win < 3:
        print(f"Rock Paper Scissor -  Round: {round_count} ")
        player1_hand = input("Enter your move Player 1: ")
        player2_hand = input("Enter your move Player 2: ")
        player2_hand = player2_hand.upper()
        player1_hand = player1_hand.upper()

        if player1_hand == "R":
            if player2_hand == "R":
                print("Tie.")
                round_count+=1
            elif player2_hand == "P":
                print("Player 2 Wins")
                player2_win += 1
                round_count += 1

            elif player2_hand == "S":
                print("Player 1 Wins")
                player1_win +=1
                round_count += 1

            else:
                print("Invalid Entry")
                continue

        elif player1_hand == "S":
            if player2_hand == "S":
                print("Tie.")
                round_count += 1
            elif player2_hand == "R":
                print("Player 2 Wins")
                player2_win += 1
                round_count += 1

            elif player2_hand == "P":
                print("Player 1 Wins")
                player1_win += 1
                round_count += 1

            else:
                print("Invalid Entry")
                continue

        elif player1_hand == "P":
            if player2_hand == "P":
                print("Tie.")
                round_count += 1
            elif player2_hand == "S":
                print("Player 2 Wins")
                player2_win += 1
                round_count += 1

            elif player2_hand == "R":
                print("Player 1 Wins")
                player1_win += 1
                round_count += 1

            else:
                print("Invalid Entry")
                continue


        else:
            print("Invalid Entry")
            continue

        print( "Next Round.")

    if player1_win > player2_win:
        print(f"The winner is Player 1. The Score is - Player 1 : {player1_win} -- Player 2: {player2_win} ")
    else:
        print(f"The winner is Player 2. The Score is - Player 2 : {player2_win} -- Player 1: {player1_win} ")

    print("The game has Ended")
    user_input = input("Do you want to Continue (y/n): ")
    if user_input == "n":
        break

