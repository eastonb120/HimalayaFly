import csv
######################################################################################################
## QuickSort Item ADT
## Date: 10/3/2021
## Version 1.0
## Author: Easton Birdsong and Jessica Oh
## Arguments: No Command Line Args
##
######################################################################################################


# Item ADT as per project requirements

# This class is an abstraction of items contained in bins.
# We are condensing the features of the items to create a universal description able to support to all items. 
# This makes the items more manageable.
# By creating a universal description of an item, we are generalizing the unique items.
# All the unique items can now belong to an item set, AKA the class.

# abstracted item ADT
######################################################################################################
## Class: item
## Purpose: ADT acts as an abstraction of items in a store.
######################################################################################################

class item:

    ######################################################################################################
    ## Function: __init__
    ## Purpose: Constructor of the item class
    ## Arguments: itemNumber - Manufacturer Item Number
    ##            quatity - Quantity of Items
    ##            binNumber - The bin in which the item resides
    ##            inStock - Are there any items in inventory
    ##            name - Item name
    ##            price - The price of the item.
    ##
    ## Returns: Instantiated item object.
    ######################################################################################################

    def __init__(self, itemNumber, quantity, binNumber, inStock, name, price):
        # Double underscore indicates that the attribute is private
        self.__itemNumber = itemNumber
        self.__quantity = quantity
        self.__binNumber = binNumber
        self.__inStock = inStock
        self.__name = name
        self.__price = price

    ######################################################################################################
    ## Function: __str__
    ## Purpose: Overloads the str output of item object when called by str(itemObj)
    ##
    ## Returns: A string of all object attributes formatted in CSV style.
    ######################################################################################################
    def __str__(self):
        return str(self.itemNumber) + "," + str(self.quantity) + "," + str(self.binNumber) + ",\"" + str(self.inStock) \
               + "\",\"" + self.name + "\"," + str(self.price)

    ######################################################################################################
    ## Function: itemNumber
    ## Purpose: This is a getter for the private attribute __itemNumber whenever itemObj.itemNumber
    ##          is called this function is ran.
    ##
    ## Returns: The value of __itemNumber
    ######################################################################################################
    @property
    def itemNumber(self):
        return self.__itemNumber

    ######################################################################################################
    ## Function: itemNumber
    ## Purpose: This is a setter for the private attribute __itemNumber whenever itemObj.itemNumber
    ##          is being assigned a value, this function is called.
    ##
    ## Returns: Nothing
    ######################################################################################################

    @itemNumber.setter
    def itemNumber(self, itemNumber):
        self.__itemNumber = itemNumber

    ######################################################################################################
    ## Function: getItemNumber
    ## Purpose: This is the getter for itemNumber after instantiation.
    ## Returns: The value of itemNumber
    ######################################################################################################

    def getItemNumber(self):
        return self.itemNumber

    ######################################################################################################
    ## Function: gsetItemNumber
    ## Purpose: This is the setter for itemNumber after instantiation.
    ##
    ## Returns: Nothing
    ######################################################################################################

    def setItemNumber(self, itemNumber):
        self.itemNumber = itemNumber

    # class attribute methods for __quantity

    ######################################################################################################
    ## Function: quatity
    ## Purpose: This is a getter for the private attribute __quantity whenever itemObj.quantity
    ##          is called this function is ran.
    ##
    ## Returns: The value of __quantity
    ######################################################################################################

    @property
    def quantity(self):
        return self.__quantity

    ######################################################################################################
    ## Function: quantity
    ## Purpose: This is a setter for the private attribute __quantity whenever itemObj.quantity
    ##          is being assigned a value, this function is called.
    ##
    ## Returns: Nothing
    ######################################################################################################

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    ######################################################################################################
    ## Function: getQuantity
    ## Purpose: This is the getter for quantity after instantiation.
    ## Returns: The value of quantity
    ######################################################################################################

    def getQuantity(self):
        return self.quantity

    ######################################################################################################
    ## Function: getQuantity
    ## Purpose: This is the setter for quantity after instantiation.
    ##
    ## Returns: Nothing
    ######################################################################################################

    def setQuantity(self, quantity):
        self.quantity = quantity

    ######################################################################################################
    ## Function: binNumber
    ## Purpose: This is a getter for the private attribute __binNumber whenever itemObj.binNumber
    ##          is called this function is ran.
    ##
    ## Returns: The value of __binNumber
    ######################################################################################################

    @property
    def binNumber(self):
        return self.__binNumber

    ######################################################################################################
    ## Function: binNumber
    ## Purpose: This is a setter for the private attribute __binNumber whenever itemObj.binNumber
    ##          is being assigned a value, this function is called.
    ##
    ## Returns: Nothing
    ######################################################################################################

    @binNumber.setter
    def binNumber(self, binNumber):
        self.__binNumber = binNumber

    ######################################################################################################
    ## Function: getBinNumber
    ## Purpose: This is the getter for binNumber after instantiation.
    ## Returns: The value of itemNumber
    ######################################################################################################

    def getBinNumber(self):
        return self.binNumber

    ######################################################################################################
    ## Function: setBinNumber
    ## Purpose: This is the setter for binNumber after instantiation.
    ##
    ## Returns: Nothing
    ######################################################################################################

    def setBinNumber(self, quantity):
        self.binNumber = quantity

    ######################################################################################################
    ## Function: inStock
    ## Purpose: This is a getter for the private attribute __inStock whenever itemObj.inStock
    ##          is called this function is ran.
    ##
    ## Returns: The value of __inStock
    ######################################################################################################

    @property
    def inStock(self):
        return self.__inStock

    ######################################################################################################
    ## Function: inStock
    ## Purpose: This is a setter for the private attribute __inStock whenever itemObj.inStock
    ##          is being assigned a value, this function is called.
    ##
    ## Returns: Nothing
    ######################################################################################################

    @inStock.setter
    def inStock(self, inStock):
        self.__inStock = inStock

    ######################################################################################################
    ## Function: isInStock
    ## Purpose: This is the getter for inStock after instantiation.
    ## Returns: The value of inStock
    ######################################################################################################

    def isInStock(self):
        return self.inStock

    ######################################################################################################
    ## Function: setIsInStock
    ## Purpose: This is the setter for inStock after instantiation.
    ##
    ## Returns: Nothing
    ######################################################################################################

    def setIsInStock(self, inStock):
        self.inStock = inStock

    ######################################################################################################
    ## Function: name
    ## Purpose: This is a getter for the private attribute __name whenever itemObj.name
    ##          is called this function is ran.
    ##
    ## Returns: The value of __name
    ######################################################################################################

    @property
    def name(self):
        return self.__name

    ######################################################################################################
    ## Function: name
    ## Purpose: This is a setter for the private attribute __name whenever itemObj.name
    ##          is being assigned a value, this function is called.
    ##
    ## Returns: Nothing
    ######################################################################################################

    @name.setter
    def name(self, name):
        self.__name = name

    ######################################################################################################
    ## Function: getName
    ## Purpose: This is the getter for name after instantiation.
    ## Returns: The value of name
    ######################################################################################################

    def getName(self):
        return self.name

    ######################################################################################################
    ## Function: setName
    ## Purpose: This is the setter for setName after instantiation.
    ##
    ## Returns: Nothing
    ######################################################################################################

    def setName(self, name):
        self.name = name

    ######################################################################################################
    ## Function: price
    ## Purpose: This is a getter for the private attribute __price whenever itemObj.price
    ##          is called this function is ran.
    ##
    ## Returns: The value of __price
    ######################################################################################################

    @property
    def price(self):
        return self.__price

    ######################################################################################################
    ## Function: price
    ## Purpose: This is a setter for the private attribute __price whenever itemObj.price
    ##          is being assigned a value, this function is called.
    ##
    ## Returns: Nothing
    ######################################################################################################

    @price.setter
    def price(self, price):
        self.__price = price

    ######################################################################################################
    ## Function: getPrice
    ## Purpose: This is the getter for price after instantiation.
    ## Returns: The value of price
    ######################################################################################################

    def getPrice(self):
        return self.price

    ######################################################################################################
    ## Function: setPrice
    ## Purpose: This is the setter for price after instantiation.
    ##
    ## Returns: Nothing
    ######################################################################################################

    def setPrice(self, price):
        self.price = price



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
            # <= allows duplicate value to pivot value to go to lessThan
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

