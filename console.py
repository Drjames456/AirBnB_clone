#!/usr/bin/python3
"""This module is a module that implements the cmd interpreter"""
if __name__ == '__main__':
    import cmd
    from models import storage
    from models.base_model import BaseModel


    class HBNBCommand(cmd.Cmd):
        """This is a class called HBNBCommand that defines a console"""
        prompt = "(hbnb) "


        def do_quit(self, arg):
            """A method that quits out of the console"""
            return True

        def do_EOF(self, line):
            """A method that exits the console using ctrl D"""
            return True

        def emptyline(self):
            """A method that returns an emptyline"""
            if self.lastcmd:
                self.lastcmd = ""
                return self.onecmd('\n')

        def do_create(self, args):
            """A method that creates new instance of the argument class"""
            arg = args.split()
            if not arg:
                print("** class name missing **")
                return
            cl = arg[0]
            if cl not in {"BaseModel"}:
                print("** class doesn't exist **")
                return
            newis = BaseModel()
            newis.save()
            print(newis.id)

        def do_show(self, args):
            """A method that prints string representation of the instance"""
            guv = args.split()
            if not guv:
                print("** class name missing **")
                return
            cl = guv[0]
            if cl not in {"BaseModel"}:
                print("** class doesn't exist **")
                return
            if len(guv) < 2:
                print("** instance id missing **")
                return
            inst = guv[1]
            key = cl + "." + inst
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])

        def do_destroy(self, args):
            """A method that deletes an instance"""
            roo = args.split()
            if not roo:
                print("** class name missing **")
                return
            cl = roo[0]
            if cl not in {"BaseModel"}:
                print("** class doesn't exist **")
                return
            if len(roo) < 2:
                print("** instance id missing **")
                return
            inst = roo[1]
            key = cl + "." + inst
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()

        def do_all(self, args):
            """A method that prints all string representation"""
            too = args.split()
            if not too:
                print([str(obj) for obj in storage.all().values()])
                return
            cl = too[0]
            if cl not in {"BaseModel"}:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in storage.all().items()
                if key.startswith(cl)])

        def do_update(self, args):
            """A method that updates an instance based on the
            class name and id"""
            coo = args.split()
            if not coo:
                print("** class name missing **")
                return
            cl = coo[0]
            if cl not in {"BaseModel"}:
                print("** class doesn't exist **")
                return
            if len(coo) < 2:
                print("** instance id missing **")
                return
            inst = coo[1]
            key = cl + "." + inst
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(coo) < 3:
                print("** attribute name missing **""")
                return
            attr = coo[2]
            if len(coo) < 4:
                print("** value missing **")
                return
            attrv = coo[3]
            obj = storage.all()[key]
            setattr(obj, attribute_name, attribute_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
