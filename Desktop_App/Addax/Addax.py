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


class App(tk.Frame):
    '''
    Fields
    '''
    serial_comm = ks_scomm.SerialComm()              
    selected_port = "NONE"
    selected_baudrate = "NONE"
    selected_mode = "NONE"
    selected_period_1 = "NONE"
    selected_duty_cycle_1 = "NONE"
    selected_period_2 = "NONE"
    selected_duty_cycle_2 = "NONE"
    selected_delay = "NONE"
    data = ""
    debug_mode = True

    '''
    Modes for holding nested frames in tabs menu
    '''
    mode_1_frame = ""
    mode_2_frame = ""
    mode_3_frame = ""
    mode_4_frame = ""
    mode_5_frame = ""
    mode_6_frame = ""

    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        '''
        Creating frames for respective modes of operation
        '''
        self.mode_1_frame = Mode_1_Frame(self)
        self.mode_2_frame = Mode_2_Frame(self)
        self.mode_3_frame = Mode_3_Frame(self)
        self.mode_4_frame = Mode_4_Frame(self)
        self.mode_5_frame = Mode_5_Frame(self)
        self.mode_6_frame = Mode_6_Frame(self)
        '''
        Creating static elements of interface
        '''

        



# creates some root element for the window
root = tk.Tk()
# sets the parent window size
root.resizable(width=False, height=False)

# creates app with input root argument
app = App(root)
# adds title
app.master.title('Addax2')
# app starts
app.mainloop()