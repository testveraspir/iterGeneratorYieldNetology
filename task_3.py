import copy


class FlatIteratorHard:

    def __init__(self, initial_list):
        self.ind_el = 0
        self.ind_list = 0
        self.list_of_list = copy.deepcopy(initial_list)

    def __iter__(self):
        return self

    def __next__(self):

        if self.ind_list < len(self.list_of_list):
            while self.list_of_list[self.ind_list]:
                temp_lst = []

                if self.ind_el < len(self.list_of_list[self.ind_list]):
                    ind = self.ind_el
                    item = self.list_of_list[self.ind_list][self.ind_el]

                    if item == [] and ind == len(self.list_of_list[self.ind_list]) - 1:
                        raise StopIteration

                    if not isinstance(item, list):
                        self.list_of_list[self.ind_list].pop(0)
                        if not self.list_of_list[self.ind_list]:
                            self.ind_list += 1
                        return item
                    else:
                        element = self.list_of_list[self.ind_list].pop(0)
                        temp_lst.extend(element)
                        self.list_of_list[self.ind_list] = temp_lst + self.list_of_list[self.ind_list]
        else:
            raise StopIteration
