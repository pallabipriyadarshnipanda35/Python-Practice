class Animal:
    def sound(self):
        print("This is an animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Create instances of each class
animal = Animal()
dog = Dog()
cat = Cat()

# Call the sound method on each instance
animal.sound()  # Output: This is an animal sound
dog.sound()     # Output: Bark
cat.sound()     # Output: Meow