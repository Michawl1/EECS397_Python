import unittest
from assignment4 import UniqueStack
from assignment4 import LimitedStack
from assignment4 import RotatingStack


class UniqueStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_push(self):
        test_unique = UniqueStack()
        test_unique.push(UniqueStackTestCase.ITEM_1)
        test_unique.push(UniqueStackTestCase.ITEM_2)
        test_unique.push(UniqueStackTestCase.ITEM_3)

        with self.assertRaises(TypeError):
            test_unique.push(None)

        with self.assertRaises(ValueError):
            test_unique.push(UniqueStackTestCase.ITEM_1)

    def test_pop(self):
        test_unique = UniqueStack()

        self.assertEqual(None, test_unique.pop())

        test_unique.push(UniqueStackTestCase.ITEM_1)
        test_unique.push(UniqueStackTestCase.ITEM_2)
        test_unique.push(UniqueStackTestCase.ITEM_3)

        self.assertEqual(test_unique.pop(), UniqueStackTestCase.ITEM_3)
        self.assertEqual(test_unique.pop(), UniqueStackTestCase.ITEM_2)
        self.assertEqual(test_unique.pop(), UniqueStackTestCase.ITEM_1)


class LimitStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def testConstructor(self):
        with self.assertRaises(TypeError):
            LimitedStack("hello")

        with self.assertRaises(ValueError):
            LimitedStack(0)

    def testPush(self):
        test_limited = LimitedStack(2)

        with self.assertRaises(TypeError):
            test_limited.push(None)

        test_limited.push(LimitStackTestCase.ITEM_1)
        test_limited.push(LimitStackTestCase.ITEM_2)

        with self.assertRaises(LimitedStack.LimitedStackOverflowError):
            test_limited.push(LimitStackTestCase.ITEM_3)

    def testPop(self):
        test_limited = LimitedStack(2)

        self.assertEqual(None, test_limited.pop())

        test_limited.push(LimitStackTestCase.ITEM_1)
        test_limited.push(LimitStackTestCase.ITEM_2)

        self.assertEqual(test_limited.pop(), LimitStackTestCase.ITEM_2)
        self.assertEqual(test_limited.pop(), LimitStackTestCase.ITEM_1)


class RotatingStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def testConstructor(self):
        with self.assertRaises(TypeError):
            RotatingStack("hello")

        with self.assertRaises(ValueError):
            RotatingStack(0)

    def testPush(self):
        test_rotating = RotatingStack(2)

        with self.assertRaises(TypeError):
            test_rotating.push(None)

        test_rotating.push(RotatingStackTestCase.ITEM_1)
        test_rotating.push(RotatingStackTestCase.ITEM_2)
        self.assertEqual(test_rotating.peek(), RotatingStackTestCase.ITEM_2)

        test_rotating.push(RotatingStackTestCase.ITEM_3)
        self.assertEqual(test_rotating.peek(), RotatingStackTestCase.ITEM_3)
        self.assertEqual([RotatingStackTestCase.ITEM_2, RotatingStackTestCase.ITEM_3], test_rotating._stack_items)

    def testPop(self):
        test_rotating = RotatingStack(2)

        self.assertEqual(None, test_rotating.pop())

        test_rotating.push(RotatingStackTestCase.ITEM_1)
        test_rotating.push(RotatingStackTestCase.ITEM_2)

        self.assertEqual(test_rotating.pop(), RotatingStackTestCase.ITEM_2)
        self.assertEqual(test_rotating.pop(), RotatingStackTestCase.ITEM_1)


if __name__ == '__main__':
    unittest.main()
