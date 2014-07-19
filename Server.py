'''
Created on Jul 9, 2014

@author: Rasel
'''
import socketserver


database = {}

#loads the data.txt into database
def readData():
    file = open('data.txt','r')
    for file in iter(file.readline,''):
        if file.split('|')[0].rstrip().lstrip() != '':
            name = (file.split('|')[0]).rstrip().lstrip()
            age = (file.split('|')[1]).rstrip().lstrip()
            address = (file.split('|')[2]).rstrip().lstrip()
            phone = (file.split('|')[3]).rstrip().lstrip()
            database[name] = name +'|' +age+'|' + address+'|' + phone  
    print("database loaded")

#Finds the customer in the database and sends response
def findCustomer(find):
    if find in database:
#        print("Found")
#        print(database[find])
        return(database[find])
    else:
#        print("not Found")
        return("Customer not Found")
    
#Add a customer in the database and sends response
def addCustomer(name,age,address,phone):
    if name in database:
#        print ("data Exist")
        return("Customer Already Exist")
    database[name] = name +'|' +age+'|' + address+'|' + phone
    return ("Add Successful")

#Delete a customer in the database and sends response
def deleteCustomer(name):
    if name in database:
        del database[name]
        return ("Delete Successful")
    else:
        return("Customer does not exist")

#Update a customer's age in the database and sends response
def updateAge(name,age):
    if name in database:
        name = database[name].split('|')[0]
        address = database[name].split('|')[2]
        phone = database[name].split('|')[3]
        del database[name]
        database[name] = name +'|' +age+'|' + address+'|' + phone
        return("Age Update Successful")
    else:
        return("Customer not found")

#Update customer's address in the database and sends response    
def updateAddress(name, address):
    if name in database:
        name = database[name].split('|')[0]
        age = database[name].split('|')[1]
        phone = database[name].split('|')[3]
        del database[name]
        database[name] = name +'|' +age+'|' + address+'|' + phone
        return ("Address Update Successful")
    else:
        return("Customer not found")

#Updates a customer's phone in the database and sends response    
def updatePhone(name,phone):
    if name in database:
        name = database[name].split('|')[0]
        age = database[name].split('|')[1]
        address = database[name].split('|')[2]
        del database[name]
        database[name] = name +'|' +age+'|' + address+'|' + phone
        return("Phone Update Successful")
    else:
        return("Customer not found")

    
#the main TCP server
class MyTCPHandler(socketserver.BaseRequestHandler):
    readData();
    print ("Server is Ready for Connection!!!")
    def handle(self):
        # self.request is the TCP socket connected to the client
        data = str(self.request.recv(1024).strip(), "utf-8")
#        print(data)
        option = data.split('|')[0]
#        print (option)
        if option == '1':
            response = findCustomer(data.split('|')[1])
        if option == '2':
            response = addCustomer(data.split('|')[1],data.split('|')[2],data.split('|')[3],data.split('|')[4])
        if option == '3':
            response = deleteCustomer(data.split('|')[1])
        if option == '4':
            response = updateAge(data.split('|')[1],data.split('|')[2])
        if option == '5':
            response = updateAddress(data.split('|')[1],data.split('|')[2])
        if option == '6':
            response = updatePhone(data.split('|')[1],data.split('|')[2])
        if option == '7':
            for k,v in database.items():
                self.request.send(bytes(v,"utf-8"))
                data = str(self.request.recv(1024).strip(), "utf-8")
#                print (v)
            response = "ALLdone"
#        print (response)
        self.request.send(bytes(response,"utf-8"))
#        print (database)
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()