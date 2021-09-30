#Item ADT as per project requirements

# This class is an abstraction of item contained in a bins. This is because we are stripping away features of
# items in order to make a description of the item more manageable to meet our end goal in a reasonable amount of time.
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

def quickSort(itemList):

    #This is the base case, we can't sort a list that contains only one item so we'll send it back up the call stack
    if len(itemList) == 1:
        return itemList
    else:
        #This will remove the right most value from the list given to the algorithm
        pivotItem = itemList.pop(len(itemList) - 1)
        #We construct two empty lists that will have items assigned to them based on value
        lesserThan = list()
        greaterThan = list()
        #This is where the sorting occurs. If the item is less than the pivot item, it goes to lesserThan than list
        for item in itemList:
            if (item.getItemNumber() < pivotItem.getItemNumber()):
                lesserThan.append(item)
        #If an item is greaterThan the value it is added to it's respective list.
            else:
                greaterThan.append(item)

        #Append [lesserThan values] + pivot value + [greaterThan values]
        #This is a recursive call to sort the "lesserThan" list prior to assigning it to the returnlist
        returnList = quickSort(lesserThan)
        #We append the pivot point to the lesserThan list
        returnList.append(pivotItem)
        #This is a recursive call to sort the "greaterThan" list and extend it to the returnList
        returnList.extend(quickSort(greaterThan))
        #Here we return the sorted list back up the call stack
        return returnList



sortedList = ""
for item in quickSort(bins):
    sortedList = sortedList + " " + str(item.getItemNumber())

print(sortedList)

