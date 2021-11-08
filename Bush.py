from Plant import *
from enum import Enum
import Randomizer

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


# ----------------------------------------------
class Bush(Plant):
    def __init__(self):
        self.name = ""
        self.length = 0
        self.month = Month(1)

    def ReadStrArray(self, strarray, i):
        # должно быть как минимум три непрочитанных значения в массиве
        if i >= len(strarray) - 2:
            return 0
        self.name = strarray[i]
        self.length = int(strarray[i + 1])
        self.month = Month(int(strarray[i + 2]) % 12 + 1)
        i += 3
        # print("tree: a = ", self.a, " b = ", self.b, "c = ", self.c)
        return i

    def RandomRead(self):
        self.length = Randomizer.generate() % 20 + 1
        self.name = Randomizer.namegenerate(self.length)
        self.month = Month(Randomizer.generate() % 12 + 1)

    def Print(self):
        print("Bush: name =", self.name, ", length =", self.length,
              ", month =", self.month, ", Fraction =", self.Fraction())
        pass

    def Write(self, ostream):
        ostream.write("bush: name = {}, length = {}, month = {}, Fraction = {}".format
                      (self.name, self.length, self.month, self.Fraction()))
        pass

    def Fraction(self):
        vowels_count = 0
        for i in range(0, len(self.name)):
            if self.name[i] == 'a' or self.name[i] == 'e' or self.name[i] == 'i' \
                    or self.name[i] == 'o' or self.name[i] == 'u':
                vowels_count += 1

        return 1.0 * vowels_count / self.length

        pass
