from stack import Stack


class UniqueStack(Stack):
    def __init__(self):
        """
        A unique stack is a stack that will only store 1 copy of a particular item
        """
        super(UniqueStack, self).__init__()
        self._item_set = set()

    def push(self, item):
        """
        adds a new item to the stack only if the new item is unique to the stack, also adds the item to
        :param item: new item to be added to the stack
        :raises TypeError: if item is None
        :raises ValueError: if item is already in the stack
        """
        if self._item_set.__contains__(item):
            raise ValueError("Stack will not two identical objects")
        self._item_set.add(item)
        super().push(item)

    def pop(self):
        """
        removes the top item from the stack
        :return: the item from the stack
        """
        if len(self._item_set) > 0:
            self._item_set.remove(super().peek())
        return super().pop()


class LimitedStack(Stack):
    def __init__(self, capacity):
        """
        A limit stack is a stack with a maximum capacity.
        If the stack size is at capacity, adding a new item will raise LimitedStackOverflowError
        :param capacity: the capacity of the stack
        :raises TypeError: if capacity is not an int
        :raises ValueError: if capacity < 0
        """
        if type(capacity) is not int:
            raise TypeError("capacity must be of type int")

        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        super(LimitedStack, self).__init__()
        self._capacity = capacity

    def push(self, item):
        """
        adds a new item to the stack only if the stack isn't full
        :param item: new item to be added to the stack
        :raises TypeError: if item is None
        :raises LimitedStackOverflowError: if you are trying to add an item past the capacity of the stack
        """
        if len(self._stack_items) is self._capacity:
            raise LimitedStack.LimitedStackOverflowError("Stack is at capacity")

        super().push(item)

    class LimitedStackOverflowError(Exception):
        pass


class RotatingStack(LimitedStack):
    def __init__(self, capacity):
        """
        A rotating stack is a stack with a maximum capacity.
        If the stack size is at capacity, adding a new item will remove the oldest item from the stack to make room for
        the new item.
        :param capacity: the capacity of the stack
        :raises TypeError: if item is None
        :raises TypeError: if capacity is not an int
        :raises ValueError: if capacity < 0
        """
        super(RotatingStack, self).__init__(capacity)
        self._capacity = capacity

    def push(self, item):
        """
        adds a new item to the stack, removes the oldest item if the stack is at capacity
        :param item: new item to be added to the stack
        :raises TypeError: if item is None
        """
        if item is None:
            raise TypeError("item cannot be type None")

        if len(self._stack_items) is self._capacity:
            del self._stack_items[:-1]

        self._stack_items.append(item)
