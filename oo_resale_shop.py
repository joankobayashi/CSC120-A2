from computer import *
from typing import Dict, Union


inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}

"""
Class of ResaleShop, the category of things classified on the resale shop side
"""

class ResaleShop:
    
    # Attributes it will need
    inventory : list
    
    # making itemID accessible 
    global itemID

    itemID = 0 # We'll increment this every time we add a new item 
               # so that we always have a new value for the itemID
    
    # Setting up the constructor
    def __init__(self):
        self.inventory = []

        
    # Methods I will need

    """
    buy: Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    
    def buy(self, description, processor_type, hard_drive_capacity, memory, operating_system,
        year_made, price):
        global itemID
        print("Buying", description)
        print("Adding to inventory...")
        new_computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system,
        year_made, price)
        self.inventory.append(new_computer)
        itemID += 1     # increment itemID
        print("Done.\n")
        return itemID


    


    """
    sell: Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, c:Computer):
        if c in self.inventory:
            print("Selling Item ID:", itemID)
            self.inventory.remove(c)
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")
        print()

    """
    print inventory: prints all the items in the inventory (if it isn't empty) with details, 
    prints error otherwise
    """

    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            print("Checking inventory... ")
            for c in self.inventory:
                # Print its details
                print("Item ID:", itemID, end=" ") 
                c.print_details()
                print("Done.")
        else:
            print("Checking inventory... ")
            print("No inventory to display.")
            print("Done.")

    """
    refurbish: Takes in the information of computer, upgrades the OS,  
    prints error otherwise
    """

    def refurbish(self, c:Computer):
        
        if c in self.inventory:
            print("Refurbishing Item ID:", itemID)
            
            """
            update price: Takes in an item_id and a new price, updates the price of the associated
            computer if it is the inventory
            """

            if int(c.year_made) < 2000:
                c.price = 0 # too old to sell, donation only
            elif int(c.year_made) < 2012:
                c.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(c.year_made) < 2018:
                c.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                c.price = 1000 # recent stuff

            #assigning new OS
            new_OS = "MacOS Monterey"

            if c.operating_system is not new_OS:
                print("Upgrading OS to ", new_OS)
                print("Upgrading Inventory...")
                c.operating_system = new_OS
                print("Done.")
                print()
        
        else:
            print("Item not found. Please select another item to refurbish.")


# Testing with a main function

def main():
    myShop = ResaleShop()
    
    # Print a little banner
    print()
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    
    # information about the computer
    myShop.buy("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    # checks inventory
    myShop.print_inventory()
    print()

    # refurbishes and checks inventory
    myShop.refurbish(myShop.inventory[0])
    myShop.print_inventory()
    print()

    # sells and checks inventory
    myShop.sell(myShop.inventory[0])
    myShop.print_inventory()
    print()

if __name__ == "__main__": main()