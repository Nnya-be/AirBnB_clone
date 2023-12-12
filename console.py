#!/usr/bin/python3
"""Command interpreter for HBNB project."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
    }
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create an instance."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if key.startswith(args[0]):
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Update an instance attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            instance = storage.all()[key]
            setattr(instance, args[2], eval(args[3]))
            instance.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, method = parts
            if method == 'all()':
                if class_name in self.classes:
                    class_instances = storage.all().values()
                    filtered_instances = [str(obj) for obj in class_instances if isinstance(obj, self.classes[class_name])]
                    print(filtered_instances)
                else:
                    print("** class doesn't exist **")
            elif method == 'count()':
                if class_name in self.classes:
                    class_instances = storage.all().values()
                    count = sum(1 for obj in class_instances if isinstance(obj, self.classes[class_name]))
                    print(count)
                else:
                    print("** class doesn't exist **")
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
