# Item ADT as per project requirements

# This class is an abstraction of items contained in bins.
# We are condensing the features of the items to create a universal description able to support to all items. 
# This makes the items more manageable.
# By creating a universal description of an item, we are generalizing the unique items.
# All the unique items can now belong to an item set, AKA the class.

# TODO remove the default args and construct in another form
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
    def getQuantity(self):
        return self.quantity
    def getBinNumber(self):
        return self.binNumber
    def isInStock(self):
        return self.inStock
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price

# This is our quicksort function. It uses recursion
def quickSort(itemList):

    # This is the base case, we can't sort a list that contains only one item so we'll send it back up the call stack
    if len(itemList) <= 1:
        return itemList
    else:
        # This will remove the right most value from the list given to the algorithm
        pivotItem = itemList.pop(len(itemList) - 1)
        # We construct two empty lists that will have items assigned to them based on value
        lesserThan = list()
        greaterThan = list()
        # This is where the sorting occurs. If the item is less than the pivot item, it goes to lesserThan than list
        for item in itemList:
            if (item.getItemNumber() < pivotItem.getItemNumber()):
                lesserThan.append(item)
        # If an item is greaterThan the value it is added to it's respective list.
            else:
                greaterThan.append(item)

        # Append [lesserThan values] + pivot value + [greaterThan values]
        # This is a recursive call to sort the "lesserThan" list prior to assigning it to the returnlist
        returnList = quickSort(lesserThan)
        # We append the pivot point to the lesserThan list
        returnList.append(pivotItem)
        # This is a recursive call to sort the "greaterThan" list and extend it to the returnList
        returnList.extend(quickSort(greaterThan))
        # Here we return the sorted list back up the call stack
        return returnList


# Driver
def main():

    bins = list()
    binNumbers = [56, 13, 25, 49, 65, 3, 53, 82, 9, 40, 31, 78, 17, 61, 47]
    for distinctNumber in binNumbers:
        bins.append(item(distinctNumber))

    sortedList = ""
    for itemBin in quickSort(bins):
        sortedList = sortedList + " " + str(itemBin.getItemNumber())

    print(sortedList)


main()
