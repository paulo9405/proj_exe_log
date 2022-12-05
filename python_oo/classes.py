class Contador(object):
    def __init__(self):
        self.total = 0

    def zerar(self):
        self.__del__()
        return self.retornar_valor()


    def incrementar(self, valor):
        self.total += valor
        return self.retornar_valor()

    def retornar_valor(self):
        return self.total

    def __del__(self):
        self.total = 0
        return self.total


class Person(object):
    def __init__(self, name, dad, mom):
        self.name = name
        self.dad = dad
        self.mom = mom

    def is_same(self, other_person):
        if self.name == other_person.name and self.mom == other_person.mom:
            return True

    def is_sibling(self, other_person):
        return self.dad == other_person.dad and self.mom == other_person.mom

    def is_predecessor(self, other_person):
        if self.is_same(other_person):
            return False

        if self.dad == other_person or self.mom == other_person:
            return True

        if self.dad is not None and self.dad.is_predecessor(other_person):
            return True

        if self.mom is not None and self.mom.is_predecessor(other_person):
            return True

        return False