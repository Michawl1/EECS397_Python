import unittest
from assignment4 import UniqueStack as uni
from assignment4 import LimitedStack as lim
from assignment4 import RotatingStack as rot


class UniqueStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_push(self):
        test_unique = uni()
        test_unique.push(UniqueStackTestCase.ITEM_1)
        test_unique.push(None)

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

'''
class UniqueStack(Stack, unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    """
    UniqueStack has the same methods and functionality as Stack, but will only store one
    copy of a particular item at a time.

    If push is called with an item that is already in the UniqueStack, a ValueError should be raised
    with an appropriate error message.

    If push is called where item equals None, a TypeError should be raised like in the base class.

    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. New versions of __init__(), push(), and pop() should be sufficient.

    Hint: One option to implement this is to maintain an internal set() alongside the internal list.
    """

    def test_push(self):
        test_unique = UniqueStack()
        test_unique.push(UniqueStack.ITEM_1)
        test_unique.push(None)

        print(test_unique._stack_items)
        self.assertEqual(1, 1)


class LimitedStack(Stack):
    """
    A LimitedStack has the same methods and functionality as Stack, but will only hold up to a certain
    number of items.

    The __init__ method for LimitedStack should take a single, positive integer as an argument. This will
    be the maximum number of items that the LimitedStack can hold. If push is called with an item and that
    item would go beyond the LimitedStack's capacity, the item is not added to the LimitedStack and a
    LimitedStack.LimitedStackOverflowError should be raised.

    If push is called where item equals None, a TypeError should be raised like in the base class.

    If __init__ is called with a non-integer argument, a TypeError should be raised.
    If __init__ is called with an int <= 0, a ValueError should be raised.

    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. New versions of __init__() and push() should be sufficient.
    """

    class LimitedStackOverflowError(Exception):
        pass

    # Add mehods here. Remove this comment and the next line before doing so.
    pass


class RotatingStack(LimitedStack):
    """
    A RotatingStack has the same methods and functionality as LimitedStack, but will not raise an
    exception when an item is added that would go beyond the maximum capacity. Instead, the item
    will be added to the stack and then the oldest item from the RotatingStack will be dropped.

    The __init__ method for RotatingStack should take a single, positive integer as an argument. This will
    be the maximum number of items that the RotatingStack can hold. If push is called with an item and that
    item would go beyond the Rotating's capacity, the item will be added to the stack, but only after
    discarding the oldest item in the stack.

    If push is called where item equals None, a TypeError should be raised like in the base class.

    If __init__ is called with a non-integer argument, a TypeError should be raised.
    If __init__ is called with an int <= 0, a ValueError should be raised.

    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. As long as LimitedStack has properly handled the __init__ method functionality,
    only a new version of push() should be needed.
    """

    # Add mehods here. Remove this comment and the next line before doing so.
    pass
    '''
