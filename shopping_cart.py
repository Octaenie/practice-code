item = str(input("What item would you like to buy?: "))
price = float(input("What is the price for that item?: "))
quantity = int(input("How many of those items would you like?: "))

print(f"Your order is {quantity} {item}/s")
print("Your total for this order is: ", price*quantity)