###### Functions Definitions:
#######################################################################
# Function Name: clientConnect() 
# Description:
# function is used to connect to the server from the raspberry pi
# to the computer. This is implemented using the built-in python socket module.
# We do this by defining a socket with an unused port. and connecting to the PC's
# IP address.
#######################################################################
# Function Name: takeReadings() 
# function takes the readings sent from the PC server from SIMTOOLS.
# It then slices the recieved readings to get the roll,pitch and yaw angles.
# the angles are then returned to be used in calculations later.
######
import socket
def clientConnect():
    # Create a socket object
    global socketClient
    socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
    # Define the port on which you want to connect
    port = 5050   
    # connect to the server on local computer
    socketClient.connect(('192.168.130.220', port))
    print("Connected to host PC")
def takeReadings():
    #Defining the variables            
    recieved = socketClient.recv(32768).decode()     ##### Put the recieved readings into variable
    #### The initial reading sent from PC is in format: "0,0,0,"
    #### so we split the string with "," as delimiter
    #### and assign each value to the appropriate angle.
    roll_recieved = recieved.split(",")[0]            ### Roll
    pitch_recieved = recieved.split(",")[1]           ### Pitch
    yaw_recieved = recieved.split(",")[2]             ### Yaw
    ## The following if conditional is to remove all errors and noise
    ## from our readings because sometimes we get two readings stuck together.
    if int(yaw_recieved)<1024:                              
        return [roll_recieved,pitch_recieved,yaw_recieved]
clientConnect()
while True:
    x = takeReadings()    ### This list contains the roll and pitch and yaw.
