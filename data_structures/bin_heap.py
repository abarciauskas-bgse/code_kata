execfile('../tree_traversals/tree_helpers.py')

class BinHeap:
    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def set_heap_list(self, data_array):
        self.heap_list = data_array
        self.current_size = len(data_array)

    def perc_up(self, i):
        """
        Updates heap_list from position i
        
        Parameters
        ----------
        i : Heap position to start percolating up

        Returns
        -------
        None
        """
        while i > 1:
            current = self.heap_list[i]
            parent_value = parent(self.heap_list, i)
            if current < parent_value:
                self.heap_list[i] = parent_value
                self.heap_list[i//2-1] = current
                i = i//2-1

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.perc_up(self.current_size-1)




