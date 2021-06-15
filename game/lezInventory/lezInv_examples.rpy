init -750 python:

    # Because Inventory is created with the help of
    # the "default" statement, we can't interact with it during the init phase.

    # Because of that, we'll prepare this function to insert all
    # the example items, and add it to a callback so it gets automatically
    # ran when the game starts.

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

    def resetInventory():

        Inventory.clear()
        addExampleItems()

    if addExampleItems not in config.start_callbacks:
        config.start_callbacks.append(resetInventory)