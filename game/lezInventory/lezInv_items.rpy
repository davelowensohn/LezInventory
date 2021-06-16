# Copyright 2021 - 2xxx Jan "Lezalith" Mašek <lezalith@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
##############################################################################

init -890 python:

    ###########################################
    ###########################################
    #
    # Item Class
    #
    ###########################################
    ###########################################

    class Item():

        "Base class for all the items."

        # Initialization. Arguments:
        #
        # name - String, name of the item.
        #
        # desc - Description of the item.
        #
        # image - Image of the Item. Can be a file,
        # a displayable, or the default None, which then
        # creates a Text Displayable from the name argument.

        # What happens upon the definition.
        def __init__(self, name, desc, image = None):

            # Name of the Item.
            self.name = name

            # Description of the Item.
            self.description = desc

            # Image of the Item.
            if image:
                self.image = image
            else:
                # Use Text Displayable if Image not given.
                self.image = Text(name, size = 20)

            # This is the base class for Items, 
            # so there is no functionality for these.
            self.usable = False
            self.consumedOnUse = False
            self.equippable = False

        ############################
        ## Getters
        ############################

        def getImage(self):

            return self.image

        ############################
        ## Checks
        ############################

        # Used by the Inventory screen, whether Item can be Equipped.
        def isEquippable(self):

            return self.equippable

        # Used by the Inventory screen, whether Item can be Used.
        def isUsable(self):

            return self.usable

        ############################
        ## To Be Overwritten
        ## Should be overwritten by child class
        ############################
        
        # What happens when the Item is used.
        def used(self, InventoryObject):
            return None 

        # What happens when the Item is Equipped.
        def equipped(self, InventoryObject):
            return None 

        # What happens when the Item is Unequipped.
        def unequipped(self, InventoryObject):
            return None

    ###########################################
    ###########################################
    #
    # UsableItem Class
    #
    ###########################################
    ###########################################

    # Class for Usable Items.
    class UsableItem(Item):

        # What happens upon the definition.
        def __init__(self, name, desc, image = None, consumedOnUse = True):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less arguments than should be.
            numOfArguments = 5

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(UsableItem, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

            # That's the point of this class.
            self.usable = True

            # Whether the Item is removed from the Inventory when Used.
            self.consumedOnUse = consumedOnUse

        ############################
        ## To Be Overwritten
        ## Should be overwritten by child class
        ############################
        
        # What happens when the Item is used.
        def used(self, InventoryObject):

            # By default, just make a note in the console that it has been used.
            return print("An Item {} has been used!".format(self.name))

    ###########################################
    ###########################################
    #
    # EquippableItem Class
    #
    ###########################################
    ###########################################

    # Class for Equippable Items.
    class EquippableItem(Item):

        # What happens upon the definition.
        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less arguments than should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(EquippableItem, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

            # That's the point of this class.
            self.equippable = True

        ############################
        ## To Be Overwritten
        ## Should be overwritten by child class
        ############################
        
        # What happens when the Item is equipped.
        def equipped(self, InventoryObject):

            # By default, just make a note in the console that it has been equipped.
            return print("An Item {} has been equipped!".format(self.name))
        
        # What happens when the Item is unequipped.
        def unequipped(self, InventoryObject):

            # By default, just make a note in the console that it has been unequipped.
            return print("An Item {} has been unequipped!".format(self.name))