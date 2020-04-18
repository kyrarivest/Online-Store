"""Kyra Rivest
Python period 2
Mr. Rossetti
Online Store Project"""

"""10/26/18 This function executes the add option in the main menu
and when the program runs for the first time"""
def add():
    on = True
    while(on):
        print("\n***Adding Item to the Store***")
        name = input("Enter an item name: ")
        price = input("Enter the price of item: ")
        inventory = input("Enter the initial inventory: ")
        name_number.append(name)
        name_inventory[name] = inventory
        name_price[name] = price

        while True:
            answer = input("\nItem added to the store. Would you like to add another item (Y/N)?").upper()
            if (answer[0] == "Y"):
                print("")
                break
            elif (answer[0] == "N"):
                on = False
                break
            else:
                print("Not valid answer")
                
    
"""10/29/18 This functon exectues the inventory option in
the main menu and is used in the stock option"""
def inventory():
    for item in name_number:
        item_number = int(name_number.index(item)) + 1
        print("item #%00d %s $%s Qty: %s"
              %(item_number, item, name_price[item], name_inventory[item]))


"""10/31/18 This function executes the purchase option in the main menu"""
def purchase():
    total = 0
    on = True
    while(on):
        third_test = True
        
        print("\n***Items for Sale***")
        for item in name_number:
            item_number = int(name_number.index(item)) + 1
            print("item #%00d %s $%s"
                  %(item_number, item, name_price[item]))
            
        
        while True:
            item = int(input("\nPlease enter the number of the item you wish to purchase: ")) -1
            if (item >= 0) and (item <= len(name_number) -1):
                break 
            else:
                print("Sorry, invalid item number")

        
        while True:
            if (int(name_inventory[name_number[item]]) == 0):
                print("Sorry, that item is not in stock")
                third_test = False
                break
            else:
                break
            
        while(third_test):
            number = int(input("Enter the quantity: "))
            if (number <= int(name_inventory[name_number[item]])):
                total += (float(name_price[name_number[item]]) * number)
                name_inventory[name_number[item]] = int(name_inventory[name_number[item]]) - number
                print("%0d items added to your shopping cart" %(number))
                break
            else:
                print("Sorry, we only have %s in stock" %(name_inventory[name_number[item]]))
                break


        while True:
            answer = input("\nWould you like to continue shopping?(Y/N)").upper()
            if (answer[0] == "N"):
                print("\n****Checkout***")
                print("Your shopping cart totals $%.2f" %(total))
                print("Thank you for your purchase")
                on = False
                break
            elif (answer[0] == "Y"):
                print("")
                break
            else:
                print("Not a valid answer")
                
        
"""10/31/18 This function executes the modify option under the stock option in the main menu"""
def modify():
    on = True
    while(on):
        print("\n***Modifying item***")
        item = int(input("Please enter the number of the item you wish to modify: ")) -1
        if (item >= 0) and (item <= len(name_number) -1):
            print("item #%00d %s $%s Qty: %s"
              %(item + 1, name_number[item], name_price[name_number[item]], name_inventory[name_number[item]]))
            price = input("Enter the new price: ")
            quantity = input("Enter new quantity: ")
            name_price[name_number[item]] = price
            name_inventory[name_number[item]] = quantity
            print("Item has been updated")
            
        else:
            print("Invalid item number")
            
        
        while True:
            answer = input("\nWould you like to modify another item (Y/N)?").upper()
            if (answer[0] == "Y"):
                print("")
                break
            elif (answer[0] == "N"):
                on = False
                break
            else:
                print("Not valid answer")
    


    
"""Main body of code. Executes as long as (Q)uit is not selected"""
import json
print("Welcome to the ASD Python Store! \n ")

try:
    file = open("OnlineStoreData.json","r")
except FileNotFoundError:
    name_number = []
    name_inventory = {}
    name_price = {}
    
    print("Store not found! Please ass items to the store.")
    add()
else:
    data = json.load(file)
    name_number = data[0]
    name_inventory = data[1]
    name_price = data[2]
    file.close()
    print("Store information has loaded!")

on = True
while(on):
    i = input("\n(P)urchase, (S)tock, (I)nventory, or (Q)uit: ").upper()

    if (i[0] == "P"):
        purchase()  

    elif (i[0] == "S"):
        print("\n*** Online Store Inventory Report ***")
        inventory()
        
        while True:
            y = input("\nWould you like to (A)dd a new item or (M)odify an existing item?").upper()
            if (y[0] == "A"):
                add()
                break
            elif(y[0] == "M"):
                modify()
                break
            else:
                print("Not a valid entry, please try again \n")
           
    elif (i[0] == "I"):
        print("\n***Online Inventory Report***")
        inventory()
  
    elif (i== "Q"):
        on = False
    else:
        print("\n Not a valid input \n")
    
else:
    """When (Q)uit is selected, data is saved into json file and program is closed"""
    store_data = [name_number,name_inventory,name_price]
    file = open("OnlineStoreData.json","w")
    json.dump(store_data, file)
    file.close()
    print("\n Thanks for visiting the Python Store \n Saving data. \nExiting...goodbye!")
       
