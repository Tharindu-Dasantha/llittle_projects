# getting the inputs
name = input("What is the name of the salesperson: ").strip()
number = input("What is the number of the salesperson: ").strip()
while True:
    try:
        weekly_sales = int(input("Weekly sales: "))
        break
    except ValueError:
        print("Value should be a number")
        pass

# Calculating the payments
pay = 300
commission = weekly_sales * (10 / 100)
pay += commission 

# outputting the payments
print(f"Mr/Miss {name}({number}) has recived a payment of {pay}")