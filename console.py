#!/usr/bin/python3
"""This module is a module that implements the cmd interpreter"""
if __name__ == '__main__':
    import cmd


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
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
