#Item ADT as per project requirements

# This class is an abstraction of item contained in a bins. This is because we are stripping away features of
# items in order to make a description of the item more managable to meet our end goal in a reasonable amount of time.
# Additionally, this is a generalization of items also. We are generalizing such that all of the unique items in the
# bins are just an item. Granted we have a name attribute, but it's still just an item.

#TODO remove the defualt args and actually
class item:
    def __init__(self, itemNumber, quantity = 20, binNumber = 16, inStock = True, name = 'item', price = 1.25):
        self.itemNumber = itemNumber
        self.quantity = quantity
        self.binNumber = binNumber
        self.inStock = inStock
        self.name = name
        self.price = price


#Data representation?
#TODO This constructor loop will use default values to build out the list so we can start testing the algorithm
binNumbers = (56, 13, 25, 49, 65, 3, 53, 82, 9, 40, 31, 78, 17, 61, 47)
bins = list()
for distinctNumber in binNumbers:
    bins.append(item(distinctNumber))

for item in bins:
    print("Item Number: " + str(item.itemNumber))
    print("Item in stock: " + str(item.inStock))
    print("Bin Number: " + str(item.binNumber))
    print("Quantity: " + str(item.quantity))
    print("Item Name: " + str(item.name))
    print("\n---------------------\n")



