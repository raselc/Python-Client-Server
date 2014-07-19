'''
Created on Jul 9, 2014

@author: Rasel
'''

import socket

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sends request to server for a customer 
def findCustomer():
    find = input("Enter Customer Name: ").lstrip().rstrip()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes("1|"+find, "utf-8"))
        # Receive data from the server and shut down
        print ( str(sock.recv(1024), "utf-8"))
    finally:
        sock.close()

# Sends details of a customer to server
def addCustomer():
    name = input("Enter Name: ").rstrip().lstrip()
    if name == '':
        print ("Invalid input ")
        return
    else:
        age = input("Enter age: ").rstrip().lstrip()
        address = input("Enter address: ").rstrip().lstrip()
        phone = input ("Enter phone number: ").rstrip().lstrip()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes('2|'+name+'|'+age+'|'+address+'|'+phone, "utf-8"))
        # Receive data from the server and shut down
        print ( str(sock.recv(1024), "utf-8"))
    finally:
        sock.close()

# Sends a request for deleting a customer      
def deleteCustomer():
    name = input("Enter Name: ").rstrip().lstrip()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes('3|'+name, "utf-8"))
        # Receive data from the server and shut down
        print ( str(sock.recv(1024), "utf-8"))
    finally:
        sock.close()

# Sends a request for updating age        
def updateAge():
    name = input("Enter Name: ").rstrip().lstrip()
    age = input("Enter Age: ").rstrip().lstrip()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes('4|'+name+'|'+age, "utf-8"))
        # Receive data from the server and shut down
        print ( str(sock.recv(1024), "utf-8"))
    finally:
        sock.close()

# Sends a request for updating Address        
def updateAddress():
    name = input("Enter Name: ").rstrip().lstrip()
    age = input("Enter Address: ").rstrip().lstrip()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes('5|'+name+'|'+age, "utf-8"))
        # Receive data from the server and shut down
        print ( str(sock.recv(1024), "utf-8"))
    finally:
        sock.close()
        
# Sends a request for updating phone
def updatePhone():
    name = input("Enter Name: ").rstrip().lstrip()
    age = input("Enter Phone: ").rstrip().lstrip()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes('6|'+name+'|'+age, "utf-8"))
        # Receive data from the server and shut down
        print ( str(sock.recv(1024), "utf-8"))
    finally:
        sock.close()
        
# Sends a request for all records
def printReport():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes('7|', "utf-8"))
        # Receive data from the server and shut down
        while True:
            field = str(sock.recv(1024), "utf-8")
            if field == "ALLdone":
                break;
            else:
                print (field)
            sock.sendall(bytes('n', "utf-8"))
        
    finally:
        sock.close()

#Displays the MENU and the starting of the program    
while True:
    print ("\nPython DB Menu")
    print ("________________")
    print ("1. Find customer")
    print ("2. Add customer")
    print ("3. Delete customer")
    print ("4. Update customer age")
    print ("5. Update customer address")
    print ("6. Update customer phone")
    print ("7. Print report")
    print ("8. Exit \n")
    selection = input("Select: ")
    
    if selection == '1':
        findCustomer()
    elif selection == '2':
        addCustomer()
    elif selection == '3':
        deleteCustomer()
    elif selection == '4':
        updateAge()
    elif selection == '5':
        updateAddress()
    elif selection == '6':
        updatePhone()
    elif selection == '7':
        printReport()
    elif selection == '8':
        print ("Good Bye")
        break
    else:
        print ("wrong input")

