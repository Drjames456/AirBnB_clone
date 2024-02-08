The AirBnB project is a web application composed of a command line interpreter to manipulate data without visual interface,a website (the front-end),and an API that provides a communication interface between the front-end and the database(to retrieve, create, delete,and  update).
The command interpreter is a purely python shell to receive command and execute it. It works as a line-oriented command interpreter that inherits from a python module called cmd (command).
It can be started using the command "python script.py"(where script is the module containing the source code) on the terminal.
usage(example):
Ædenubuntu#/: python script.py
Welcome to the cmd interpreter

type help for more info on command1, command2.
=============================================

(cmd)> help command1
command1 does what command1 does
(cmd)> help quit
quit closes the or breaks out of the cmdloop()
(cmd)> quit
Ædenubuntu#/:

The above description shows how the interpreter works by running the script.
The above message 'Welcome to the cmd interpreter' is an intro from the cmd module and information 'type help for more info on command1, command2' is a message to give more information on each commands(method).
The (cmd)> is a prompt that continously recieves command until the user quitsfrom it.
