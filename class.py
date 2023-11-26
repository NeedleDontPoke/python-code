from abc import ABCMeta, abstractmethod


class Main(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_n')

    def __init__(self, name, n=0):
        self._name = name
        self._n = n

    @property
    def name(self):
        return self._name

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        self._n = n

    @abstractmethod
    def count(self):
        return self._name * self._n if self._n != 0 else 'error'


class Person(Main):
    def count(self):
        return self._name * self._n


def main():
    persons = [Person('gzy', 5), Person('hyy', 2)]
    for person in persons:
        print(person.count())


if __name__ == '__main__':
    main()
