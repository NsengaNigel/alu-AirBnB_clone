#!/usr/bin/python3
"""Console Module for the HBNB Project"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""
    prompt = "(hbnb) "  # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def emptyline(self):
        """Override the emptyline method to do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
