# MIT License
# ---
# Microprocessor Systems Lab Project
# ---
# Program purpose: Serial communication class.
# ---
# @author: Krzysztof Stezala
# ---
# Institute of Control, Robotics and Information Engineering of
# Poznan University of Technology  

# dependecies
import sys
import glob
import serial

class SerialComm:
    debug_mode = True
    serial_port = ''

    def __init__(self):
        if(self.debug_mode):
            print("Debug mode enabled")
            print("object created")

    def listAllPorts(self):
        '''
        Lists all serial ports avalaible on the given machine
        
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        '''
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i+1) for i in range(25)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                serial_port = serial.Serial(port)
                serial_port.close()
                result.append(port)
                #print("port found")
            except (OSError, serial.SerialException):
                #print("port exception")
                pass
        return result

    def setPort(self, port_name, speed):
        if(self.debug_mode):
            print("creating port")
        self.serial_port = serial.Serial(port_name, speed, timeout=1)
        self.serial_port.close()

    def sendData(self, data):
        data = data.encode() 
        if(self.debug_mode):
            print("opening: ")
            print(self.serial_port.open())
            self.serial_port.write(data)
            print("closing: ")
            print(self.serial_port.close())
                    
        else:
            self.serial_port.open()
            self.serial_port.write(data)
            self.serial_port.close()

    def receiveData(self, data):
        self.serial_port.open()
        self.serial_port.write(data)
        incoming_data = self.serial_port.readline()
        self.serial_port.close()
        incoming_data = incoming_data.decode()

        return incoming_data

       