######################################################################################################
## Function:  CSVitemImporter
## Purpose:   Creates a list of item objects from a CSV file
## Arguments: fileName - The name of the file to import
## Returns:   itemList - A list of item objects
######################################################################################################
def CSVitemImporter(fileName):
    # list to hold our item objects
    itemList = list()

    try: 
        # open a file to read
        csv_file = open(fileName, mode='r')
        # DictReader uses first row, which contains headers here, to refer to columns in CSV
        csv_reader = csv.DictReader(csv_file)
        # headers in csv have not been read yet
        readHeader = False
        # the CSV file is read row by row; after the header, items are created and added to the list
        for row in csv_reader:
            if readHeader == False:
                pass
                readHeader = True
            else:
                # adds an item created from a row in the CSV to the list
                itemList.append(item(int(row["item_number"]), int(row["quantity"]), int(row["bin_num"]), row["in_stock"]
                                     , row["name"], float(row["price"])))
    except IOError:
        print("File Not Located or Locked by Another Application")

    return itemList

######################################################################################################
## Function:  CSVitemWriter
## Purpose:   Creates a CSV file from a list of item objects
## Arguments: itemList - a list of item objects
##            CSVheaderString - String containing headers for the CSV file
##            fileName - NThe name of the file to output
##            printOutputToConsole - Determines if output is printed to console
## Returns:   Nothing
######################################################################################################
def CSVitemWriter(itemList, CSVheaderString, fileName, printOutputToConsole = True):
    # open a file to write in
    fileObject = open(fileName, "w")
    # prints the headers for the output CSV file
    if printOutputToConsole:
        print(CSVheaderString)
    # writes the headers for the output CSV file in the file
    fileObject.write(CSVheaderString + "\n")
    # cycles through items in item list and writes the items to separate lines in CSV
    for itemObj in itemList:
        if printOutputToConsole:
            print(str(itemObj))
        fileObject.write(str(itemObj) + "\n")
    # closes CSV file
    fileObject.close()


# Driver
def main():
    inputFile = "InventoryManifest.csv"
    outputFile = "InventoryManifest_Output.csv"
    CSVheadString = '"item_number","quantity","bin_num","in_stock","name","price"'
    CSVitemWriter(quickSort(CSVitemImporter(inputFile)), CSVheadString, outputFile)

main()
