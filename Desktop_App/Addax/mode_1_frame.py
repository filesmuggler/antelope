import tkinter as tk
import tkinter.ttk as ttk

class Mode_1_Frame(tk.Frame):
    '''Fields'''
    user_freq_label = ""
    user_duty_label = ""
    user_freq_scaler = ""
    user_duty_scaler = ""



    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        self.user_freq_label = tk.Label(self, text="Period (B)").grid(column=0,row=0, sticky=tk.W)
        self.user_freq_scaler = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.user_freq_scaler.grid(column=0,row=1,columnspan=2, padx=5, pady=5)

        self.user_duty_label = tk.Label(self, text="Duty Cycle (A)").grid(column=0,row=3, sticky=tk.W)
        self.user_duty_scaler = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.user_duty_scaler.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
