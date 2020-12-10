import unittest


class Heap:
    # Konstruktor mit Datenfeldern
    def __init__(self, liste):
        self.liste = liste
        self.groesse = len(liste)

    # Methoden
    def vertausche(self, i, j):
        temp = self.liste[i]
        self.liste[i] = self.liste[j]
        self.liste[j] = temp


# Testcases
class TestHeap(unittest.TestCase):
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
