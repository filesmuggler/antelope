# MIT License
# ---
# Microprocessor Systems Lab Project
# ---
# Program purpose: Set PWM parameters and send them 
# over previously chosen serial port.
# ---
# @author: Krzysztof Stezala
# ---
# Institute of Control, Robotics and Information Engineering of
# Poznan University of Technology  

# dependecies
import tkinter as tk
import tkinter.ttk as ttk
import ks_scomm
import serial

# App inherits from tk.Frame class to 
# become the window in our world
class App(tk.Frame):
    s_comm = ks_scomm.SerialComm()
    selected_port = "NONE"
    selected_mode = "NONE"
    selected_freq_1 = "NONE"
    selected_filling_1 = "NONE"
    selected_freq_2 = "NONE"
    selected_filling_2 = "NONE"
    data = ""
    debug_mode = True

    '''
    Widgets for ch#2 panel
    '''
    channel_panel_2 = []


    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        
        '''
        Port Selection Group
        '''
        self.portsLabel = tk.Label(self,text="Ports:")
        self.portsLabel.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
       
        self.portsButton = tk.Button(
            self, text="Set Port", command=self.setPort
            )
        self.portsButton.grid(column=1, row=0, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)

        self.yScroll1 = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll1.grid(row=1, column=2, sticky=tk.N+tk.S+tk.E)

        self.portsList = tk.Listbox(self, height=3, width=40, selectmode=tk.SINGLE)
        self.portsList.grid(column=0,row=1, columnspan=2)

        self.avalaible_ports = self.s_comm.listAllPorts()
        for item in self.avalaible_ports:
            self.portsList.insert(tk.END, item)
       
        self.portsList.config(yscrollcommand=self.yScroll1.set)
        self.yScroll1.config(command=self.portsList.yview)
        '''
        Vertical Separator Group
        '''
        self.v_separator_1 = ttk.Separator(self, orient=tk.VERTICAL).grid(column=3, row=0, rowspan=5, sticky=tk.N+tk.S)
        
        '''
        Horizontal Separator Group
        '''
        self.h1_separator = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=2, columnspan=3, sticky=tk.W+tk.E)
        
        '''
        Mode Selection Group
        '''
        self.modesLabel = tk.Label(self,text="Modes:")
        self.modesLabel.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
       
        self.modesButton = tk.Button(
            self, text="Set Mode", command=self.setMode
            )
        self.modesButton.grid(column=1, row=3, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)

        self.yScroll2 = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll2.grid(row=4, column=2, sticky=tk.N+tk.S+tk.E)

        self.modesList = tk.Listbox(self, height=4, width=40, selectmode=tk.SINGLE)
        self.modesList.grid(column=0,row=4, columnspan=2)

        self.avalaible_modes = ["Mode 0","Mode 1","Mode 2","Mode 3","Mode 4", "Mode 5", "Mode 6"]
        for item in self.avalaible_modes:
            self.modesList.insert(tk.END, item)
       
        self.modesList.config(yscrollcommand=self.yScroll2.set)
        self.yScroll2.config(command=self.portsList.yview)

        '''
        Output Message Group
        '''
        self.outputLabel = tk.Label(self,text="Output:")
        self.outputLabel.grid(column=0, row=6, sticky=tk.W, padx=5, pady=2)
 
        self.messageLabel = tk.Label(self,text="Message", relief=tk.SUNKEN, height = 2)
        self.messageLabel.grid(column=0, row=7, columnspan=11, rowspan=7,sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=2)
        
        
        '''
        Horizontal Separator Group
        '''
        self.h2_separator = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=5, columnspan=11, sticky=tk.W+tk.E)


        '''
        Frequency 1 Group
        '''
        self.freqLabel_1 = tk.Label(self,text="CH#1 Frequency")
        self.freqLabel_1.grid(column=4, row=0, columnspan=2, sticky=tk.N+tk.S+tk.W, padx=5, pady=5)

        self.freqButton_1 = tk.Button(
            self, text="Set", command=self.setFreq_1
            )
        self.freqButton_1.grid(column=6,row=0, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)

        self.freqScaler_1 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.freqScaler_1.grid(row=1, column=4, columnspan=3, padx=5, pady=5)

        
        '''
        Vertical Separator Group
        '''
        self.v_separator_2  = ttk.Separator(self, orient=tk.VERTICAL).grid(column=7, row=0, rowspan=5, sticky=tk.N+tk.S)
        
        
        '''
        Frequency 2 Group
        '''
        self.freqLabel_2 = tk.Label(self,text="CH#2 Frequency")
        self.freqLabel_2.grid(column=8, row=0, columnspan=2, sticky=tk.N+tk.S+tk.W, padx=5, pady=5)
        self.channel_panel_2.append(self.freqLabel_2)

        self.freqButton_2 = tk.Button(
            self, text="Set", command=self.setFreq_2
            )
        self.freqButton_2.grid(column=10,row=0, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)
        self.channel_panel_2.append(self.freqButton_2)

        self.freqScaler_2 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.freqScaler_2.grid(row=1, column=8, columnspan=3, padx=5, pady=5)
        self.channel_panel_2.append(self.freqScaler_2)
        
        '''
        Horizontal Separator Group
        '''
        self.h3_separator = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=4, row=2, columnspan=7, sticky=tk.W+tk.E)
        
        '''
        Duty Cycle 1 Group
        '''
        self.fillingLabel_1 = tk.Label(self,text="CH#1 Duty Cycle")
        self.fillingLabel_1.grid(column=4, row=3, columnspan=2, sticky=tk.N+tk.S+tk.W, padx=5, pady=5)

        self.fillingButton_1 = tk.Button(
            self, text="Set", command=self.setFilling_1
            )
        self.fillingButton_1.grid(column=6,row=3, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)

        self.fillingScaler_1 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.fillingScaler_1.grid(row=4, column=4, columnspan=3, padx=5, pady=5)

        '''
        Duty Cycle 2 Group
        '''
        self.fillingLabel_2 = tk.Label(self,text="CH#2 Duty Cycle")
        self.fillingLabel_2.grid(column=8, row=3, columnspan=2, sticky=tk.N+tk.S+tk.W, padx=5, pady=5)
        self.channel_panel_2.append(self.fillingLabel_2)

        self.fillingButton_2 = tk.Button(
            self, text="Set", command=self.setFilling_2
            )
        self.fillingButton_2.grid(column=10,row=3, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)
        self.channel_panel_2.append(self.fillingButton_2)

        self.fillingScaler_2 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.fillingScaler_2.grid(row=4, column=8, columnspan=3, padx=5, pady=5)
        self.channel_panel_2.append(self.fillingScaler_2)

        '''
        Horizontal Separator Group
        '''
        self.h4_separator = ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=14, columnspan=11, sticky=tk.W+tk.E)

        '''
        Button group
        '''        
        self.quitButton = tk.Button(
            self, text="Quit", command=self.quit
            )
        self.quitButton.grid(column=0,row=15, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)

        self.randButton = tk.Button(
            self, text="Random", command=self.randSignal
            )
        self.randButton.grid(column=8,row=15, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)

        self.sendButton = tk.Button(
            self, text="Send", command=self.sendData
            )
        self.sendButton.grid(column=10,row=15, sticky=tk.N+tk.S+tk.W+tk.E, padx=5, pady=5)
        
    def setPort(self):
        '''
        setPort() gets the selected port from the listbox
        and its parameters
        '''
        if(self.debug_mode):
            print("setting port...")
        if(not self.portsList.curselection()):
            if(self.debug_mode):
                print("Select port")
        else:
            self.selected_port = self.portsList.get(self.portsList.curselection());
            if(self.debug_mode):
                print(self.selected_port)
            self.messageLabel['text'] = "selecting port "+self.selected_port
            self.s_comm.setPort(self.selected_port,9600)

    def setMode(self):
        '''
        setMode() gets the selected mode from the listbox
        and its parameters
        '''
        if(self.debug_mode):
            print("setting mode...")
        if(not self.modesList.curselection()):
            if(self.debug_mode):
                print("Select mode")
            self.messageLabel['text'] = "Select Mode First!"
            self.messageLabel['fg'] = "red"
        else:
            self.selected_mode = self.modesList.get(self.modesList.curselection());
            if(self.debug_mode):
                print(self.selected_mode)
            self.messageLabel['text'] = "selecting mode "+self.selected_mode
            self.messageLabel['fg'] = "green"
            if(self.selected_mode == "Mode 1"):
                #disable ch#2 panel
                for item in self.channel_panel_2:
                    item.config(state=tk.DISABLED)
            else:
                #enable ch#2 panel
                for item in self.channel_panel_2:
                    item.config(state=tk.NORMAL)

        

    def setFreq_1(self):
        if(self.debug_mode):
            print("setting freq 1...")
        self.selected_freq_1 = self.freqScaler_1.get()
        self.messageLabel['text'] = "setting frequency 1..."
        self.messageLabel['fg'] = "green"

    def setFreq_2(self):
        if(self.debug_mode):
            print("setting freq 2...")
        self.selected_freq_2 = self.freqScaler_2.get()
        self.messageLabel['text'] = "setting frequency 2..."
        self.messageLabel['fg'] = "green"

    def setFilling_1(self):
        if(self.debug_mode):
            print("setting filling 1...")
        self.selected_filling_1 = self.fillingScaler_1.get()
        self.messageLabel['text'] = "setting duty cycle 1..."
        self.messageLabel['fg'] = "green"

    def setFilling_2(self):
        if(self.debug_mode):
            print("setting filling 2...")
        self.selected_filling_2 = self.fillingScaler_2.get()
        self.messageLabel['text'] = "setting duty cycle 2..."
        self.messageLabel['fg'] = "green"

    def randSignal(self):
        if(self.debug_mode):
            print("generating random params...")
        self.messageLabel['text'] = "generating random..."
        self.messageLabel['fg'] = "green"

    
    def sendData(self):
        '''
        sendData() formats output and sends data on the serial port
        '''
        self.encodeData()
        if(self.debug_mode):
            print("sending data...")
        self.s_comm.sendData(self.data)
        self.messageLabel['text'] = "sending data..."
        self.messageLabel['fg'] = "green"


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
        self.output_mode = self.selected_mode[-1:]
        # encode duty cycle
        if(self.output_mode == '0'):
            self.data = "0"
            return

        if(self.output_mode == '1'):
            # single channel protocol
            if(self.debug_mode):
                print("single channel protocol")
            self.output_duty_cycle = "{0:0>2}".format(self.selected_filling_1)
            self.output_freq = "{0:0>8}".format(self.selected_freq_1)        

        else:
            # double channel protocol
            if(self.debug_mode):
                print("double channel protocol")
            self.output_duty_cycle = "{0:0>2}".format(self.selected_filling_1) + "{0:0>2}".format(self.selected_filling_2)
            self.output_freq = "{0:0>8}".format(self.selected_freq_1) + "{0:0>8}".format(self.selected_freq_2)       

        # set output data
        self.data = "S" + self.output_mode + "D" + self.output_duty_cycle + "F" + self.output_freq + "E"
        print(self.data)


# creates some root element for the window
root = tk.Tk()
# sets the parent window size
root.resizable(width=False, height=False)

# creates app with input root argument
app = App(root)
# adds title
app.master.title('Macaque')
# app starts
app.mainloop()
