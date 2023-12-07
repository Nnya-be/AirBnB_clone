#!/usr/bin/python3
"""commands to exit the program (quit and EOF)."""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the program."""
        print("\n")
        return True

    def emptyline(self):
        """Call when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
