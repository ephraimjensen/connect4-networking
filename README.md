# Overview

This program is a connect 4 game that allows two players to play a game of connect 4 over local area network. To start this program, edit the client code (client.py) such that HOST is equal to the IP you will be running the server from. Next, run the server code (server.py). Third, run the client code on two different devices that are on the same local network or a Virtual Machines on your computer. Finally, follow the prompts on the screen of the client machines and try to beat the other player at Connect 4.


I wrote this software to learn how networking and threading work so that I can use them in future projects.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://www.loom.com/share/07d529fec0c24aefbc68d63c8a58b8e4)

# Network Communication

I used a client/server model where there are two clients that can make requests from the server. 

I am using TCP to send messages on Port 80.

The messages being sent to the server from the client have an operation code at the start of the message and then context specific content after that. The messages being sent from the server to the client are completely context dependant. All messages must be shorter than 1024 bytes. 

# Development Environment

I used VS Code to write this code and used Windows Subsystem for Linux to run a Kali Linux and a Ubuntu installation to run the client code as I was testing. 

I built this program in Python and used the following modules: socket, threading, os, ast, and time.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python Sockets Documentation](https://docs.python.org/3/howto/sockets.html)
* [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
* [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=%0A)
* [Geeks For Geeks](https://www.geeksforgeeks.org/multithreading-python-set-1/)



# Future Work

 * display finished board on Win/Lose screen
 * better input verification (client side)
 * maybe try to make sends/recieves non-blocking and more dynamic
 * maybe rewrite code according to a pattern of sends and recieves 


