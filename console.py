#!/usr/bin/python3
"""console.py contains the entry point of the command interprete"""
import cmd
from models import storage
from models.base_model import BaseModel #importo la clase que traigo de model
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """class for cmd """
    prompt = "(hbnb) "
    list_class = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
    list_atrr = ["id", "created_at", "updated_at"]
    list_prefix = ["quit", "EOF", "create", "show", "destroy", "all", "update"]

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
            """Prints the string representation of an instance based on the class name and id"""
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
    
    def do_destroy(self, arg):
            """Deletes an instance based on the class name and id"""
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
                    del storage.all()[k]# si la encuentra la imprime
                    storage.save()
                else:
                    print("** no instance found **")
    
    def do_all(self, arg):
        everything = []
        arg = arg.split()
        if len(arg) == 0:
            for k, v in storage.all().items():
                everything.append(str(v))
            print(everything)
        else:
            if arg[0] not in self.list_class:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    c = k.split(".")
                    if c[0] == arg[0]:
                        everything.append(str(v))
                print(everything)
    
    def do_update(self, arg):
            """Updates an instance based on the class name and id by adding or updating attribute"""
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
                    if len(arg) == 2:
                        print("** attribute name missing **")
                    elif len(arg) == 3:
                        print("** value missing **")
                    else:
                        if arg[2] in self.list_atrr:
                            pass
                        else:
                            if arg[3][0] == "\"":
                                v = arg[3].lstrip('\"')
                                if arg[3][-1] == "\"":
                                    v = arg[3].strip('\"')
                                else:
                                    i = 1
                                    while True:
                                        if arg[3 + i][-1] == "\"":
                                            v += " " + arg[3 + i].strip('\"')
                                            break
                                        v += " " + arg[3 + i]
                                        i += 1
                            else:
                                v = arg[3]                       
                            setattr(storage.all()[k], arg[2], v)
                            storage.save()
                else:
                    print("** no instance found **")

    def precmd(self, line):
        a = line.split()
        if a[0] not in self.list_prefix and "." in a[0]:
            b = a[0].split(".")            
            line = b[1].strip("()") + " " + b[0]
        return super().precmd(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
