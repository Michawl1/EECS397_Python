# Implement this function:
def store_checkout(inventory_tuple_list, item_purchase_list):
    """
        inventory_tuple_list:
            A list of tuples. Each tuple has a string representing an
            item name, an int representing a price, and a string representing
            a description.

            Example: [("A", 5, "shiny new A"), ("B", 10, "big heavy B")]


        item_purchase_list:
            A list of strings. Each string represents an item name.

            Example: ["A", "A", "B", "C"]


        Return the total price of the items in item_purchase_list by using
        prices from the provided inventory_tuple_list. If an item does not
        have a price, it is free. The descriptions are extra, useless
        information for this function.

        The example inputs here would have a total cost of:
        5 + 5 + 10 + 0 = 20
    """
    total = 0
    pricing_dictionary = {}
    for tuple in inventory_tuple_list:
        pricing_dictionary[tuple[0]] = tuple[1]

    for purchase_item in item_purchase_list:
        if pricing_dictionary.__contains__(purchase_item):
            total += pricing_dictionary[purchase_item]

    return total


# Implement this function:
def highest_frequency_count(item_list):
    """
        item_list:
            A list of strings. Each string represents an item name.

            Example: ["A", "A", "B", "C", "A", "B", "B"]


        Find and return a count for the most frequently occurring item
        in item_list.

        In the example, "A" and "B" each appear 3 times, while "C" appears
        only 1 time. Therefore, expected return value would be 3.
    """
    return_list = {}

    for item in item_list:
        if return_list.__contains__(item):
            return_list[item] = return_list[item] + 1
        else:
            return_list[str(item)] = 1

    return (sorted(return_list.items(), key=lambda x: x[1], reverse=True))[0][1]
