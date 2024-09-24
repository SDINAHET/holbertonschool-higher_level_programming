#!/usr/bin/python3
"""
Module that demonstrates the use of Mixins in Python.

This module includes two mixin classes that provide specific behaviors:
    - SwimMixin: Adds the ability to swim.
    - FlyMixin: Adds the ability to fly.

It also includes a Dragon class that inherits from both mixins and demonstrates
how a dragon can both swim and fly.

Classes:
    - SwimMixin: Mixin class providing swim functionality.
    - FlyMixin: Mixin class providing fly functionality.
    - Dragon: A class that inherits from SwimMixin and FlyMixin, and has additional behaviors.
"""

class SwimMixin:
    """
    SwimMixin Class that provides swimming functionality.

    Methods:
        swim(): Prints a message indicating the creature swims.
    """
    def swim(self):
        """Prints that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """
    FlyMixin Class that provides flying functionality.

    Methods:
        fly(): Prints a message indicating the creature flies.
    """
    def fly(self):
        """Prints that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon Class that inherits from SwimMixin and FlyMixin.

    The dragon can swim, fly, and has an additional behavior to roar.

    Methods:
        roar(): Prints a message indicating the dragon roars.
    """
    def roar(self):
        """Prints that the dragon roars."""
        print("The dragon roars!")


if __name__ == "__main__":
    # Test Dragon functionality
    draco = Dragon()
    draco.swim()  # Outputs: The creature swims!
    draco.fly()   # Outputs: The creature flies!
    draco.roar()  # Outputs: The dragon roars!
