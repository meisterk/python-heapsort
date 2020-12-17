import unittest


class Heap:
    # Konstruktor mit Datenfeldern
    def __init__(self, liste):
        self.liste = liste
        self.groesse = len(liste)

    # Methoden
    def parent(self, i):
        return (i-1)//2

    def groesstesParent(self):
        return (self.groesse//2)-1

    def vertausche(self, i, j):
        temp = self.liste[i]
        self.liste[i] = self.liste[j]
        self.liste[j] = temp


# Testcases
class TestHeap(unittest.TestCase):
    def test_groesstesParent_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.groesstesParent()
        self.assertEqual(result, 4)

    def test_groesstesParent_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.groesstesParent()
        self.assertEqual(result, 3)

    def test_groesstesParent_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8])
        result = heap.groesstesParent()
        self.assertEqual(result, 3)

    def test_parent_0_is_minus_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.parent(0)
        self.assertEqual(result, -1)

    def test_parent_9_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.parent(9)
        self.assertEqual(result, 4)

    def test_parent_8_is_3(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.parent(8)
        self.assertEqual(result, 3)

    def test_parent_7_is_3(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.parent(7)
        self.assertEqual(result, 3)

    def test_vertausche_1_2(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        heap.vertausche(0, 1)
        self.assertEqual(heap.liste, [2, 1, 3, 4, 5, 6, 7, 8, 9])

    def test_vertausche_1_9(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        heap.vertausche(0, 8)
        self.assertEqual(heap.liste, [9, 2, 3, 4, 5, 6, 7, 8, 1])

    def test_vertausche_1_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        heap.vertausche(0, 0)
        self.assertEqual(heap.liste, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# Run Tests
if __name__ == "__main__":
    unittest.main()
