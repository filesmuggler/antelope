import tkinter as tk
import tkinter.ttk as ttk

class Mode_5_Frame(tk.Frame):
    '''Fields'''
    user_freq_label_1 = ""
    user_freq_label_2 = ""
    user_duty_label_1 = ""
    user_duty_label_2 = ""
    
    user_freq_scaler_1 = ""
    user_freq_scaler_2 = ""
    user_duty_scaler_1 = ""
    user_duty_scaler_2 = ""


    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''
        Creates all the widgets in the window
        '''
        self.user_freq_label_1 = tk.Label(self, text="Period 1[us] (B)").grid(column=0,row=0, sticky=tk.W)
        self.user_freq_scaler_1 = tk.Scale(self, from_=1, to=23, resolution = 0.1, length= 300,orient=tk.HORIZONTAL)
        self.user_freq_scaler_1.grid(column=0,row=1,columnspan=2, padx=5, pady=5)

        self.user_duty_label_1 = tk.Label(self, text="Duty Cycle 1[%] (A)").grid(column=0,row=2, sticky=tk.W)
        self.user_duty_scaler_1 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.user_duty_scaler_1.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        self.user_freq_label_2 = tk.Label(self, text="Period 2[us] (D)").grid(column=0,row=4, sticky=tk.W)
        self.user_freq_scaler_2 = tk.Scale(self, from_=1, to=23, resolution = 0.1, length= 300,orient=tk.HORIZONTAL)
        self.user_freq_scaler_2.grid(column=0,row=5,columnspan=2, padx=5, pady=5)

        self.user_duty_label_2 = tk.Label(self, text="Duty Cycle 2[%] (C)").grid(column=0,row=6, sticky=tk.W)
        self.user_duty_scaler_2 = tk.Scale(self, from_=0, to=100, tickinterval = 10, length= 300,orient=tk.HORIZONTAL)
        self.user_duty_scaler_2.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
