import unittest


class Element:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Heap:
    # Constructor with Attributes
    def __init__(self, liste):
        self.liste = liste
        self.groesse = len(liste)

    # Methods
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

    def priority(self, index):
        return self.liste[index].priority

    def index_of_node_with_maximum_priority(self, index1, index2, index3):
        if((self.priority(index1) >= self.priority(index2)) and (self.priority(index1) >= self.priority(index3))):
            return index1
        if((self.priority(index2) >= self.priority(index1)) and (self.priority(index2) >= self.priority(index3))):
            return index2
        else:
            return index3

    def swap_objects(self, index1, index2):
        temp = self.liste[index1]
        self.liste[index1] = self.liste[index2]
        self.liste[index2] = temp

    def heapify(self, index):
        l = self.index_of_left_child(index)
        r = self.index_of_right_child(index)
        if(l == -1):
            l = index
        if(r == -1):
            r = index
        index_of_max = self.index_of_node_with_maximum_priority(l, r, index)
        if index_of_max != index:
            self.swap_objects(index, index_of_max)
            self.heapify(index_of_max)

    def build_max_heap(self):
        i = self.index_of_biggest_parent()
        while(i >= 0):
            self.heapify(i)
            i = i-1

    def heapsort(self):
        while(self.groesse > 1):
            self.build_max_heap()
            self.swap_objects(0, self.groesse - 1)
            self.groesse = self.groesse - 1

# Testcases


class TestHeap(unittest.TestCase):
    def setUp(self):
        e1 = Element("one", 1)
        e2 = Element("two", 2)
        e3 = Element("three", 3)
        e4 = Element("four", 4)
        e5 = Element("five", 5)
        e6 = Element("six", 6)
        e7 = Element("seven", 7)
        e8 = Element("eight", 8)
        e9 = Element("nine", 9)
        e10 = Element("nine", 10)
        self.liste_1_to_9 = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
        self.liste_1_to_10 = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
        self.liste_2_1_3_to_9 = [e2, e1, e3, e4, e5, e6, e7, e8, e9]
        self.liste_9_2_to_8_1 = [e9, e2, e3, e4, e5, e6, e7, e8, e1]
        self.liste_2_3_1_4_5_7_6_9_8 = [e2, e3, e1, e4, e5, e7, e6, e9, e8]

    def test_left_child_of_2_is_5(self):
        heap = Heap(self.liste_1_to_10)
        result = heap.index_of_left_child(2)
        self.assertEqual(result, 5)

    def test_left_child_of_5_is_minus_1(self):
        heap = Heap(self.liste_1_to_10)
        result = heap.index_of_left_child(5)
        self.assertEqual(result, -1)

    def test_right_child_of_5_is_minus_1(self):
        heap = Heap(self.liste_1_to_10)
        result = heap.index_of_right_child(5)
        self.assertEqual(result, -1)

    def test_right_child_of_2_is_6(self):
        heap = Heap(self.liste_1_to_10)
        result = heap.index_of_right_child(2)
        self.assertEqual(result, 6)

    def test_groesstesParent_is_4(self):
        heap = Heap(self.liste_1_to_10)
        result = heap.index_of_biggest_parent()
        self.assertEqual(result, 4)

    def test_groesstesParent_is_3(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_biggest_parent()
        self.assertEqual(result, 3)

    def test_groesstesParent_is_4(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_biggest_parent()
        self.assertEqual(result, 3)

    def test_parent_0_is_minus_1(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_parent(0)
        self.assertEqual(result, -1)

    def test_parent_9_is_4(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_parent(9)
        self.assertEqual(result, 4)

    def test_parent_8_is_3(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_parent(8)
        self.assertEqual(result, 3)

    def test_parent_7_is_3(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_parent(7)
        self.assertEqual(result, 3)

    def test_maximum_0_1_2(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_node_with_maximum_priority(0, 1, 2)
        self.assertEqual(result, 2)

    def test_maximum_3_7_8(self):
        heap = Heap(self.liste_1_to_9)
        result = heap.index_of_node_with_maximum_priority(3, 7, 8)
        self.assertEqual(result, 8)

    def test_vertausche_1_2(self):
        heap = Heap(self.liste_1_to_9)
        heap.swap_objects(0, 1)
        self.assertEqual(heap.liste, self.liste_2_1_3_to_9)

    def test_vertausche_1_9(self):
        heap = Heap(self.liste_1_to_9)
        heap.swap_objects(0, 8)
        self.assertEqual(heap.liste, self.liste_9_2_to_8_1)

    def test_vertausche_1_1(self):
        heap = Heap(self.liste_1_to_9)
        heap.swap_objects(0, 0)
        self.assertEqual(heap.liste, self.liste_1_to_9)

    def test_heapsort_1(self):
        heap = Heap(self.liste_1_to_9)
        heap.heapsort()
        self.assertEqual(heap.liste, self.liste_1_to_9)

    def test_heapsort_2(self):
        heap = Heap(self.liste_2_3_1_4_5_7_6_9_8)
        heap.heapsort()
        self.assertEqual(heap.liste, self.liste_1_to_9)


'''
    def test_heapsort_3(self):
        heap = Heap([17, -33, 2, 5, 23, 48, 7])
        heap.heapsort()
        self.assertEqual(heap.liste, [-33, 2, 5, 7, 17, 23, 48])
'''

# Run Tests
if __name__ == "__main__":
    unittest.main()
