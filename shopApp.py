# Set Up Shop
print("\nWelcome To My Smoothie Shop!")
print("""
1 ~ Oreo $7.99
2 ~ Banana & Strawberry $5.99
3 ~ Peanut Butter $6.99
4 ~ Blueberry $8.99
5 ~ Smore $11.99
(Enter Anything Else To Cancel)
""")
# Variables
orderSum = "Receipt: \n"
totalCost = 0
# while loop to ask for order and amount
# using correct grammar 1 smothie vs multiple smoothies
# If the amount is zero the smoothie will not be added
while True:
    order = (input("Place Your Order Here: "))

    if order == "1":
        amount = int(input("Enter The Amount You Want: "))
        if amount == 1:
            print(f"You Ordered {amount} Oreo Smoothie!\n")
        elif amount == 0:
            print("(Oreo Smoothie Order Cancelled)\n")
            continue
        else:
            print(f"You Ordered {amount} Oreo Smoothies!\n")
        orderSum += f"Oreo $7.99 * {amount}\n"
        totalCost += 7.99 * amount
    elif order == "2":
        amount = int(input("Enter The Amount You Want: "))
        if amount == 1:
            print(f"You Ordered {amount} Banana & Strawberry Smoothie!\n")
        elif amount == 0:
            print("(Banana & Strawberry Smoothie Order Cancelled)\n")
            continue
        else:
            print(f"You Ordered {amount} Banana & Strawberry Smoothies!\n")
        orderSum += f"Banana & Strawberry $5.99 * {amount}\n"
        totalCost += 5.99 * amount
    elif order == "3":
        amount = int(input("Enter The Amount You Want: "))
        if amount == 1:
            print(f"You Ordered {amount} Peanut Butter Smoothie!\n")
        elif amount == 0:
            print("(Peanut Butter Smoothie Order Cancelled)\n")
            continue
        else:
            print(f"You Ordered {amount} Peanut Butter Smoothies!\n")
        orderSum += f"Peanut Butter $6.99 * {amount}\n"
        totalCost += 6.99 * amount
    elif order == "4":
        amount = int(input("Enter The Amount You Want: "))
        if amount == 1:
            print(f"You Ordered {amount} Blueberry Smoothie!\n")
        elif amount == 0:
            print("(Blueberry Smoothie Order Cancelled)\n")
            continue
        else:
            print(f"You Ordered {amount} Blueberry Smoothies!\n")
        orderSum += f"Blueberry $8.99 * {amount}\n"
        totalCost += 8.99 * amount
    elif order == "5":
        amount = int(input("Enter The Amount You Want: "))
        if amount == 1:
            print(f"You Ordered {amount} Smore Smoothie!\n")
        elif amount == 0:
            print("(Smore Smoothie Order Cancelled)\n")
            continue
        else:
            print(f"You Ordered {amount} Smore Smoothies!\n")
        orderSum += f"Smore $11.99 * {amount}\n"
        totalCost += 11.99 * amount
    else:
        print("(You ended the Order)")
        break

# print receipt
print(f"""
{orderSum}Total Cost: ${totalCost}

Thank You For Shopping With Us!
""")
