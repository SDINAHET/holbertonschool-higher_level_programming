#!/usr/bin/python3
""" My class module
This module defines the MyClass class, which represents an object
with a name and a number. The class provides methods to create
instances of the class and to represent those instances as strings.
"""


class MyClass:
    """ My class representing a game entity with scoring capabilities.
    """

    score = 0  # Class attribute to keep track of the score.

    def __init__(self, name, number=4):
        """
        Initializes a new instance of MyClass.

        Args:
            name (str): The name of the player or team.
            number (int, optional): An integer representing some numeric value
            associated with the instance.
            Defaults to 4.
        """
        self.__name = name  # A private attribute storing the name of the
        # player or team.
        self.number = number  # A public attribute storing a numeric value.
        self.is_team_red = (self.number % 2) == 0  # Boolean indicating if the
        # number is even.

    def win(self):
        """
        Increases the score by 1 to indicate a win.

        This method is typically called when the instance wins a game or a
        round, reflecting an increase in the score. The score is a class
        attribute, meaning it is shared across all instances of MyClass.

        Example:
            >>> my_class_instance = MyClass("Team A")
            >>> my_class_instance.win()
            >>> my_class_instance.score
            1
        """
        self.score += 1  # Increment the score by 1.

    def lose(self):
        """
        Decreases the score by 1 to indicate a loss.

        This method is typically called when the instance loses a game or a
        round, reflecting a decrease in the score. The score is a class
        attribute, meaning it is shared across all instances of MyClass.

        Example:
            >>> my_class_instance = MyClass("Team A")
            >>> my_class_instance.win()  # score becomes 1
            >>> my_class_instance.lose()  # score becomes 0
            >>> my_class_instance.score
            0
        """
        self.score -= 1  # Decrement the score by 1.

    def __str__(self):
        """
        Returns a string representation of the MyClass instance.

        This string includes the name, number, and current score of the
        instance, formatted for easy readability.

        Returns:
            str: A formatted string describing the instance.
        """
        return "[MyClass] {} - {:d} => {:d}".format(
            self.__name, self.number, self.score)

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object. Ensures 'number' comes first in the dictionary.
    """
    # Extract the object's attributes as a dictionary
    obj_dict = obj.__dict__

    # Create a new dictionary with 'number' as the first key, if it exists
    ordered_dict = {}
    
    if 'number' in obj_dict:
        ordered_dict['number'] = obj_dict.pop('number')

    # Add the remaining attributes
    ordered_dict.update(obj_dict)

    return ordered_dict
