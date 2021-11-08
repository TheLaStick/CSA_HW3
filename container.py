# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # def ReadStrArray(self, strarray):

    def Print(self):
        print("Container stores ", len(self.store), " plants:")
        for plant in self.store:
            plant.Print()

        plants = self.DeleteSort()
        print("Plants with Fractions higher than average = {}\n".format(len(plants)))
        for plant in plants:
            plant.Print()

        pass

    def Write(self, ostream):
        ostream.write("Container stores {} plants:\n".format(len(self.store)))
        for plant in self.store:
            plant.Write(ostream)
            ostream.write("\n")

        plants = self.DeleteSort()
        ostream.write("\nPlants with Fractions higher than average = {}\n".format(len(plants)))
        for plant in plants:
            plant.Write(ostream)
            ostream.write("\n")
        pass

    def DeleteSort(self):
        sum_of_fractions = 0
        for plant in self.store:
            sum_of_fractions += plant.Fraction()

        sum_of_fractions /= len(self.store)
        new_cont = []

        for new_plant in self.store:
            if new_plant.Fraction() >= sum_of_fractions:
                new_cont.append(new_plant)

        return new_cont
