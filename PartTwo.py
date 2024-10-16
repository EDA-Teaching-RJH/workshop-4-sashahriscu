# define principal function
def main():
    # set accepted coins
    accepted_coins = [5, 10, 20, 50]
    # set coffee price
    coffee_price = 75
    # set default amount of coins inserted
    total_inserted = 0

    # user asked to insert coins until the total inserted covers the coffee price
    while total_inserted < coffee_price:
        remaining_amount = coffee_price - total_inserted
        print(f"Remaining amount: {remaining_amount}p")
        coin = int(input("Insert coins (machine only accepts 5p, 10p, 20p, 50p): "))
        
        # validate inserted coin
        if coin in accepted_coins:
            total_inserted += coin
        else: # invalidated coins not accpeted
            print("Only 5p, 10p, 20p, or 50p coins accepted. Please try with the accepted coins.")

    # calculate change
    if total_inserted > coffee_price:
        change = total_inserted - coffee_price
        print(f"Your change is {change}p")
    else:  # if amount is fulfilled
        print("Thank you ! Your coffee will be ready shortly.")

# define principal function
main()

