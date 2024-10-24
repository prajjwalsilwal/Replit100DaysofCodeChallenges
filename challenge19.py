while True:
    print()
    print("Loan Calculator")
    print()
    principal_amt = int(input("Enter Borrowed Amount: "))
    interest_rate = int(input("Enter the interest rate: "))
    loan_time = int(input("Enter the loan time: "))

    print()
    for i in range  (0,loan_time):
        principal_amt = ((interest_rate) / 100) * principal_amt + principal_amt
        print(f"In year: {i+1}. Total Amount due is: {principal_amt}")

    print()
    user_input = input("Do you want to Continue (y/n): ")

    if user_input == "n":
        break

