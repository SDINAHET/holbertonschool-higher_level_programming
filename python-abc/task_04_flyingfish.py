#!/usr/bin/python3
"""
Module that defines a FlyingFish class, demonstrating multiple inheritance.

The module contains the following classes:
    - Fish: Represents a fish with the ability to swim and a habitat in water.
    - Bird: Represents a bird with the ability to fly and a habitat in the sky.
    - FlyingFish: A class that inherits from both Fish and Bird, and can both
      swim and fly, with a habitat that includes both water and the sky.

Method Resolution Order (MRO) is explored with multiple inheritance in this module.
"""

class Fish:
    """
    Fish Class representing a fish.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints a message indicating the fish lives in water.
    """
    def swim(self):
        """Prints that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints that the fish lives in water."""
        print("The fish lives in water")


class Bird:
    """
    Bird Class representing a bird.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints a message indicating the bird lives in the sky.
    """
    def fly(self):
        """Prints that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints that the bird lives in the sky."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish Class that inherits from both Fish and Bird.

    This class demonstrates multiple inheritance and overrides methods from
    both parent classes.

    Methods:
        swim(): Prints a message indicating the flying fish is swimming.
        fly(): Prints a message indicating the flying fish is soaring.
        habitat(): Prints a message indicating the flying fish lives both in water and in the sky.
    """
    def swim(self):
        """Prints that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints that the flying fish lives both in water and in the sky."""
        print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    # Test FlyingFish functionality
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # Investigate Method Resolution Order (MRO)
    print(FlyingFish.mro())
