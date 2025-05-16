cost_price = float(input("Enter the cost of your item: "))
selling_price = float(input("Enter the selling price of your item:"))
if selling_price > cost_price:
   profit = selling_price - cost_price
   print("Your profit is:",profit)

else:
   loss = cost_price - selling_price
   print("You've lost" ,loss)
