menu = {
    'Pasta' : 40,
    'Pizza' : 50,
    'Burger' : 60,
    'Salade' : 70,
    'Coffee' : 80
}
print("Welcome to my Huzaifa Resturant")
print("Pasta: Rs40\nPizza: Rs50\nBurger: Rs60\nSalade: Rs70\nCoffee: Rs80")

order_total = 0

item_1 = input("Enter your First Item")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item has been added  in {item_1}")
else:
    print(f"{item_1} is not available")

another_item = input("Do you want second item? (Yes/No)")
if another_item == "Yes":
    item_2 = input("Please Enter Your Second Item:")
else:
    print("The Order is not  racognize")
    
if item_2 in menu:
    order_total += menu[item_2]
    print(f"Item {item_2} has been added")
else:
    print(f"you is not available {item_2}")
print(f"The Total Amount is {order_total}")
   