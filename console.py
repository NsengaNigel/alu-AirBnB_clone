#!/usr/bin/env python3
"""
Console module for the HBNB project.
"""
import cmd
import shlex
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter.
    """
    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User"]  # Add other classes here as you create them

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()
        
        # if not arg:
        #     print("** class name missing **")
        #     return
        # try:
        #     new_instance = eval(arg)()
        #     new_instance.save()
        #     print(new_instance.id)
        # except NameError:
        #     print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance based on class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] in self.valid_classes:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        if attr_name not in ["id", "created_at", "updated_at"]:
            setattr(obj, attr_name, attr_value)
            obj.save()

    def help_create(self):
        """Help message for the create command"""
        print("Creates a new instance of BaseModel, saves it and prints the id")
        print("Usage: create <class name>")

    def help_show(self):
        """Help message for the show command"""
        print("Prints the string representation of an instance")
        print("Usage: show <class name> <id>")

    def help_destroy(self):
        """Help message for the destroy command"""
        print("Deletes an instance based on the class name and id")
        print("Usage: destroy <class name> <id>")

    def help_all(self):
        """Help message for the all command"""
        print("Prints all string representation of all instances")
        print("Usage: all or all <class name>")

    def help_update(self):
        """Help message for the update command"""
        print("Updates an instance based on the class name and id")
        print("Usage: update <class name> <id> <attribute name> \"<attribute value>\"")


if __name__ == '__main__':
    HBNBCommand().cmdloop()