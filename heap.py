from random import *


class MaxHeap:
    def __init__(self, starting_array=None):

        if starting_array is None:
            self._heap = []
            self._array_size = 0
        else:
            self._heap = starting_array
            self._array_size = len(self._heap)
            self.heapify()

    def heapify(self):

        last_internal_node = self._array_size // 2 - 1

        for i in range(last_internal_node, -1, -1):
            left = 2 * i + 1
            right = 2 * i + 2
            if (left < self._array_size and self._heap[i] < self._heap[left]) or \
                    (right < self._array_size and self._heap[i] < self._heap[right]):
                self.percolate_down(i)

    def percolate_down(self, subtree_index):
        i = subtree_index
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self._array_size and self._heap[i] < self._heap[left]:
            i = left
        if right < self._array_size and self._heap[i] < self._heap[right]:
            i = right
        if i != subtree_index:
            (self._heap[subtree_index], self._heap[i]) = (self._heap[i], self._heap[subtree_index])  # swap
            self.percolate_down(i)

    def percolate_up(self, subtree_index):
        i = subtree_index
        parent = int((i - 1) / 2)
        if self._heap[parent] < self._heap[i]:
            (self._heap[parent], self._heap[i]) = (self._heap[i], self._heap[parent])  # swap
            self.percolate_up(parent)

    def remove_node(self):
        """puts returned value in last position to facilitate sort"""
        i = self._array_size - 1
        (self._heap[i], self._heap[0]) = (self._heap[0], self._heap[i])  # swap
        self._array_size -= 1
        self.percolate_down(0)
        return self._heap[i]

    def add_node(self, x):
        self._heap.append(x)
        self._array_size += 1
        self.percolate_up(self._array_size - 1)

    def sort_heap(self):
        for i in range(self._array_size - 1, 0, -1):
            self.remove_node()
        return self._heap


# Driver code to test heapify and sort
def main():
    SIZE = 40
    my_array = [randint(0, SIZE) for _ in range(1, SIZE + 1)]
    print(f'original: {my_array}')
    h = MaxHeap(my_array)
    print(f'heaped: {my_array}')
    h.add_node(9999)
    print(f'add 9999: {my_array}')
    h.add_node(0)
    print(f'add 9999: {my_array}')
    h.heapify()
    print(f're-heap : {my_array}')
    sorted_array = h.sort_heap()
    print(f'sorted: {sorted_array}')


if __name__ == "__main__":
    main()
