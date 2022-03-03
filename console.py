#!/usr/bin/python3
"""console.py contains the entry point of the command interprete"""

import cmd



class HBNBCommand(cmd.Cmd):
    """class for cmd """
    prompt = "(hbnb)"

    def do_quit(self, variable):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, variable):
        """EOF command to exit the program"""
        exit()

    def emptyline(self):
        """keep line empty"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
