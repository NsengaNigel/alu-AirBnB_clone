#!/usr/bin/python3
"""Console Module for the HBNB project"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Override the emptyline method to do nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        # Implementation...

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        # Implementation...

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        # Implementation...

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        # Implementation...

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        # Implementation...

if __name__ == '__main__':
    HBNBCommand().cmdloop()

