#!/usr/bin/python3
"""Defines the HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handles EOF to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of a given class."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()  # Evaluate if the class exists
            new_instance.save()         # Save to file
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of instances."""
        if arg:
            if arg not in storage.classes():
                print("** class doesn't exist **")
                return
            objects = [str(obj) for key, obj in storage.all().items() if key.startswith(arg)]
        else:
            objects = [str(obj) for obj in storage.all().values()]
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on class name, id, and attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"')
        # Cast to correct type (handle string, int, float)
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif '.' in attr_value:
                attr_value = float(attr_value)
        except ValueError:
            pass
        setattr(instance, attr_name, attr_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()


