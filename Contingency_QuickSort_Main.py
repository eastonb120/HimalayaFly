import csv
import os.path as os


# Item ADT as per project requirements

# This class is an abstraction of items contained in bins.
# We are condensing the features of the items to create a universal description able to support to all items. 
# This makes the items more manageable.
# By creating a universal description of an item, we are generalizing the unique items.
# All the unique items can now belong to an item set, AKA the class.

# abstracted item ADT
class item:
    def __init__(self, itemNumber, quantity=20, binNumber=16, inStock='1', name='item', price=1.25):
        # Double underscore indicates that the attribute is private
        self.__itemNumber = itemNumber
        self.__quantity = quantity
        self.__binNumber = binNumber
        self.__inStock = inStock
        self.__name = name
        self.__price = price

    # Override str(instantiatedObjName) to print a string to conveniently write to CSV file
    def __str__(self):
        return str(self.itemNumber) + "," + str(self.quantity) + "," + str(self.binNumber) + ",\"" + str(self.inStock) \
               + "\",\"" + self.name + "\"," + str(self.price)

    # class attribute methods for __itemNumber
    @property
    def itemNumber(self):
        return self.__itemNumber

    @itemNumber.setter
    def itemNumber(self, itemNumber):
        self.__itemNumber = itemNumber

    def getItemNumber(self):
        return self.itemNumber

    def setItemNumber(self, itemNumber):
        self.itemNumber = itemNumber

    # class attribute methods for __quantity
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    # class attribute methods for __binNumber
    @property
    def binNumber(self):
        return self.__binNumber

    @binNumber.setter
    def binNumber(self, binNumber):
        self.__binNumber = binNumber

    def getBinNumber(self):
        return self.binNumber

    def setBinNumber(self, quantity):
        self.binNumber = quantity

    # class attribute methods for __inStock
    @property
    def inStock(self):
        return self.__inStock

    @inStock.setter
    def inStock(self, inStock):
        self.__inStock = inStock

    def isInStock(self):
        return self.inStock

    def setIsInStock(self, inStock):
        self.inStock = inStock

    # class attribute methods for __getName
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    # class attribute methods for __price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price


class FileExists(Exception):
    pass


# This is our quicksort function. It uses recursion.
# INPUT: list of items
# OUTPUT: sorted list of items
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
            if (item.getItemNumber() <= pivotItem.getItemNumber()):
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

# This creates an item list from a csv file
# INPUT: file name
# OUTPUT: list of items
def CSVitemImporter(fileName):
    # list to hold our item objects
    itemList = list()

    try: 
        # open a file to read
        csv_file = open(fileName, mode='r')
        # DictReader uses first row, which contains headers here, to refer to columns in csv
        csv_reader = csv.DictReader(csv_file)
        # headers in csv have not been read yet
        readHeader = False
        # the csv file is read row by row; after the header, items are created and added to the list
        for row in csv_reader:
            if readHeader == False:
                pass
                readHeader = True
            else:
                # adds an item created from a row in the csv to the list
                itemList.append(item(int(row["item_number"]), int(row["quantity"]), int(row["bin_num"]), row["in_stock"]
                                     , row["name"], float(row["price"])))
    except IOError:
        print("File Not Located or Locked by Another Application")

    return itemList

# This creates an output csv file
# INPUT: list of items, string for csv headers, file name
# OUTPUT: none
def CSVitemWriter(itemList, CSVheaderString, fileName, printOutputToConsole = True):
    if os.exists(fileName):
        raise FileExists("File already exists.")
    else:
        # open a file to write in
        fileObject = open(fileName, "w")
        # prints the headers for the output csv file
        if printOutputToConsole:
            print(CSVheaderString)
        # writes the headers for the output csv file in the file
        fileObject.write(CSVheaderString + "\n")
        # cycles through items in item list and writes the items to separate lines in csv
        for itemObj in itemList:
            if printOutputToConsole:
                print(str(itemObj))
            fileObject.write(str(itemObj) + "\n")
        # closes csv file
        fileObject.close()


# Driver
def main():
    inputFile = "InventoryManifest.csv"
    outputFile = "InventoryManifest_Output.csv"
    CSVheadString = '"item_number","quantity","bin_num","in_stock","name","price"'
    CSVitemWriter(quickSort(CSVitemImporter(inputFile)), CSVheadString, outputFile)

main()
