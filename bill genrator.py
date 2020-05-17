sum = 0

while(True):
    userInput = input("Enter the item price and press Q to quite : \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order Total so far : {sum}")

    else:
        print(f"Your Total bill is {sum}. Thanks For shopping with us.")
        break

# ---------------------------Note-----------------------------------------
print("\nFor learn how to run and access bill_genrator , open this file in your editor and learn about this file")
print("\nThank You\n")