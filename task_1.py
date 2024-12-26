class FlatIterator:

    def __init__(self, list_of_list):
        self.ind_el = -1
        self.ind_list = 0
        for lst in list_of_list:
            if not lst:
                list_of_list.remove(lst)
        self.list_of_list = list_of_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind_list < len(self.list_of_list):
            if self.ind_el < len(self.list_of_list[self.ind_list]):
                self.ind_el += 1
                item = self.list_of_list[self.ind_list][self.ind_el]
                if self.ind_el == len(self.list_of_list[self.ind_list]) - 1:
                    self.ind_list += 1
                    self.ind_el = -1
                return item
        else:
            raise StopIteration
