# getting three inputs from the user
balance = int(input("enter the balance in the beginning of the month: "))
withdraw = int(input("enter total withdrawals in the month: "))
deposit = int(input("enter total deposits in the month: "))

# calculate the new balance
new_balance = balance - withdraw + deposit
tax = (withdraw + deposit) * (1/100)
new_balance -= tax

# printing out the new balance
print(f"Balance: {new_balance}")