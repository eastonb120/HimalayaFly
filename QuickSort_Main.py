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

    def getItemNumber(self):
        return self.itemNumber


#Data representation?
#TODO This constructor loop will use default values to build out the list so we can start testing the algorithm
binNumbers = [56, 13, 25, 49, 65, 3, 53, 82, 9, 40, 31, 78, 17, 61, 47]
bins = list()
for distinctNumber in binNumbers:
    bins.append(item(distinctNumber))

# for item in bins:
#     print("Item Number: " + str(item.itemNumber))
#     print("Item in stock: " + str(item.inStock))
#     print("Bin Number: " + str(item.binNumber))
#     print("Quantity: " + str(item.quantity))
#     print("Item Name: " + str(item.name))
#     print("\n---------------------\n")



# pivotItem = bins.pop(len(bins) - 1)
# lesser = list()
# greater = list()
# for item in bins:
#     if(item.getItemNumber() < pivotItem.getItemNumber()):
#         lesser.append(item)
#     else:
#         greater.append(item)
#
# lesserString = ""
# for item in lesser:
#     lesserString = lesserString + str(item.getItemNumber()) + ", "
# print(lesserString)


def quickSort(itemList):

    if len(itemList) == 1:
        return list(itemList)
    else:
        print("Length before pivot pop: " + str(len(itemList)))
        pivotItem = itemList.pop(len(itemList) - 1)
        print("pivotItem post pop: " + str(vars(pivotItem)))
        print("Pivot value: " + str(pivotItem.getItemNumber()))
        lesser = list()
        greater = list()
        print("Length after pivot pop: " + str(len(itemList)))
        for item in itemList:
            if (item.getItemNumber() < pivotItem.getItemNumber()):
                print("Lesser: " + str(item.getItemNumber()))
                lesser.append(item)
            else:
                print("Greater: " + str(item.getItemNumber()))
                greater.append(item)


        print("pivotItem post sort: " + str(vars(pivotItem)))

        print("Lesser List Length: " + str(len(lesser)))
        print("Greater List Length: " + str(len(greater)))
        returnListL = quickSort(lesser)
        print("Length after return lesser: " + str(len(returnListL)))
        returnListP = returnListL.append(pivotItem)
        print("Length after return pivotItem: " + str(len(returnListP)))
        returnList = returnListP.extend(quickSort(greater))
        return returnList



sortedList = ""
for item in quickSort(bins):
    sortedList = sortedList + ", " + str(item.getItemNumber())

print(sortedList)

