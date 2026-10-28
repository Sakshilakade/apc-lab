class Grandfather:

    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

    def public_function(self):
        print("Public Function")

    def _protected_function(self):
        print("Protected Function")

    def __private_function(self):
        print("Private Function")

    def show_private(self):
        print(self.__private_var)
        self.__private_function()


class Father(Grandfather):

    def display(self):
        print(self.public_var)
        print(self._protected_var)

        self.public_function()
        self._protected_function()


class Son(Father):

    def show(self):
        print(self.public_var)
        print(self._protected_var)

        self.public_function()
        self._protected_function()

        self.show_private()


s = Son()
s.show()