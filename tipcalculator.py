print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want:S,M or L?")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
add_pepperoni = input("Do you want to add pepperoni:Y or N?")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
cheese = input("Do you want extra cheese?Y or N? ")
if cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")

