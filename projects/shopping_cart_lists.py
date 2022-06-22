entered_product = ""
cart = []

while entered_product != "done":
    entered_product = input("please enter an item(SKU, description, unit price, quantity) or done. ")
    print(entered_product)
    cart.append(entered_product.split(","))
    list(entered_product)
print("shopping complete")
cart.pop()
#print(cart)

#subtotal
subtotal = 0
for item in cart:
    print(item)
    item_cost = int(item[2]) * int(item[3])
    subtotal = subtotal + item_cost
print("Your subtotal is $" + str(subtotal)) 

#coupon
import random
num = range(10, 35, 5)
percent_off = random.choice(num)
coupon = random.choice(num) / 100
print(str(percent_off) + "%")
new_total = subtotal - coupon * subtotal 
print("Congratulations, you have received a " + str(percent_off) + "% discount and your new total is now $" + str(new_total))

#sales tax
import random
num_2 = range(6, 125, 1)
sales_tax = float(random.choice(num_2))/ 10
print(str(sales_tax) + "%")
final_total = new_total + new_total * (sales_tax / 100)
print("Your sales tax today is " + str(sales_tax) + "% which makes your final total $" + str(round(final_total, 2)))