class Animal(object):
    """This is the base class."""

    def __init__(self, species, age):
        self.species = species
        self.age = age

    # Instance method.
    def description(self):
        print(f"{self.species} is {self.age} years old")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError(f"Provided {age} age has to be a positive number.")
