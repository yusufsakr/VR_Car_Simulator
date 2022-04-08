import serial
import socket
# COM6 : SIMTools COM
# COM2 : Python Com
# COM6 --> COM2 from virtual port software.
# identifying serial com and baudrate

ser = serial.Serial(
    port='COM2',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
##############################
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ##### Creating a socket        
print ("Socket successfully created")    ## Indicator that the socket creation was successfull
port = 5050                                ### Declaring a random unused port
socketServer.bind(('', port))                          ### Binding the socket to the port and making it open to all devices in the network
print ("socket binded to %s" %(port))       ### Indicator that the socket is binded
socketServer.listen(5)                                 ### Configuring the socket to listen if anyone connects
print ("socket is listening")               ### Indicator that the socket is listening
ourIP = socket.gethostbyname(socket.gethostname())
print("The host IP is : "+ourIP)
#################################
print("Connected to: " + ser.portstr) #   <--- Making sure we're connected to COM2
client1, addr = socketServer.accept()                                                 ### At this point, a client is trying to connect to the server. 
                                                                     ### This line accepts that connection and takes the hostname and address
print ('Got connection from', addr )                                 ### Indicator that the connection has been made from "Address"
if addr:                                                             ### If there's a connection:

    while(True):                                                     #### Infinite loop to send readings

            reading = ser.read(17)                                      ### This line reads from serial communication(SIMTOOLS)
            if "P" in str(reading):                                     ##### Used this line to remove empty readings.

                reading_string = str(reading)                         ###### Turning the byte into string
                reading_string = reading_string[2:]                  ###### Removing first character "b" and quote from beginning of string
                reading_string = reading_string[:-1:] + ","          ####### Removing quote at the end of the bytearray and adding "," at the end to use as a delimiter later
                indiv_reading=[]                                     ####### We put individual readings into this list to join later into 
                final_list=[]                                        ####### Final list after joining each number.

                if reading_string[0] =="R":                                       ####### If the reading has no errors or overlapping characters <--- This means that the reading is correct from simtools

                    for character in reading_string:                                      ######## This loop to remove P,R,Y from string

                        if character == "P" or character == "R" or character =="Y":          #### Iterating over all characters of the reading, and only adding integers, thus removing P,R,Y from string.
                            pass
                        else:
                            if character != ",":               ######### Split string into numbers using "," as delimiter

                                indiv_reading.append(character)   #### append each number into string to join later and add to final list

                            elif character == ",":                ####### If i is equal to "," this means that we reached the end of the integer.

                                joined ="".join(indiv_reading)   #### join the list using "," as a delimiter 
                                joined= joined+","               #### add a "," to the final index because it doesn't contain "," by default <== to use in slicing when sending over server.
                                final_list.append(joined)        #### append the joined list into the final list that contains all values
                                indiv_reading=[]                 #### reset first list to re-use again.

                    final_list_string="".join(final_list)
                    if len(final_list)==3:                  ### Some readings had errors, so this line ensures that the readings we're getting are the correct readings.
                        client1.send(final_list_string.encode())
