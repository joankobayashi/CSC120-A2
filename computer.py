"""
Class of Computer, the category of things classified on the computer shop side
"""

class Computer:

    # Attributes it will need
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # Setting up the constructor, which are the information about the computers

    def __init__(self, description: str, processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int)-> None: 
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?

    """
    print details: Takes in a Dict containing all the information about a computer,
    returns the detailed information about the computer with its meanings
    """

    def print_details(self):
        print("{'description':", self.description, "'processor_type':", 
         self.processor_type, "'hard_drive_capacity':", self.hard_drive_capacity, "'memory':", self.memory,
        "'operating_system':",self.operating_system, "'year_made':",self.year_made, "'price':",self.price,"}")

   