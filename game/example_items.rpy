
# We execute inits in the logical order: Inventory -> Items -> ...
# Lower numbers execute first. 
#
# This would be important if, for example, Items used some parts of the Inventory,
# we'd need to make sure Inventory was defined before Items.
#
# At the time of writing this comment, there are no such connections present.
# However, they are common, so I want to keep the practice going. 
#

init -750 python:

    # -(1)- ...running this straight away would give us "Inventory" not defined.
    # Which is why we're only setting it up here, and we'll run this when
    # we start the game.

    def addExampleItems():

        # Equippables
        Inventory.add(durian)
        Inventory.add(grapes)
        Inventory.add(lemon)
        Inventory.add(apple)

        # Passives
        Inventory.add(cherries)
        Inventory.add(orange)
        Inventory.add(cranberries)
        Inventory.add(kiwi)
        Inventory.add(strawberry)

        # Usables
        Inventory.add(dragonFruit)
        Inventory.add(guava)
        Inventory.add(apricot)
        Inventory.add(wmelon)
        Inventory.add(passionFruit)
        Inventory.add(grapefruit)