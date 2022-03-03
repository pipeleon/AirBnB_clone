#!/usr/bin/python3
"""console.py contains the entry point of the command interprete"""

from models.base_model import BaseModel #importo la clase que traigo de model
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    """class for cmd """
    prompt = "(hbnb)"
    list_class = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]


    def do_quit(self, variable):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, variable):
        """EOF command to exit the program"""
        exit()

    def emptyline(self):
        """keep line empty"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        if arg == "":
            print("** class name missing **")
        elif arg not in self.list_class:
            print("** class doesn't exist **")
        else:
            _object = eval(arg + "()")#esto es para evaluar la clase y lo guarde, ver punto 5
            _object.save()#se guarda la instancia creada
            print(_object.id)#se imprime la instancia creada

    def do_show(self, arg):
            """show de object Basemodel for ID"""
            arg = arg.split() #convertimos cadena en lista
            if len(arg) == 0:
                print("** class name missing **")
            elif arg[0] not in self.list_class:#se evalua si hay una clase
                print("** class doesn't exist **")
            elif len(arg) == 1: # evalua si no tiene id
                print("** instance id missing **")
            else:
                k = "{}.{}".format(arg[0], arg[1])
                if k in storage.all().keys():#recorro las llaves
                    print(storage.all()[k])# si la encuentra la imprime
                else:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
