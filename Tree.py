from Plant import *
import Randomizer


# ----------------------------------------------
class Tree(Plant):
    def __init__(self):
        self.name = ""
        self.length = 0
        self.age = 0

    def ReadStrArray(self, strarray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strarray) - 2:
            return 0
        self.name = strarray[i]
        self.length = int(strarray[i + 1])
        self.age = int(strarray[i + 2])
        i += 3
        # print("tree: name = ", self.name, " length = ", self.length, " age = ", self.age)
        return i

    def RandomRead(self):
        self.length = Randomizer.generate() % 20 + 1
        self.name = Randomizer.namegenerate(self.length)
        self.age = Randomizer.generate()

    def Print(self):
        print("tree: name =", self.name, ", length =", self.length,
              ", age =", self.age, ", Fraction =", self.Fraction())
        pass

    def Write(self, ostream):
        ostream.write("tree: name = {}, length = {}, age = {}, Fraction = {}".format
                      (self.name, self.length, self.age, self.Fraction()))
        pass

    def Fraction(self):
        vowels_count = 0
        for i in range(0, len(self.name)):
            if self.name[i] == 'a' or self.name[i] == 'e' or self.name[i] == 'i' \
                    or self.name[i] == 'o' or self.name[i] == 'u':
                vowels_count += 1

        return 1.0 * vowels_count / self.length

        pass
