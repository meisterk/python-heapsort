import unittest


class Heap:
    # Konstruktor mit Datenfeldern
    def __init__(self, liste):
        self.liste = liste
        self.groesse = len(liste)

    # Methoden
    def parent(self, i):
        return (i-1)//2

    def linkesKind(self, i):
        if(i <= self.groesstesParent()):
            return 2*i + 1
        else:
            return -1

    def rechtesKind(self, i):
        r = 2*i+2
        if(r < self.groesse):
            return r
        else:
            return -1

    def groesstesParent(self):
        return (self.groesse//2)-1

    def wert(self, i):
        return self.liste[i]

    def getList(self, i):
        return self.liste

    def maximum(self, a, b, c):
        if(self.wert(a) >= self.wert(b) and self.wert(a) >= self.wert(c)):
            return a
        if(self.wert(b) >= self.wert(a) and self.wert(b) >= self.wert(c)):
            return b
        else:
            return c

    def vertausche(self, i, j):
        temp = self.liste[i]
        self.liste[i] = self.liste[j]
        self.liste[j] = temp


# Testcases
class TestHeap(unittest.TestCase):
    def test_linkesKind_von_2_is_5(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.linkesKind(2)
        self.assertEqual(result, 5)

    def test_linkesKind_von_5_is_minus_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.linkesKind(5)
        self.assertEqual(result, -1)

    def test_rechtesKind_von_5_is_minus_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.rechtesKind(5)
        self.assertEqual(result, -1)

    def test_rechtesKind_von_2_is_6(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.rechtesKind(2)
        self.assertEqual(result, 6)

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

    def test_maximum_0_1_2(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.maximum(0, 1, 2)
        self.assertEqual(result, 2)

    def test_maximum_3_7_8(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.maximum(3, 7, 8)
        self.assertEqual(result, 8)

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
