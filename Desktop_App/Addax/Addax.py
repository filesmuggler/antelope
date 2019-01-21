# MIT License
# ---
# Microprocessor Systems Lab Project
# ---
# Program purpose: Control of ADuC831 microcontroller PWM signals
# ---
# @author: Krzysztof Stezala
# ---
# Institute of Control, Robotics and Information Engineering of
# Poznan University of Technology  

# dependecies
import tkinter as tk
import tkinter.ttk as ttk
import serial

import ks_scomm
from mode_1_frame import Mode_1_Frame
from mode_2_frame import Mode_2_Frame
from mode_3_frame import Mode_3_Frame
from mode_4_frame import Mode_4_Frame
from mode_5_frame import Mode_5_Frame
from mode_6_frame import Mode_6_Frame

from tab_frame import Tab_Frame


class Addax(tk.Frame):
    '''
    Fields
    '''
    serial_comm = ks_scomm.SerialComm()              
    selected_port = "NONE"
    chosen_port = "NONE"
    selected_baudrate = 9600
    chosen_baudrate = "NONE"
    selected_mode = "NONE"
    selected_freq_1 = "NONE"
    selected_duty_cycle_1 = "NONE"
    selected_freq_2 = "NONE"
    selected_duty_cycle_2 = "NONE"
    selected_delay = "NONE"
    data = ""
    debug_mode = True

    '''
    Elements of UI:
    1. Buttons
    2. Option Menus
    3. Labels
    4. Mode Tabs
    5. Mode Frames
    '''
    '''
    Buttons
    '''
    update_ports_button = ""
    info_ports_button = ""
    set_port_button = ""
    info_baudrate_button = ""
    set_baudrate_button = ""
    info_receive_button = ""
    receive_button = ""
    set_button = ""
    about_button = ""
    quit_button = ""
    
    '''
    Option Menus
    '''
    port_menu = ""
    baudrate_menu = ""

    '''
    Labels
    '''
    ports_label = ""
    baudrate_label = ""
    output_label = ""
    message_label = ""

    '''
    Mode tabs
    '''
    tabControl = ""
    tab_mode_1 = ""
    tab_mode_2 = ""
    tab_mode_3 = ""
    tab_mode_4 = ""
    tab_mode_5 = ""
    tab_mode_6 = ""

    '''
    Mode frames
    '''
    mode_1_frame = ""
    mode_2_frame = ""
    mode_3_frame = ""
    mode_4_frame = ""
    mode_5_frame = ""
    mode_6_frame = ""
    
    '''Separators'''
    h1_sep = ""
    h2_sep = ""
    h3_sep = ""
    v1_sep = ""
    

    def __init__(self,master=None):
        '''
        Constructor
        '''
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        1. Ports part
        2. Baudrate part
        3. Output part
        4. Modes part
        5. Buttons part
        '''

        '''Ports part'''
        self.ports_label = tk.Label(self,text="Ports").grid(column = 0, row = 0, padx=5, pady=5)
        self.update_ports_button = tk.Button(self,text="Update",command=self.updatePorts, width=8).grid(column=1,row=0, sticky=tk.E, padx=5, pady=5)
        
        self.avalaible_ports = self.serial_comm.listAllPorts()
        self.chosen_port = tk.StringVar()
        self.chosen_port.set(self.avalaible_ports[0])
        self.port_menu = tk.OptionMenu(self,self.chosen_port, *self.avalaible_ports).grid(column=0,row=1,columnspan=2,sticky=tk.W+tk.E, padx=5, pady=2)

        self.info_ports_button = tk.Button(self,bitmap="questhead", command=self.infoPorts).grid(column=0,row=2, padx=5, pady=5)
        self.set_port_button = tk.Button(self,text="Set", command=self.setPort, width=8).grid(column=1,row=2, sticky=tk.E, padx=5, pady=5)

        self.h1_sep = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=3, columnspan=2, sticky=tk.W+tk.E, padx=5, pady=5)

        '''Baudrate part'''
        self.baudrate_label = tk.Label(self,text="Baudrate").grid(column=0,row=4, padx=5, pady=5)
        self.avalaible_bauds = [9600,11520]
        self.chosen_baudrate = tk.StringVar()
        self.chosen_baudrate.set(self.avalaible_bauds[0])
        self.baudrate_menu = tk.OptionMenu(self,self.chosen_baudrate, *self.avalaible_bauds).grid(column=0, row=5, columnspan=2,sticky=tk.W+tk.E, padx=5, pady=2)
        self.h2_sep = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=7, columnspan=2, sticky=tk.W+tk.E, padx=5, pady=5)

        self.info_baudrate_button = tk.Button(self,bitmap="questhead", command=self.infoBauds).grid(column=0,row=6, padx=5, pady=5)
        self.set_baudrate_button = tk.Button(self,text="Set", command=self.setBaudrate, width=8).grid(column=1,row=6, sticky=tk.E,  padx=5, pady=5)

        '''Output part'''
        self.output_label = tk.Label(self,text="Output:").grid(column=0, row=8, sticky=tk.W, padx=5, pady=2)
 
        self.message_label = tk.Label(self,text="Message", relief=tk.SUNKEN, width=30, height = 5)
        self.message_label.grid(column=0, row=9, columnspan=2, rowspan=2,sticky=tk.W+tk.E, padx=5, pady=2)
        self.h3_sep = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=12, columnspan=5, sticky=tk.W+tk.E, padx=5)
        
        self.v1_sep = ttk.Separator(self, orient=tk.VERTICAL).grid(column=2, row=0, rowspan=12, sticky=tk.N+tk.S, padx=5)

        '''Modes part'''
   

        self.tabControl = ttk.Notebook(self)
        self.tab_mode_1 = Tab_Frame(self.tabControl,"Mode1.jpg")
        self.mode_1_frame = Mode_1_Frame(self.tab_mode_1)
        self.tab_mode_2 = Tab_Frame(self.tabControl,"Mode2.jpg")
        self.mode_2_frame = Mode_2_Frame(self.tab_mode_2)
        self.tab_mode_3 = Tab_Frame(self.tabControl,"Mode3.jpg")
        self.mode_3_frame = Mode_3_Frame(self.tab_mode_3)
        self.tab_mode_4 = Tab_Frame(self.tabControl,"Mode4.jpg")
        self.mode_4_frame = Mode_4_Frame(self.tab_mode_4)
        self.tab_mode_5 = Tab_Frame(self.tabControl,"Mode5.jpg")
        self.mode_5_frame = Mode_5_Frame(self.tab_mode_5)
        self.tab_mode_6 = Tab_Frame(self.tabControl,"Mode6.jpg")
        self.mode_6_frame = Mode_6_Frame(self.tab_mode_6)

        self.tabControl.add(self.tab_mode_1, text="Mode 1")
        self.tabControl.add(self.tab_mode_2, text="Mode 2")
        self.tabControl.add(self.tab_mode_3, text="Mode 3")
        self.tabControl.add(self.tab_mode_4, text="Mode 4")
        self.tabControl.add(self.tab_mode_5, text="Mode 5")
        self.tabControl.add(self.tab_mode_6, text="Mode 6")
        self.tabControl.grid(column=3,row=0,columnspan=2,rowspan=12,sticky=tk.N+tk.S)
        

        '''
        Buttons part
        '''
        self.quit_button = tk.Button(self, text="Quit",command=self.quit).grid(column=0,row=13, sticky=tk.W+tk.E, padx=5, pady=5)
        self.about_button = tk.Button(self, text="About",command=self.aboutProgram).grid(column=1,row=13, sticky=tk.W+tk.E, padx=5, pady=5)
        self.receive_button = tk.Button(self, text="Receive",command=self.receiveData).grid(column=3,row=13,sticky=tk.W,padx=5,pady=5)
        self.set_button = tk.Button(self,text="Set & Send",command=self.sendData).grid(column=4,row=13, sticky=tk.E, padx=5, pady=5)



    def updatePorts(self):
        print("updatePorts() needs work!")

    def infoPorts(self):
        print("infoPorts() needs work!")

    def setPort(self):
        '''
        setPort() gets the selected port from the listbox
        and its parameters
        '''
        if(self.debug_mode):
            print("setting port...")
        
        if(self.chosen_port.get()=="NONE"):
            if(self.debug_mode):
                print("Select port")
        else:
            self.selected_port = self.chosen_port.get();
            if(self.debug_mode):
                print(self.selected_port)
            self.message_label['text'] = "selecting port "+self.selected_port
            self.serial_comm.setPort(self.selected_port,self.selected_baudrate)

    def infoBauds(self):
        print("infoBauds() needs work!")

    def setBaudrate(self):
        '''
        setBaudrate() gets the selected baudrate
        '''
        if(self.debug_mode):
            print("setting baudrate...")
        
        if(self.chosen_baudrate.get()=="NONE"):
            if(self.debug_mode):
                print("Select baudrate")
        else:
            self.selected_baudrate = self.chosen_baudrate.get();
            if(self.debug_mode):
                print(self.selected_baudrate)
            self.message_label['text'] = "selecting baudrate "+self.selected_baudrate
            
    def aboutProgram(self):
        print("aboutProgram() needs some work!")

    def getData(self):
        if(self.debug_mode):
            print("getting donuts for boss...")
        self.tab_index = self.tabControl.index(self.tabControl.select())
        if(self.debug_mode):
            print(self.tab_index)
            print(self.tabControl.tab(self.tab_index))
        if(self.tab_index == 0):
            if(self.debug_mode):
                print("getting licky lollies")
            self.selected_mode = int(self.tab_index) + 1
            self.selected_duty_cycle_1 = self.mode_1_frame.user_duty_scaler.get()
            self.selected_freq_1 = (int)(1.0/((self.mode_1_frame.user_freq_scaler.get())*0.001))
        elif(self.tab_index == 1):
            if(self.debug_mode):
                print("getting pinky pies")
            self.selected_mode = int(self.tab_index) + 1
            self.selected_duty_cycle_1 = self.mode_2_frame.user_duty_scaler_1.get()
            self.selected_duty_cycle_2 = self.mode_2_frame.user_duty_scaler_2.get()
            self.selected_freq_1 = self.mode_2_frame.user_freq_scaler.get()
            self.selected_freq_2 = self.selected_freq_1

        elif(self.tab_index == 2):
            if(self.debug_mode):
                print("getting berry berries")
            self.selected_mode = int(self.tab_index) + 1
            self.selected_duty_cycle_1 = self.mode_3_frame.user_duty_scaler_1.get()
            self.selected_duty_cycle_2 = self.mode_3_frame.user_duty_scaler_2.get()
            self.selected_freq_1 = self.mode_3_frame.user_freq_scaler.get()
            self.selected_freq_2 = self.selected_freq_1
        elif(self.tab_index == 3):
            if(self.debug_mode):
                print("getting nutty nuts")
            self.selected_mode = int(self.tab_index) + 1
        elif(self.tab_index == 4):
            if(self.debug_mode):
                print("getting crispy creams")
            self.selected_mode = int(self.tab_index) + 1
            self.selected_duty_cycle_1 = self.mode_5_frame.user_duty_scaler_1.get()
            self.selected_duty_cycle_2 = self.mode_5_frame.user_duty_scaler_2.get()
            self.selected_freq_1 = self.mode_5_frame.user_freq_scaler_1.get()
            self.selected_freq_2 = self.mode_5_frame.user_freq_scaler_2.get()
        elif(self.tab_index == 5):
            if(self.debug_mode):
                print("getting dicky donuts")
            self.selected_mode = int(self.tab_index) + 1
        

    def sendData(self):
        '''
        sendData() formats output and sends data on the serial port
        '''
        # set data first
        # get current tab
        # get values based on the tab
        # set them properly
        self.getData()
        self.setPort()
        self.setBaudrate()
        self.encodeData()
        if(self.debug_mode):
            print("sending data...")
        self.serial_comm.sendData(self.data)
        self.message_label['text'] = "sending data..."
        self.message_label['fg'] = "green"

    def receiveData(self):
        self.request_for_data = "SG".encode()
        self.incoming_data = self.serial_comm.receiveData(self.request_for_data)
        self.incoming_data =  str(self.incoming_data)[:-2]
        self.message_label['text'] = str(self.incoming_data)
        self.message_label['fg'] = "blue"
        print(str(self.incoming_data))

    def encodeData(self):
        '''
        encodeData() implements text-based protocol

        TEXT-BASED PROTOCOL:
        a) single channel PWM
        S0D00F00000000E

        Content:      START|MODE NUMBER|DUTY CYCLE BLOCK|DUTY CYCLE VALUE|FREQ BLOCK|FREQ VALUE|END
        No. digits:   1    |1          |1               |2               |1         |8         |1

        b) double channel PWM
        S0D0000F0000000000000000E

        Content:      START|MODE NUMBER|DUTY CYCLE BLOCK|DUTY CYCLE VALUE1|DUTY CYCLE VALUE2|FREQ BLOCK|FREQ VALUE1|FREQ VALUE2|END
        No. digits:   1    |1          |1               |2                |2                |1         |8          |8          |1

        '''
        self.output_freq = ""
        self.output_duty_cycle = ""
        self.output_mode = ''



        if(self.debug_mode):
            print("encoding data...")
        # encode mode
        self.output_mode = self.selected_mode
        # encode duty cycle
        if(self.output_mode == 0):
            self.data = "0"
            return

        if(self.output_mode == 1):
            # single channel protocol
            if(self.debug_mode):
                print("single channel protocol")
            self.output_duty_cycle = "{0:0>2}".format(self.selected_duty_cycle_1)
            self.output_freq = "{0:0>8}".format(self.selected_freq_1)        

        else:
            # double channel protocol
            if(self.debug_mode):
                print("double channel protocol")
            self.output_duty_cycle = "{0:0>2}".format(self.selected_duty_cycle_1) + "{0:0>2}".format(self.selected_duty_cycle_2)
            if(self.debug_mode):
                print(self.output_duty_cycle)
            self.output_freq = "{0:0>8}".format(self.selected_freq_1) + "{0:0>8}".format(self.selected_freq_2)  
            if(self.debug_mode):
                print(self.output_freq)

        # set output data
        self.data = "S" + str(self.output_mode) + "D" + str(self.output_duty_cycle) + "F" + str(self.output_freq) + "E"
        print(self.data)



# creates some root element for the window
root = tk.Tk()
# sets the parent window size
root.resizable(width=False, height=False)

# creates app with input root argument
app = Addax(root)
# adds title
app.master.title('Addax')
# app starts
app.mainloop()