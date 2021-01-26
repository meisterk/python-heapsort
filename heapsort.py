import unittest


class Heap:
    # Konstruktor mit Datenfeldern
    def __init__(self, liste):
        self.liste = liste
        self.groesse = len(liste)

    # Methoden
    def index_of_parent(self, index):
        return (index-1)//2

    def index_of_left_child(self, index):
        if(index <= self.index_of_biggest_parent()):
            return 2*index + 1
        else:
            return -1

    def index_of_right_child(self, index):
        r = 2*index + 2
        if(r < self.groesse):
            return r
        else:
            return -1

    def index_of_biggest_parent(self):
        return (self.groesse//2)-1

    def wert(self, i):
        return self.liste[i]

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

    def heapify(self, i):
        l = self.index_of_left_child(i)
        r = self.index_of_right_child(i)
        if(l == -1):
            l = i
        if(r == -1):
            r = i
        max = self.maximum(l, r, i)
        if max != i:
            self.vertausche(i, max)
            self.heapify(max)

    def baueMaxHeap(self):
        i = self.index_of_biggest_parent()
        while(i >= 0):
            self.heapify(i)
            i = i-1

    def heapsort(self):
        while(self.groesse > 1):
            self.baueMaxHeap()
            self.vertausche(0, self.groesse - 1)
            self.groesse = self.groesse - 1

# Testcases


class TestHeap(unittest.TestCase):
    def test_linkesKind_von_2_is_5(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.index_of_left_child(2)
        self.assertEqual(result, 5)

    def test_linkesKind_von_5_is_minus_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.index_of_left_child(5)
        self.assertEqual(result, -1)

    def test_rechtesKind_von_5_is_minus_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.index_of_right_child(5)
        self.assertEqual(result, -1)

    def test_rechtesKind_von_2_is_6(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.index_of_right_child(2)
        self.assertEqual(result, 6)

    def test_groesstesParent_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = heap.index_of_biggest_parent()
        self.assertEqual(result, 4)

    def test_groesstesParent_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.index_of_biggest_parent()
        self.assertEqual(result, 3)

    def test_groesstesParent_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8])
        result = heap.index_of_biggest_parent()
        self.assertEqual(result, 3)

    def test_parent_0_is_minus_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.index_of_parent(0)
        self.assertEqual(result, -1)

    def test_parent_9_is_4(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.index_of_parent(9)
        self.assertEqual(result, 4)

    def test_parent_8_is_3(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.index_of_parent(8)
        self.assertEqual(result, 3)

    def test_parent_7_is_3(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = heap.index_of_parent(7)
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

    def test_heapsort_1(self):
        heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        heap.heapsort()
        self.assertEqual(heap.liste, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_heapsort_2(self):
        heap = Heap([2, 3, 1, 4, 5, 7, 6, 9, 8])
        heap.heapsort()
        self.assertEqual(heap.liste, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_heapsort_3(self):
        heap = Heap([17, -33, 2, 5, 23, 48, 7])
        heap.heapsort()
        self.assertEqual(heap.liste, [-33, 2, 5, 7, 17, 23, 48])


# Run Tests
if __name__ == "__main__":
    unittest.main()
