#!/usr/bin/python3
"""
Animal Module

This module provides an abstract base class `Animal` and its subclasses `Dog`
and `Cat`, which define specific implementations of the abstract method `sound`

Classes:
    Animal (ABC): An abstract base class that defines the blueprint for all
    animal classes, requiring them to implement the `sound` method.
    Dog (Animal): A subclass of `Animal` that implements the `sound` method to
    return "Bark".
    Cat (Animal): A subclass of `Animal` that implements the `sound` method to
    return "Meow".

Example:
    You can create instances of `Dog` and `Cat`, but not `Animal` directly:

        bobby = Dog()
        garfield = Cat()

        print(bobby.sound())  # Output: Bark
        print(garfield.sound())  # Output: Meow

    Attempting to instantiate `Animal` will raise a `TypeError`:

        animal = Animal()  # Raises: TypeError: Can't instantiate abstract
        class Animal with abstract method sound
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class representing an Animal.

    This class provides a template for other animal classes to implement the
    sound method.

    Methods:
        sound(): Abstract method that must be implemented by any subclass of
        Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses to define the
        sound of the animal.

        Raises:
            NotImplementedError: If this method is not implemented by a
            subclass.
        """
        pass


class Dog(Animal):
    """
    Dog Class

    A subclass of the `Animal` abstract base class representing a dog.

    Methods:
        sound(): Returns the sound made by a dog, which is "Bark".
    """

    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: The string "Bark", representing the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat Class

    A subclass of the `Animal` abstract base class representing a cat.

    Methods:
        sound(): Returns the sound made by a cat, which is "Meow".
    """

    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: The string "Meow", representing the sound a cat makes.
        """
        return "Meow"
