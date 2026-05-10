# stock prices (fixed)
prices = {
    "aapl": 180,
    "tsla": 250
}

# user input
stock = input("Enter stock name: ")
qty = int(input("Enter quantity: "))

# calculation
total = prices[stock] * qty
print("Total Investment:", total)
