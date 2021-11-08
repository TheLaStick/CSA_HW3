from Plant import *
from enum import Enum
import Randomizer


class Type(Enum):
    HOME = 1
    GARDEN = 2
    WILD = 3


# ----------------------------------------------
class Flower(Plant):
    def __init__(self):
        self.name = ""
        self.length = 0
        self.type = Type(1)

    def ReadStrArray(self, strarray, i):
        # должно быть как минимум три непрочитанных значения в массиве
        if i >= len(strarray) - 2:
            return 0
        self.name = strarray[i]
        self.length = int(strarray[i + 1])
        self.type = Type(int(strarray[i + 2]) % 3 + 1)
        i += 3
        # print("tree: a = ", self.a, " b = ", self.b, "c = ", self.c)
        return i

    def RandomRead(self):
        self.length = Randomizer.generate() % 20 + 1
        self.name = Randomizer.namegenerate(self.length)
        self.type = Type(Randomizer.generate() % 3 + 1)

    def Print(self):
        print("Flower: name =", self.name, ", length =", self.length,
              ", type =", self.type, ", Fraction =", self.Fraction())
        pass

    def Write(self, ostream):
        ostream.write("flower: name = {}, length = {}, type = {}, Fraction = {}".format
                      (self.name, self.length, self.type, self.Fraction()))
        pass

    def Fraction(self):
        vowels_count = 0
        for i in range(0, len(self.name)):
            if self.name[i] == 'a' or self.name[i] == 'e' or self.name[i] == 'i' \
                    or self.name[i] == 'o' or self.name[i] == 'u':
                vowels_count += 1

        return 1.0 * vowels_count / self.length

        pass
