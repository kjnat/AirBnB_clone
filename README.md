The goal of this project is to deploy on a server the clone version of the AirBnB website.

To start the command interpreter first clone the repository and locate the "console.py" file and run it.
AirBnb_clone$ console.py

A prompt will then appear like this:
(hbnb)

This prompt has built in commands of which you can use for your project:
(hbnb) quit

Your shell should look like this in the interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


But also in non-interactive mode: (like the Shell project in C)
  
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
