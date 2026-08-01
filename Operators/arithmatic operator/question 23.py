#Take price and discount %, calculate final price.

Original_price = int(input("Enter the og price of the product :"))

Discount = float(input("Enter the discount percentage % :"))

Finale_price = Original_price*(1 - Discount / 100)

print("Finale price = ", Finale_price)