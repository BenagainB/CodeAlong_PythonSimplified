
class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
        self.__cost = 50  # private member

    def play(self):
        print("pam pam pam pam pam pam pam")


class BassGuitar(Guitar):
    pass


class ElectricGuitar(Guitar):   # inheritance
    def __init__(self):
        super().__init__(n_strings=8)  # override super to have same named member
        self.color = ("#000000", "#FFFFFF")     # colors are black and white

    def play_louder(self):
        print("pam pam pam pam pam pam pam".upper())

    def __secret(self):     # access parent private member and keep as private in this class
        print("this guitar actually cost me $", self._Guitar__cost, "only!")


def main():
    my_guitar = Guitar()
    print("my_guitar has", my_guitar.n_strings, "strings")
    my_electric = ElectricGuitar()
    my_electric.play_louder()
    print("my_electric has", my_electric.n_strings, "strings")
    print("my_electric has", my_electric.color, "color")
    # print("my_electric has", my_electric.cost, "cost")  #can't access private member
    my_electric._ElectricGuitar__secret()
    print("BassGuitar has", BassGuitar(4).n_strings, "strings")


if __name__ == '__main__':
    main()
