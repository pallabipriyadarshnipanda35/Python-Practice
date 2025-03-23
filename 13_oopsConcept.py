class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow!"

# Example usage
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", breed="Siamese")

print(f"{dog.name} is a {dog.breed} and says {dog.make_sound()}")
print(f"{cat.name} is a {cat.breed} and says {cat.make_sound()}")