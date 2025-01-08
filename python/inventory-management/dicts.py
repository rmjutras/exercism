"""Functions to keep track and alter inventory."""

def alter_inventory(inventory, items, increment):
    """ Renee created this as an abstraction of the add and decrement item functions
    """
    for item in items:
        if inventory.get(item) is None:
            if increment > 0:
                inventory[item] = increment
            else:
                pass
        elif (inventory[item] + increment) < 1:
            inventory[item] = 0
        else:
            inventory[item] += increment
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    return alter_inventory(inventory, items, 1)


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    return add_items({}, items)


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    return alter_inventory(inventory, items, -1)


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    items_list = []
    for item in inventory:
        if inventory[item] > 0:
            items_list.append((item, inventory[item]))
    return items_list

