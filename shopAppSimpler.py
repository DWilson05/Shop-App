# Set Up Shop
print("Welcome To My Smoothie Shop!")
print("""
1 ~ Oreo $7.99
2 ~ Banana & Strawberry $5.99
3 ~ Peanut Butter $6.99
4 ~ Blueberry $8.99
5 ~ Smore $11.99
(Enter Anything Else To Cancel Order)
""")

# Variables
orderSum = ["Receipt: "]
totalCost = 0

# while loop to ask for order
# add order to list & increase total
while True:
    order = input("Place Your Order Here: ")
    if order == "1":
        print(f"You Ordered An Oreo Smoothie!\n")
        orderSum.append("Oreo $7.99")
        totalCost += 7.99

    elif order == "2":
        print("You Ordered A Banana & Strawberry Smoothie!\n")
        orderSum.append(f"Banana & Strawberry $5.99")
        totalCost += 5.99

    elif order == "3":
        print("You Ordered A Peanut Butter Smoothie!\n")
        orderSum.append("Peanut Butter $6.99")
        totalCost += 6.99

    elif order == "4":
        print(f"You Ordered A Blueberry Smoothie!\n")
        orderSum.append("Blueberry $8.99")
        totalCost += 8.99

    elif order == "5":
        print("You Ordered A Smore Smoothie!\n")
        orderSum.append(f"Smore $11.99")
        totalCost += 11.99

    else:
        print("(You ended the Order)\n")
        break

# print receipt
for i in range(len(orderSum)):
    print(orderSum[i])
print(f"""Total Cost: {totalCost}

Thank You For Shopping With Us!
""")
