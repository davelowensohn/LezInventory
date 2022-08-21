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
#####
#TODO: REWRITE THIS FILE ###############################
#####
##############################################################################
#
# Hey! 
# Welcome to the Docs that tell you how to define your own items.
#
# If you're here, it means you've probably visited inventoryDocs.rpy already.
# If not, I highly recommend you start there.
#
# There are three types of Items in LezInventory by default.
# Regular Item, which doesn't do anything
# Usable Item, which can be Used, consuming the Item and triggering an effect.
# Equippable Item, which can be equipped into the Equip Slot the Inventory has.
#
##############################################################################
#
# For regular items, you can simply define an Item object, like so:
#
define lezInvExampleItem = Item("Example Item", "A simple example.", None)
#
# This creates a regular item. Item (As well as EquippableItem and UsableItem, which 
# we'll get to in a second) takes three arguments. 
# First one is the name, second is the description, and third is the image.
# Image file doesn't have to be provided, in which case the Item's name will
# be used as text in the Inventory Slot instead.
#
##############################################################################
#
# Next, items that can be Used. You can also think of them as consumable items,
# rather than usable ones. 
#
# To start, you're going to want to copy-paste the UsableItem template.
# (I say template, this is actually the real UsableItem class, just
# with different name so it doesn't get in the way.)
#

# TODO: OUTDATED EXAMPLE. Great examples of usables are Grapefruit and Guava.

# init -1 python:

#     # Give the class a different name, instead of the UsableItemExample.
#     class UsableItemExample(Item):

#         # This marks the Item as usable.
#         usable = True

#         # TODO: Maybe make a config var for this?
#         consumedOnUse = True

#         ## __init__ got ommited, as Apple doesn't take/need any extra arguments.
        
#         # What happens when the Item is used.
#         def used(self, InventoryObject):

#             ##############################################
#             # Here is what happens when the Item is used.
#             # Change this to your desires!
#             ##############################################

#             # By default, just make a note in the console that it has been used.
#             return print("An Item {} has been used!".format(self.name))
#
# As is written in the last comment, by default, all UsableItem does is
# print out the Item used into the console.
#
# In your case, this will happen if you either define the UsableItem class
# rather than creating your own (As described in this paragraph),
# or if you don't change the used() function to your own functionality.
#
# After that, we can define our new Item.
# As already stated, UsableItem takes the same arguments as the regular Item,
# being the name, the description and the image. 
#
# TODO: OUTDATED: define lezInvExampleUsableItem = UsableItemExample(name = "Example Usable" , desc = "A simple example no.2" , image = None) 
#
# Since UsableItem is a subclass of Item, the arguments are passed to the parent class.
# If you decide to change the number of arguments, numOfArguments should
# be changed (the "self" argument also counts).
# 
# (If you don't know what these last lines mean, don't worry,
# that means you probably don't need to know what they mean anyway.)
#
######################################################################################
#
# Finally, items that can be Equipped. The Inventory has one Equip slot
# by default, and you can make it do things on both equipping it and unequipping it.
#
# Again, copy the template below for starters.
# (And again, it's the actual class, just with an example name.
#

# TODO: OUTDATED EXAMPLE. Great examples of equippables are Apple and Lemon.

# init -1 python:

#     # Give the class a different name, instead of the EquippableItemExample.
#     class EquippableItemExample(EquippableItem):

#         # What happens upon the definition.
#         # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
#         # It is ommited in some examples, check those out. 
#         def __init__(self, *args, **kwargs):

#             # Calls the parent class, Item, with everything that it needs.
#             super(UsableItemExample, self).__init__( *args, **kwargs )

#         ############################
#         ## To Be Overwritten
#         ## Should be overwritten by child class
#         ############################
        
#         # What happens when the Item is equipped.
#         def equipped(self, InventoryObject):

#             ###################################################
#             # Here is what happens when the Item is equipped.
#             ###################################################

#             # By default, just make a note in the console that it has been equipped.
#             return print("An Item {} has been equipped!".format(self.name))
        
#         # What happens when the Item is unequipped.
#         def unequipped(self, InventoryObject):

#             ###################################################
#             # Here is what happens when the Item is unequipped.
#             ###################################################

#             # By default, just make a note in the console that it has been unequipped.
#             return print("An Item {} has been unequipped!".format(self.name))# 
#
# As is the case with UsableItem, all it does by default is
# print out the Item equipped/unequipped into the console.
#
# (Mostly copied from above)
# In your case, this will happen if you either define the EquippableItem class
# rather than creating your own (As described in this paragraph),
# or if you don't change the equipped() and/or unequipped function to your own functionality.
#
# And again, he's an example EquippableItem defined.
# As already stated, UsableItem takes the same arguments as the regular Item,
# being the name, the description and the image. 
#
# TODO: OUTDATED: define lezInvExampleEquippableItem = EquippableItemExample("Example Equippable" , "A simple example no.3" , None)
#
# These items are functional. If you want to see for youselves, you can
# run this function ingame to add them to the Inventory.
# #

# TODO: OUTDATED FUNCTION.

# init -1 python:

#     def addDocItems():
#         Inventory.add(lezInvExampleItem)
#         Inventory.add(lezInvExampleUsableItem)
#         Inventory.add(lezInvExampleEquippableItem)
#
######################################################################################
#
# And when you're done reading this, you should be able to define
# your own items, both simple and complex :) 
#
# But of course, you might want to see some examples, first. I got you!
#
# I have included three example Items that aren't placed into the Inventory at any point from my side.
# They are the most simple ones used in my LezInventory project, they should guide you. The files are:
# apple.rpy for a simple look at how equip and unequip effects are done
# passionfruit.rpy for a usable that leads to a label
# dragonfruit.rpy for a usable that let's you show a screen
#
# Go check them out, they're commented and very simple to understand!
#
######################################################################################
#
# I can't wait to see what amazing Items people can create with this!