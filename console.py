#!/usr/bin/python3
import cmd
import shlex
import sys
import json
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.place import Place

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'State': State,
        'Place': Place
    }

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, args):
        """ Create an object of any class with given parameters."""
        if not args:
            print("** class name missing **")
            return

        parts = args.split(" ", 1)
        class_name = parts[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        params = {}

        if len(parts) > 1:
            param_str = parts[1]

            # Use shlex to handle quoted strings and split into a list of parameters
            param_list = shlex.split(param_str)

            for param in param_list:
                if "=" in param:
                    key, value = param.split("=", 1)

                    # Handle string values enclosed in double quotes
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]  # Remove the surrounding quotes
                        value = value.replace("\\\"", "\"")  # Unescape any escaped quotes
                        value = value.replace("_", " ")  # Replace underscores with spaces

                    # Handle float values containing a dot
                    elif '.' in value:
                        try:
                            value = float(value)
                        except ValueError:
                            continue  # Skip if the value can't be converted to float

                    # Handle integer values
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            continue  # Skip if the value can't be converted to integer

                    # Add the key-value pair to the dictionary
                    params[key] = value

        # Create an instance of the specified class with the parameters
        new_instance = HBNBCommand.classes[class_name](**params)

        # Save the new instance to storage
        new_instance.save()
        print(new_instance.id)

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instances = storage.all().values()
        filtered_instances = [str(instance) for instance in instances if instance.__class__.__name__ == class_name]
        print(filtered_instances)


    def do_EOF(self, args):
        """Exits the program cleanly"""
        print("")
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def precmd(self, line):
        """Called before executing the command; handles post-processing of commands."""
        if line != "EOF":
            print(line)
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()

