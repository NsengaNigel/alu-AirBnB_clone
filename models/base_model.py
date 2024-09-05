#!/usr/bin/python3

"""
This is a sample module.
"""

def greet(name: str) -> None:
    """
    Print a personalized greeting message.

    Args:
        name (str): The person's name.

    Returns:
        None
    """
    print(f"Hello, {name}!")

class Person:
    """
    A class representing a person.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person object.

        Args:
            name (str): The person's name.
            age (int): The person's age.

        Returns:
            None
        """
        self.name = name
        self.age = age

    def say_hello(self) -> None:
        """
        Print a greeting message.

        Returns:
            None
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
    person = Person("John Doe", 30)
    person.say_hello()
