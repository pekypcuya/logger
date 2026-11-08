import types
from logger import logger


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_list):
            current_list = self.list_of_list[self.outer_index]
            if self.inner_index < len(current_list):
                item = current_list[self.inner_index]
                self.inner_index += 1
                return item
            else:
                self.outer_index += 1
                self.inner_index = 0
        raise StopIteration


def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


# Логируем потребление генератора: результат = готовый список
@logger('flat_generator.log')
def consume_generator(list_of_lists):
    return list(flat_generator(list_of_lists))


# Логируем потребление итератора аналогично
@logger('flat_iterator.log')
def consume_iterator(list_of_lists):
    return list(FlatIterator(list_of_lists))


if __name__ == '__main__':
    data = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(consume_generator(data))
    print(consume_iterator(data))